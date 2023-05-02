"""A game class that stores the game database, the players in the game, and the
teams in the game."""
__author__ = "Park"

import json
import os

import pymongo

from src.player import Player

MONGOCLIENT = pymongo.MongoClient(os.getenv("PURDUESTAT_MONGO_ADDRESS"))
TEAM_LIST = ["team_one", "team_two"]

collection = MONGOCLIENT["game_server"]["games"]


class Map:
    """A map class that represents one map in a scrim.

    The map class stores the game database, the players in the game, and the teams in the game.

    Attributes
    ----------
    map_id : str
        the map id
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

    def __init__(self, map_id: str):
        self.map_id = map_id
        self.game_db = collection.find_one({"_id": map_id})
        self.map_name = self.game_db["_map_name"]
        self.round_start_times = []
        self.players = None
        self.team1 = None
        self.team2 = None

    def find_round_start_times(self):
        """Finds the times when a new round starts."""
        timestamps = self.game_db["_time_stamps"]

        for i in range(1, len(timestamps)):
            if timestamps[i] - timestamps[i - 1] >= 5:
                self.round_start_times.append(timestamps[i])

    def set_players(self) -> dict:
        """Adds players to dict."""
        players = {}
        for team in TEAM_LIST:
            for i in range(5):
                player = Player(self.game_db, i, f"_{team}")
                players[
                    f"player{i + 6 if team == 'team_two' else i + 1}"
                ] = player.output()
                print(f"{team} player {i} set: {player.name}")
        # with open("dev_file.txt", "+w", encoding="utf-8") as file:
        #     file.write(json.dumps(players, indent=4))
        self.players = players

    #    print(self.players)


# Snippets
# =======================================================================================================
# mode setter
# if self.map in ["Busan", "Ilios", "Lijiang Tower", "Nepal", "Oasis"]:
#     self.mode = "Control"
# elif self.map in ["Dorado", "Havana", "Junkertown", "Rialto", "Route 66", "Watchpoint Gibraltar"]:
#     self.mode = "Escort"
# elif self.map in ["Blizzard World", "Eichenwalde", "Hollywood", "King's Row", "Numbani"]:
#     self.mode = "Hybrid"
# else:
#     self.mode = "Error. Unknown map."
# =======================================================================================================
