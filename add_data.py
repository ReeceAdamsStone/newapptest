from app import app, db
from models import KeyWordCategory, KeyCharacterCategory, ExamSkillsCategory, GrammarRulesCategory, SpellingsCategory
from flask_sqlalchemy import SQLAlchemy

key_word_data = [    "Adjective",
    "Adverbs",
    "Allusion",
    "Antagonist",
    "Characterisation",
    "Connotation",
    "Dialogue",
    "Dramatic Irony",
    "Ellipsis",
    "Figurative Language",
    "Foreshadowing",
    "Genre",
    "Homophones",
    "Imagery",
    "Narrator",
    "Noun",
    "Pronoun",
    "Protagonist",
    "Rhetoric",
    "Symbolism",
    "Theme"
]


key_character_data = [    "Macbeth",
    "Lady Macbeth",
    "Duncan",
    "Banquo",
    "Macduff",
    "Lady Macduff",
    "Witches (Weird Sisters)",
    "King Duncan's Sons",
    "Fleance",
    "Hecate",
    "Lennox",
    "Ross",
    "Angus",
    "Siward",
    "Young Siward",
    "Seyton",
    "Old Major",
    "Napoleon",
    "Snowball",
    "Squealer",
    "Boxer",
    "Mollie",
    "Benjamin",
    "Clover",
    "Muriel",
    "Mr. Jones",
    "Mr. Pilkington",
    "Mr. Frederick",
    "Moses the Raven",
    "Ebenezer Scrooge",
    "Bob Cratchit",
    "Tiny Tim",
    "Jacob Marley",
    "Ghost of Christmas Past",
    "Ghost of Christmas Present",
    "Ghost of Christmas Yet to Come (or Future)",
    "Fred",
    "Belle",
    "Fezziwig",
    "Mrs. Cratchit",
    "Martha Cratchit"]


exam_skills_data = ["Analyse",
    "Assess",
    "Compare",
    "Contrast",
    "Describe",
    "Discuss",
    "Evaluate",
    "Examine",
    "Explain",
    "Identify",
    "Illustrate",
    "Interpret",
    "Justify",
    "Outline",
    "Prove",
    "Relate",
    "State",
    "Summarise"]




grammar_rules_data = [
    "Nouns",
    "Verbs",
    "Adjectives",
    "Adverbs",
    "Plurals",
    "Possessives",
    "Pronouns",
    "Capital Letters",
    "Full Stops",
    "Question Marks",
    "Exclamation Marks",
    "Sentences",
    "Phrases",
    "Contractions",
    "Apostrophes",
    "Homophones",
    "Proper Nouns"
]



spellings_data = [
    "accommodate",
    "apparent",
    "approximately",
    "committee",
    "conscious",
    "definitely",
    "embarrass",
    "existence",
    "harass",
    "immediately",
    "independent",
    "necessary",
    "occurred",
    "precede",
    "recommend",
    "separate",
    "successful",
    "thorough",
    "weird"
]



def populate_db():
        for key_word in key_word_data:
            key_word_instance = KeyWordCategory(key_word=key_word)
            db.session.add(key_word_instance)

        for key_character in key_character_data:
            key_character_instance = KeyCharacterCategory(key_character=key_character)
            db.session.add(key_character_instance)

        for exam_skill in exam_skills_data:
            exam_skill_instance = ExamSkillsCategory(exam_skill=exam_skill)
            db.session.add(exam_skill_instance)

        for grammar_rule in grammar_rules_data:
            grammar_rule_instance = GrammarRulesCategory(grammar_rule=grammar_rule)
            db.session.add(grammar_rule_instance)

        for spelling in spellings_data:
            spelling_instance = SpellingsCategory(spellings=spelling)
            db.session.add(spelling_instance)
        
        db.session.commit()


with app.app_context():
    populate_db()