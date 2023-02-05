'''
A game class that stores the game database, the players in the game, and the teams in the game.
'''
__author__ = 'Park'

from player import Player

TEAM_LIST = ['_team_one', '_team_two']

class Map:
    '''
    A map class. Represents one map in a scrim.
    '''
    def __init__(self, game_db):
        self.game_db = game_db
        self.players = None
        self.team1 = None
        self.team2 = None

    def set_players(self):
        '''
        Adds players to teams.
        '''
        team_dict = {}
        for team in TEAM_LIST:
            team_dict[team] = {}
            team_dict[team]['name'] = self.game_db[team]['_name']
            team_dict[team]['players'] = {}
            player_list = self.game_db[team]['_players']
            for (i, j) in player_list:
                player = Player(self.game_db, i, team) # TODO: replace player index with player dictionary and fix player class
                team_dict[team]['players'][i] = player.name
        self.players = team_dict
        print(self.players)
