# Main class
__author__ = "Park"
__version__ = "08/02/2022"

import os
import pymongo
from player import Player

address = os.getenv('PURDUESTAT_MONGO_ADDRESS')
client = pymongo.MongoClient(address)
db = client["game_server"]
collection = db["games"]
game_db = collection.find_one({"_id": "dbecea12163e"}) # take in id

def create_teams():
        teams_dict = {"team 1": 
                        {"name": game_db["_team_one"]["_name"], 
                        "players": {0: None,
                                    1: None,
                                    2: None,
                                    3: None,
                                    4: None,
                                    5: None,}}, 
                    "team 2": 
                        {"name": game_db["_team_two"]["_name"], 
                        "players": {0: None,
                                    1: None,
                                    2: None,
                                    3: None,
                                    4: None,
                                    5: None,}}}

        teams = ["_team_one", "_team_two"]
        for team in teams:
            player_list = game_db[team]["_players"]
            for i in range(len(player_list)):
                player = Player(player_list[i]["_name"], game_db, i, team)
                if team == "_team_one":
                    teams_dict["team 1"]["players"][i] = player.name
                else: 
                    teams_dict["team 2"]["players"][i] = player.name
        return teams_dict

if __name__ == "__main__":
    teams = create_teams()
    print(teams)

# Snippets
# =====================================================================================================================
# mode setter
"""
if self.map in ["Busan", "Ilios", "Lijiang Tower", "Nepal", "Oasis"]:
    self.mode = "Control"
#2CP disappearing in ow2
elif self.map in ["Hanamura", "Horizon Lunar Colony", "Paris", "Temple of Anubis", "Volskaya Industries"]:
    self.mode = "Assault"
elif self.map in ["Dorado", "Havana", "Junkertown", "Rialto", "Route 66", "Watchpoint Gibraltar"]:
    self.mode = "Escort"
elif self.map in ["Blizzard World", "Eichenwalde", "Hollywood", "King's Row", "Numbani"]:
    self.mode = "Hybrid"
else:
    self.mode = "Error. Unknown map."
"""
# =====================================================================================================================