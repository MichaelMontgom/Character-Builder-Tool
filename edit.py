from serialize import *
import os
from utilities import WrongValueError, clear_console


def edit_character():
    characters = load_players()
    num = 1
    print(f'Please choose a character to edit:')
    for i in characters[1:]:
        print(f'{num}. {i.name}')
        num = num + 1

    while True:
        try:
            choice = int(input())
            if choice > (len(characters) - 1) or choice <= 0:
                raise WrongValueError

        except ValueError:
            print(f'That was not a number!')
            continue
        except WrongValueError:
            print(f'That was not an option, please try again')
            continue
        else:
            break

    clear_console()

    character = characters[choice]
    questions = character.questions

    while True:
        incrementer = 0
        incrementer2 = 1
        inc = 1
        for i in questions:
            print(f'Q{incrementer + 1}: {questions[incrementer].body}')
            for j in i.answers:
                print(f'{inc}. {j.body} ---> {j.reward}')
                inc = inc + 1
            incrementer = incrementer + 1
            print()
            print('-' * 40)
            print()
        while True:
            try:
                choice_question = int(input(f'Please choose a question you would like to edit'))
                if choice not in range(1, len(questions)):
                    raise WrongValueError

            except WrongValueError:
                print(f'That was not an option, please try again')
                continue
            except ValueError:
                print(f'That was not an integer')
                continue
            else:
                break

        clear_console()
        inc = 1
        print(f'{questions[choice_question - 1].body}')
        for i in questions[choice_question - 1].answers:
            print(f'{inc}. {i.body} ---> {i.reward}')

        while True:
            try:
                choice_edit = str(input(f'Would you like to edit the question or answers? (q/a)').lower())
                if choice_edit not in ('a', 'q'):
                    raise WrongValueError

            except WrongValueError:
                print(f'That was not an option, please try again')
                continue
            except ValueError:
                print(f'That was not an string, try again')
                continue
            else:
                break

        if choice_edit == 'a':
            print(f'pressed a')
        else:
            print(f'pressed q')

        #TODO: Setup editing for a specific question and answer


def edit_survey():
    print()


def edit_engine():
    clear_console()
    while True:
        try:
            choice = int(input(f'What would you like to edit?\n1. Character\n2. Survey\n'))
            if choice not in (1, 2):
                raise WrongValueError
        except ValueError:
            print(f'That was not an integer!')
            continue
        except WrongValueError:
            print(f'That was not an option')
            continue
        except Exception as e:
            print(e)
        else:
            break

    if choice == 1:
        edit_character()
    else:
        edit_survey()
