import random


class Player:
    '''
    player.py is on a single team, with many other players
    players play in a game for a team
    '''
    def __init__(self, name, skill):
        self.name = name

        # player.py skill rankings
        self.skill = skill

    def salary(self):
        return 5000 + self.skill * 100

    def __str__(self):
        return '{}, Skill: {}, Salary: {}'.format(self.name, self.skill, self.salary())


def generate_player():
    first_names = [
       'Jackson',
       'Aiden',
       'Lucas',
       'Liam',
       'Noah',
       'Ethan',
       'Mason',
       'Caden',
       'Oliver',
       'Elijah',
       'Grayson',
       'Jacob',
       'Michael',
       'Benjamin',
       'Carter',
       'James',
       'Jayden',
       'Logan',
       'Alexander',
       'Caleb',
       'Ryan',
       'Luke',
       'Daniel',
       'Jack',
       'William',
       'Owen',
       'Gabriel',
       'Matthew',
       'Connor',
       'Jayce',
       'Isaac',
       'Sebastian',
       'Henry',
       'Muhammad',
       'Cameron',
       'Wyatt',
       'Dylan',
       'Nathan',
       'Nicholas',
       'Julian',
    ]
    first_name = random.choice(first_names)
    last_name = random.choice(first_names)
    full_name = '{} {}'.format(first_name, last_name)
    # generate skill and salary
    skill = 10 + random.randint(0, 90)
    return Player(full_name, skill,)