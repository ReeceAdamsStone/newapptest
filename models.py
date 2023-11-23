from flask_sqlalchemy import SQLAlchemy
from app import db

# db = SQLAlchemy()

class KeyWordCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key_word = db.Column(db.String(20), unique=True, nullable=False)

class KeyCharacterCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key_character = db.Column(db.String(20), unique=True, nullable=False)

class ExamSkillsCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exam_skill = db.Column(db.String(50), unique=True, nullable=False)

class GrammarRulesCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grammar_rule = db.Column(db.String(50), unique=True, nullable=False)

class SpellingsCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spellings = db.Column(db.String(20), unique=True, nullable=False)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword_category_id = db.Column(db.Integer, db.ForeignKey('key_word_category.id'), nullable=False)
    key_word_category = db.relationship('KeyWordCategory', backref='cards')

    key_character_category_id = db.Column(db.Integer, db.ForeignKey('key_character_category.id'), nullable=False)
    key_character_category = db.relationship('KeyCharacterCategory', backref='cards')

    exam_skills_category_id = db.Column(db.Integer, db.ForeignKey('exam_skills_category.id'), nullable=False)
    exam_skills_category = db.relationship('ExamSkillsCategory', backref='cards')

    grammar_rules_category_id = db.Column(db.Integer, db.ForeignKey('grammar_rules_category.id'), nullable=False)
    grammar_rules_category = db.relationship('GrammarRulesCategory', backref='cards')

    spellings_category_id = db.Column(db.Integer, db.ForeignKey('spellings_category.id'), nullable=False)
    spellings_category = db.relationship('SpellingsCategory', backref='cards')
