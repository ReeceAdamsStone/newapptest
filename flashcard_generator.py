from app import db
from models import *
import random

class CardGenerator:
    def __init__(self, db):
        self.db = db
    
    def generate_random_card(self):
        num_keywords = db.session.query(KeyWordCategory).count()
        num_characters = db.session.query(KeyCharacterCategory).count()
        num_skills = db.session.query(ExamSkillsCategory).count()
        num_rules = db.session.query(GrammarRulesCategory).count()
        num_spellings = db.session.query(SpellingsCategory).count()
        
        # Define a function to get a random attribute from a category
        def get_random_attribute(query, num_records):
            used_attributes = set()  # Track used attribute IDs
            while True:
                attribute_id = random.randint(1, num_records)
                if attribute_id not in used_attributes:
                    used_attributes.add(attribute_id)
                    return query.get(attribute_id)
        
        keyword_category = get_random_attribute(db.session.query(KeyWordCategory), num_keywords)
        key_character_category = get_random_attribute(db.session.query(KeyCharacterCategory), num_characters)
        exam_skills_category = get_random_attribute(db.session.query(ExamSkillsCategory), num_skills)
        grammar_rules_category = get_random_attribute(db.session.query(GrammarRulesCategory), num_rules)
        spellings_category = get_random_attribute(db.session.query(SpellingsCategory), num_spellings)

        return Card(
            key_word_category=keyword_category,
            key_character_category=key_character_category,
            exam_skills_category=exam_skills_category,
            grammar_rules_category=grammar_rules_category,
            spellings_category=spellings_category
        )
