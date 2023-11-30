from flask import Flask, render_template, request, url_for, redirect, session, jsonify
from app import app, db
from forms import GameSetupForm, PlayerDataForm
from models import Card
from flashcard_generator import CardGenerator
from player_generator import PlayerGenerator

card_generator = CardGenerator(db)

# Rules and explainer page
@app.route('/rules', methods=['GET', 'POST'])
def rules():
    return render_template('rules.html')


@app.route('/about-me', methods=['GET', 'POST'])
def about_me():
    return render_template('aboutme.html')


# Game settings input page
# Records session variables of game settings to be passed later
@app.route('/game-setup', methods=['GET', 'POST'])
def game_setup():
    game_setup_form = GameSetupForm()

    if game_setup_form.validate_on_submit():
        # Handle game setup data
        game_mode = game_setup_form.game_mode.data
        num_teams = int(game_setup_form.num_teams.data)
        time_limit = int(game_setup_form.time_limit.data)
        game_type = game_setup_form.game_type.data
        num_rounds = int(game_setup_form.num_rounds.data) if game_type == 'multi-round' else 1
        category = game_setup_form.category.data

        session['game_setup_data'] = {
            'game_mode': game_mode,
            'num_teams': num_teams,
            'time_limit': time_limit,
            'game_type': game_type,
            'num_rounds': num_rounds,
            'category': category
            }
               
        return redirect(url_for('player_data'))
    
    print(game_setup_form.errors)


    player_data_form = PlayerDataForm(request.form)

    return render_template('game_setup.html', game_setup_form=game_setup_form, player_data_form=player_data_form)

# Handles player data form entry as well as team selection
@app.route('/player-data', methods=['GET', 'POST'])
def player_data():
    # Initialize player data entry form
    player_data_form = PlayerDataForm(request.form)

    # Initialize session objects of previous game data and number of teams
    game_settings = session.get('game_setup_data')
    num_teams = game_settings['num_teams']
    new_players = []
        
        # create the team_data session object in the form of a dictionary by passing a dict as the default value
    team_data = session.get('team_data', {})

    if request.method == 'POST' and player_data_form.validate_on_submit():
        # Get the most recent name that has been added
        new_player_name = player_data_form.player_names.entries[-1].data
        new_players.append(new_player_name)

        # Check if a team has been selected for the player
        selected_team = request.form.get('team')
        if selected_team and selected_team in team_data:
            team_data[selected_team].append(new_player_name)
        else:
            # If no team is selected or the team doesn't exist, assign the player to a default team
            default_team = f'Team 1'
            if default_team in team_data:
                team_data[default_team].append(new_player_name)
            else:
                team_data[default_team] = [new_player_name]

        #session object team data is updated with the contents of the team_data dict in this route
        session['team_data'] = team_data

    return render_template('player_data.html', game_settings=game_settings, player_data_form=player_data_form, team_data = team_data, new_players=new_players, team_names=list(range(1, num_teams + 1)), num_teams = num_teams)



#Removes a player from a team and the team storage
@app.route('/player/<team>/<player>', methods=['DELETE'])
def remove_player(team, player):
    team_data = session.get('team_data')

    if team in team_data and player in team_data[team]:
        team_data[team].remove(player)
    
    session['team_data'] = team_data

    return jsonify({'status': 'success'})



# Adds a player to a team and name logic
@app.route('/add_player_to_team', methods=['POST'])
def add_player_to_team():
    team = request.form.get('team')  # Get the selected team from the form
    player_name = request.form.get('player_name')  # Get the player's name from the form

    if player_name.strip():  # Check if the player name is not blank or contains only whitespace
        team_data = session.get('team_data', {})

        # Add the player to the selected team
        if team in team_data:
            team_data[team].append(player_name)
        else:
            # If the team doesn't exist, create it and add the player
            team_data[team] = [player_name]

        session['team_data'] = team_data

    return redirect('/player-data')


# Teams and players display and storage
@app.route('/get_teams_and_players', methods=['GET'])
def get_teams_and_players():
    # Retrieve team_data 
    team_data = session.get('team_data', {})
    game_settings = session.get('game_setup_data', {})
    num_teams = game_settings.get('num_teams', 0)
    
    
    # Check if there are no players assigned to teams
    if all(len(players) == 0 for players in team_data.values()):
        return "There are currently 0 players assigned to teams"

    return render_template('teams_and_players.html', team_data=team_data, num_teams=num_teams)
   
# Route for card gen based on generator
@app.route('/generate_random_card', methods=['GET'])
def generate_random_card():
    # Call the generate_random_card function to get a random card
    random_card = card_generator.generate_random_card()

    # Convert the card information to a dictionary
    card_data = {
        'Key Word': random_card.key_word_category.key_word,
        'Key Character': random_card.key_character_category.key_character,
        'Exams Skills': random_card.exam_skills_category.exam_skill,
        'Grammar Rules': random_card.grammar_rules_category.grammar_rule,
        'Spellings': random_card.spellings_category.spellings
    }

    # Return the card data as a JSON response
    return jsonify(card_data)


# Game instance routing
@app.route('/playing-game', methods=['GET', 'POST'])
def game_instance():
    # Retrieve game settings and player data from the session
    game_settings = session.get('game_setup_data')
    team_data = session.get('team_data')

    # Initialize game state (scores, current card, passes)
    game_state = session.get('game_state', {
        'scores': {player: 0 for team, players in team_data.items() for player in players},
        'passes': {player: 0 for team, players in team_data.items() for player in players},
           })


    return render_template('game_instance.html', game_settings=game_settings, team_data=team_data,
                           game_state=game_state)

@app.route('/get-session-data')
def get_session_data():
    game_setup_data = session.get('game_setup_data', {})
    team_data = session.get('team_data', {})
    is_turn_session_active = session.get('is_turn_session_active', False)
    
    return jsonify({
        'game_setup_data': game_setup_data,
        'team_data': team_data,
        'is_turn_session_active': is_turn_session_active
    })

player_generator = PlayerGenerator([])

# Next player 
@app.route('/next-player', methods=['POST'])
def next_player():
    team_data = session.get('team_data')
    players = [player for players in team_data.values() for player in players]

    player_generator.players = players
    
    current_player, next_player = next(player_generator, (None, None))

    player_info = {
        'current_player': current_player,
        'next_player': next_player,
           }
    
    if next_player is None:
        
        final_turn = {
        'current_player': current_player,
          }

        return jsonify(final_turn)

    return jsonify(player_info)






@app.route('/update-pass-score', methods=['POST'])
def update_pass_score():
    data = request.get_json()  # Get the data from the request

    # Retrieve the current player's name and scoring data from the session
    current_player = data.get('current_player')
    scoring = session.get('scoring', {})

    # Update the pass score for the current player
    if current_player in scoring:
        scoring[current_player]['passes'] += 1

    # Store the updated scoring data in the session
    session['scoring'] = scoring

    return jsonify({'passes': scoring.get(current_player, {}).get('passes', 0)})



@app.route('/update-correct-score', methods=['POST'])
def update_correct_score():
    data = request.get_json()  # Get the data from the request
    
    current_player = data.get('current_player')
    scoring = session.get('scoring', {})

    # Update the pass score for the current player
    if current_player in scoring:
        scoring[current_player]['correct'] += 1


    # Process and update the player's score here, similar to updating the pass score
        # Store the updated scoring data in the session
    session['scoring'] = scoring

    return jsonify({'correct': scoring.get(current_player, {}).get('correct', 0)})

    
