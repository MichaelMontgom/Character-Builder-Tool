class Answer:
    def __init__(self, body, reward):
        self.body = body
        self.reward = reward
        self.questions = {}

    def __str__(self):
        return f'Body: {self.body}, Reward: {self.reward}, Questions: {self.questions}'


class Question:
    def __init__(self, body, answers):
        self.body = body
        self.answers = answers

    def __str__(self):
        return f'Body: {self.body}, Answers: {self.answers}'


class Player:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def __str__(self):
        return f'Name: {self.name}, Questions: {self.questions}'


class Survey:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def __str__(self):
        return f'Name: {self.name}, Questions: {self.questions}'
