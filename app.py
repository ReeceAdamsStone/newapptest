from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{app.root_path}/cards.sqlite"
app.config['CORS_METHODS'] = ['GET', 'POST', 'PUT', 'DELETE']


db = SQLAlchemy()    

db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

import models
import routes

with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run()





