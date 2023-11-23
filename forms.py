
from flask_wtf import FlaskForm
from wtforms import RadioField, SelectField, IntegerField, SubmitField, validators, StringField, FieldList
from flask import session

class GameSetupForm(FlaskForm):
    game_mode = SelectField('Game Mode:', choices=[('Full', 'Full Game'), ('Selected', 'Select Rounds'), ('Custom', 'Custom')], default='Full')
    num_teams = SelectField('Number of Teams:', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1')
    time_limit = IntegerField('Time Limit (seconds)', [validators.InputRequired(), validators.NumberRange(min=1, max=45, message='The time limit should be 45 seconds or less')], default=30)
    game_type = SelectField('Game Type', choices=[('multi-round', 'Multi-round'), ('single-category', 'Single category')], default='multi-round')
    num_rounds = IntegerField('Number of Rounds (if multi-round):', render_kw={'min': '1'}, default=1)
    category = SelectField('Select Category (for single category game):', choices=[('Key Subject Terms', 'Key Subject Terms'), ('Key Characters', 'Key Characters'), ('Exam Skills and Command Words', 'Exam Skills and Command Words'), ('Spellings', 'Spellings'), ('Grammar Rules and Concepts', 'Grammar Rules and Concepts'),], default='Key Subject Terms')
    team_names = SubmitField('Enter Player Data')


# #original

class PlayerDataForm(FlaskForm):
    # team_names = FieldList(StringField('Team Name', [validators.DataRequired()], choices=[], min_entries=1))
    player_names = FieldList(StringField('Player Name', [validators.DataRequired()]), min_entries=1, max_entries=4)
    jointeam1 = SubmitField('Join Team 1')
    jointeam2 = SubmitField('Join Team 2')
    jointeam3 = SubmitField('Join Team 3')
    start_game = SubmitField('Start Game')

