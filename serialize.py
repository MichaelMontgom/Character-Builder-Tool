import pickle
from models import Player, Survey
from os.path import exists
from tkinter import filedialog, Tk


def save_player(player):
    """This method will save the player to disk"""
    try:

        if not exists('./character.pkl'):
            with open('character.pkl', 'wb') as f:
                pickle.dump([Player('John Doe', [])], f, pickle.HIGHEST_PROTOCOL)

        print(player.__dict__)
        print(player.questions[0].body)

        data = load_players()

        data.append(player)

        with open(f'character.pkl', 'wb') as f:
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
    except Exception as e:
        print(e)
        print(f'Something went wrong saving the character')


def load_players():
    with open(f'character.pkl', 'rb') as f:
        data = pickle.load(f)

    return data


def save_survey(survey):
    """This method will save the player to disk"""
    try:

        if not exists('./survey.pkl'):
            with open('survey.pkl', 'wb') as f:
                pickle.dump([Survey(f'survey 1', [])], f, pickle.HIGHEST_PROTOCOL)

        data = load_survey()

        data.append(survey)

        with open(f'survey.pkl', 'wb') as f:
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
    except Exception as e:
        print(e)
        print(f'Something went wrong saving the character')


def load_survey():
    with open(f'survey.pkl', 'rb') as f:
        data = pickle.load(f)

    return data


def get_path():
    """Creates dialog to save file"""
    root = Tk()
    root.withdraw()
    path = filedialog.asksaveasfilename(filetypes=(("text files", "*.txt"), ("all files", "*.*")),
                                        defaultextension='.txt')

    return path


def write_to_file(filename, data, name):
    with open(filename, 'w') as f:
        f.write(f'Name: {name}\n\n')
        for i in data:
            f.write(f'\t- {i.reward}\n')
