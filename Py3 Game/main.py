import random

from teammanager import TeamManager
from team import League, Team
from player import generate_player


def main():
    #set up our data
    #generate some players
    players = []
    for i in range(100):
        players.append(generate_player())

    #set up 5 teams
    teams = [
        Team('Patriots'),
        Team('Giants'),
        Team('Raiders'),
        Team('Steelers'),
        Team('Seahawks'),
        Team('Cowboys'),

    ]
    for team in teams:
        for player_num in range(11):

            #give them 11 starting players
            selected_player = random.choice(players)
            team.players.append(selected_player)
            players.remove(selected_player)



    #we have a single league
    first_league = League('National Football League', teams, players)


    # create the manager
    manager = TeamManager(random.choice(teams), first_league)


    print('Season begins')
    for i in range(10):
        manager.manage()
        first_league.play_round()
    print('Season ends')





if __name__ == '__main__':
    main()
