'''
A game class that stores the game database, the players in the game, and the teams in the game.
'''
__author__ = "Park"

from player import Player

TEAM_LIST = ["_team_one", "_team_two"]

class Game:
    def __init__(self, game_db):
        self.game_db = game_db
        self.players = None
        self.team1 = None
        self.team2 = None

    def set_players(self):
        team_dict = {}
        index = 0
        for team in TEAM_LIST:
            team_dict[team] = {}
            team_dict[team]["name"] = self.game_db[team]["_name"]
            team_dict[team]["players"] = {}
            player_list = self.game_db[team]["_players"]
            for i in range(len(player_list)):
                player = Player(player_list[i]["_name"], self.game_db, i, team)
                team_dict[team]["players"][i] = player.name
        self.players = team_dict

    