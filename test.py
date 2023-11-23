# # # from flask import Flask, render_template, request, url_for, redirect, session
# # # from app import app
# # # from forms import GameSetupForm, PlayerDataForm

# # # @app.route('/player-data', methods=['GET', 'POST'])
# # # def player_data():
# # #     #initialize player data entry form
# # #     player_data_form = PlayerDataForm(request.form)

# # #     #intialize session objects of previous game data and number of teams 
# # #     game_settings = session.get('game_setup_data')
# # #     num_teams = game_settings['num_teams']
   
# # #     if player_data_form.validate_on_submit():
# # #         #gets the most recent name that has been added
# # #         new_player_name = player_data_form.player_names.entries[-1].data

# # # return render_template('player_data.html', player_data_form=player_data_form, team_names=team_names, player_names=player_names)

# # # establishes a route for the player data page
# # # establishes the form for player data entry
# # # recalls the game settings session object so that the number of teams in the game can be accessed

# # # iterate over the number of teams and return the formatted string as options in the dropdown - team f{1}, team 2 etc
# # # new user names are added to the page so that users can see their players





# # @app.route('/player-data', methods=['GET', 'POST'])
# # def player_data():
# #     player_data_form = PlayerDataForm(request.form)

# #     # Initialize or get the player data from the session
# #     player_data = session.get('player_data', {'team_names': [], 'player_names': []})
# #     team_names = player_data['team_names']
# #     player_names = player_data['player_names']

# #     if player_data_form.validate_on_submit():
# #         # Handle the form data
# #         new_team_name = player_data_form.team_names.entries[-1].data
# #         new_player_name = player_data_form.player_names.entries[-1].data

# #         # Add the new data to the existing lists
# #         team_names.append(new_team_name)
# #         player_names.append(new_player_name)

# #         # Update the session data
# #         player_data['team_names'] = team_names
# #         player_data['player_names'] = player_names
# #         session['player_data'] = player_data

# #     return render_template('player_data.html', player_data_form=player_data_form, team_names=team_names, player_names=player_names)


# def add_player_to_team():
#     team = team_and_players



# # Add this route to remove players
# @app.route('/remove_player/<team>/<player>', methods=['GET'])
# def remove_player(team, player):
#     team_data = session.get('team_data')
#     game_settings = session.get('game_setup_data')
#     #if the key is in dict of teams and value in that key
#     if team in team_data and player in team_data[team]:
#         #access the value of that key and remove that value.
#         team_data[team].remove(player)

#     session['team_data'] = team_data

#     return redirect('/player-data')

    # return render_template('player_data.html', player_data_form = player_data_form, new_players=new_players, teams_and_players = teams_and_players)


##old remove player from list routing
# @app.route('/remove_item/<item_type>/<name>', methods=['GET'])
# def remove_item(item_type, name):
#     player_data = session.get('player_data', {'team_names': [], 'player_names': []})

#     if name.strip():  # Check if the name is not blank or contains only whitespace
#         if item_type == 'team':
#             if name in player_data['team_names']:
#                 player_data['team_names'].remove(name)
#         elif item_type == 'player':
#             if name in player_data['player_names']:
#                 player_data['player_names'].remove(name)

#         session['player_data'] = player_data

#     return redirect('/player-data')



# Remove Button no JS

# <h3>Current Players:</h3>
# <ul>
#   {% for team, players in team_data.items() %}
#     {% for player in players %}
#       <li>{{ player }}
#         <!-- <form method="GET" action="/remove_player/{{ team }}/{{ player }}"> -->
#           <form method="DELETE" action="/player/{{ team }}/{{ player }}">
#           <input type="submit" value="Remove">
#         </form>
#       </li>
#     {% endfor %}
#   {% endfor %}
# </ul>
# </body>




# <!-- <h3>Teams and Players:</h3>
#   <ul id="teamsAndPlayersContainer">
#     {% for team, players in team_data.items() %}
#       <li>Team {{ team }}:
#         <ul>
#           {% for player in players %}
#             <li>{{ player }}</li>
#           {% endfor %}
#         </ul>
#       </li>
#     {% endfor %}
#   </ul> -->




# <!-- teams and players display for user -->
# <div class="w3-container">
#   <h3>Teams and Players:</h3>
#   <div id="teamsAndPlayersContainer" class="w3-container w3-center">
#     {% for team_num, players in team_data.items() %}
#     <p>Team {{ team_num }} :</p>
#     <ul class="w3-ul">
#       {% for player in players %}
#       <li class="w3-li w3-hover-border">{{ player }}</li>
#       {% endfor %}
#     </ul>
#     {% endfor %}
#   </div>
# </div>

  


# <div class="w3-container w3-center">
#   <h3>Current Players:</h3>
  
#   {% for team, players in team_data.items() %}
#     {% for player in players %}
#     <div class="w3-row">
#       <div class="w3-col m8">
#         {{ player }}
#       </div>
#       <div class="w3-col m4">
#         <form onsubmit="deletePlayer('{{ team }}', '{{ player }}'); return false;">
#           <input type="submit" value="Remove" class="w3-button w3-red">
#         </form>
#       </div>
#     </div>
#     {% endfor %}
#   {% endfor %}
# </div>




# @app.route('/player-score', methods=['POST'])
# def player_score():
#     team_data = session.get('team_data')
#     players = [player for players in team_data.values() for player in players]

#     player_generator.players = players
#     current_player = next(player_generator)

#     scoring = {current_player: {'passes': 0, 'correct_answers': 0} for current_player in player_generator}

#     return jsonify(scoring)

# @app.route('/player-score', methods=['POST'])
# def player_score():
#     current_player = request.json.get('current_player')  # Get the current player from the request

#     # Initialize the scoring dictionary if it's not already created
#     if 'scoring' not in session:
#         session['scoring'] = {}

#     scoring = session['scoring']

#     # Check if the player exists in the scoring dictionary; if not, initialize their score
#     if current_player not in scoring:
#         scoring[current_player] = {'passes': 0, 'correct_answers': 0}

#     return jsonify(scoring[current_player])










# Here is the content for my first column: 

# Scoreboard:

# <!-- Scoring/Player data UI -->
# <h1> Scoreboard </h1>

# <table>
#   <thead>
#     <tr>
#       <th>Player</th>
#       <th>Passes</th>
#       <th>Corrects</th>
#     </tr>
#   </thead>
#   <tbody id="scoreTableBody">
#     <!-- Player scores will be dynamically added here -->
#   </tbody>
# </table>
# </div>

# Start Game button:

# <!-- start countdown to game start. Initiate timer based on game settings variable. TIMER BUTTON -->
# <button onclick="startInitialCountdown()">Click to start game!</button>

# Next players turn button:


# <!-- Next Turn Button. Working to cycle players. Disabled when all players cycled.  -->
# <button id="nextPlayerButton">Next Player's Turn</button>

# Current players score tracker:

#   <p> Score Tracker for this turn </p>
#   <span id="correctScore">Correct: 0</span>
#   <div id="passScore"> Passes: 0 </div>
#   <br>

# Current and next player:

# <!-- HTML to display the current players -->
# <div id="currentPlayer">Current Player: Your name will appear here when it is your turn  </div>
# <div id="nextPlayer">Next Player: Your name will appear here when it is your turn next </div>
# <div id="lastTurnMessage"> </div>
# <br>