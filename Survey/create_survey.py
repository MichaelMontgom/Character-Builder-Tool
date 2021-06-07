from Character.create_character_engine import create_questions
from models import Survey
from utilities import clear_console


def create_survey_engine():
    clear_console()
    survey = Survey(None, None)

    survey.name = input(f'What do you want this survey to be called?')

    survey.questions = create_questions()

    return survey
