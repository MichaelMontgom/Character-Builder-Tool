from utilities import *
from Character.play_engine import play_engine
from Character.create_character_engine import create_engine
from Survey.create_survey import create_survey_engine
from Survey.play_survey import play_survey_engine
from serialize import *
from edit import edit_engine

if __name__ == '__main__':

    while True:

        print(f'Hello, welcome to the character creation tool!')

        while True:
            try:
                choice = int(
                    input(f'1. Create Character\n2. Play Character\n3. Create Survey\n4. Play Survey\n5. Edit\n'))
                if choice not in range(1, 6):
                    raise WrongValueError

            except ValueError:
                print(f'That was not an integer!')
                continue
            except WrongValueError:
                print(f'That was not an option, please try again')
                continue
            else:
                break

        if choice == 1:
            player = create_engine()
            save_player(player)

        elif choice == 2:
            play_engine()
        elif choice == 3:
            survey = create_survey_engine()
            save_survey(survey)
        elif choice == 4:
            play_survey_engine()
        else:
            edit_engine()
