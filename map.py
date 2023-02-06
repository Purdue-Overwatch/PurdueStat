"""
A game class that stores the game database, the players in the game, and the teams in the game.
"""
__author__ = "Park"

from player import Player

TEAM_LIST = ["_team_one", "_team_two"]


class Map:
    """A map class that represents one map in a scrim.

    The map class stores the game database, the players in the game, and the teams in the game.

    Attributes
    ----------
    game_db : dict
        the game database
    players : dict
        the players in the game
    team1 : dict
        the first team in the game
    team2 : dict
        the second team in the game

    Methods
    -------
    set_players()
        Adds players to teams.

    """

    def __init__(self, game_db):
        self.game_db = game_db
        self.players = None
        self.team1 = None
        self.team2 = None

    def set_players(self):
        """Adds players to teams."""
        team_dict = {}
        for team in TEAM_LIST:
            team_dict[team] = {}
            team_dict[team]["name"] = self.game_db[team]["_name"]
            team_dict[team]["players"] = {}
            for i in range(5):
                player = Player(self.game_db, i, team)
                team_dict[team]["players"][i] = player.name
                player.set_all()
                player.print_all_attributes()

        self.players = team_dict
        print(self.players)


# Snippets
# =======================================================================================================
# mode setter
# if self.map in ['Busan', 'Ilios', 'Lijiang Tower', 'Nepal', 'Oasis']:
#     self.mode = 'Control'
# elif self.map in ['Dorado', 'Havana', 'Junkertown', 'Rialto', 'Route 66', 'Watchpoint Gibraltar']:
#     self.mode = 'Escort'
# elif self.map in ['Blizzard World', 'Eichenwalde', 'Hollywood', 'King's Row', 'Numbani']:
#     self.mode = 'Hybrid'
# else:
#     self.mode = 'Error. Unknown map.'
# =======================================================================================================
