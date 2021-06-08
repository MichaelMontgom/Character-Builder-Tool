from serialize import *
from utilities import *


def play_survey_engine():
    history = []
    save_choice = ''
    data = load_survey()

    num = 0
    print(f'Please choose a survey below to play:')
    for i in data[1:]:
        print(f'{num + 1}. {i.name}')
        num = num + 1

    while True:
        try:
            choice = int(input())
            # print(len(data))
            if choice > (len(data) - 1) or choice <= 0:
                raise WrongValueError

        except ValueError:
            print(f'That was not a number!')
            continue
        except WrongValueError:
            print(f'That was not an option, please try again')
            continue
        else:
            break

    survey = data[choice]
    questions = survey.questions
    incrementer = 0
    incrementer2 = 1

    while True:
        clear_console()
        print(f'Survey: {survey.name}')
        print(f'Q{incrementer + 1}: {questions[incrementer].body}')

        for i in questions[incrementer].answers:
            print(f'{incrementer2}: {i.body}')
            incrementer2 = incrementer2 + 1
        while True:
            try:

                choice = int(input())

                if (choice - 1) < 0 or (choice - 1) >= len(questions[incrementer].answers):
                    raise WrongValueError

                break

            except ValueError:
                print(f'That was not an integer, please make a valid choice')
            except WrongValueError:
                print(f'That was not a choice, please try again')
            except Exception as e:
                print(e)
        try:
            history.append(questions[incrementer].answers[choice - 1])
        except Exception as e:
            print(e)

        incrementer = incrementer + 1
        incrementer2 = 1

        if (len(questions) - 1) >= incrementer:
            continue
        else:
            break

    clear_console()
    print(f'Here are the rewards you have acquired!')
    print(f'-' * 40)
    for i in history:
        print(f'{i.reward}\n')
    while True:

        try:
            save_choice = str(input(f'would you like to you rewards to a txt file? (y/n)').lower())
            print(save_choice)
            if save_choice != 'y' and save_choice != 'n':
                raise WrongValueError

        except WrongValueError:
            print(f'That was not an option - Wrong Value Error')
            continue
        except ValueError:
            print(f'That was not an option! - Value Error')
        else:
            break
    if save_choice == 'y':
        name = input(f'Please enter a name for the character: ')
        write_to_file(get_path(), history, name)
    else:
        print()
    input('Press any key to go back to the main menu...')
    clear_console()
    return
