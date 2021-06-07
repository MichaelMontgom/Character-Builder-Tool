from models import Player, Question, Answer


def create_questions():
    q = Question(None)
    q.answers = []
    a = Answer(None, None)
    questions = []
    while True:
        q.body = input(f'Enter the question: ')

        while True:
            a.body = input(f'Enter the body of the answer: ')
            a.reward = input(f' Enter the reward: ')

            choice_ans = input('Do you want to add another answer? (y/n)').lower()
            if choice_ans == 'n':
                q.answers.append(a)
                break
            else:
                q.answers.append(a)
                a = Answer(None, None)
                continue

        questions.append(q)

        choice_q = input(f'Do you want to add another question? (y/n)').lower()
        if choice_q == 'n':

            break
        else:
            q = Question(None)
            q.answers = []
            a = Answer(None, None)

            continue

    return questions


def create_engine():
    player = Player(None, None)

    player.name = input(f'What is the name of the character?\n')

    player.questions = create_questions()

    # print(*player.questions, sep=', ')
    # print(*player.questions[0].answers, sep=', ')

    return player
