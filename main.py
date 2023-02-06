# Main class
__author__ = "Park"

import os
import pymongo
from player import Player
from map import Map

address = os.getenv("PURDUESTAT_MONGO_ADDRESS")
client = pymongo.MongoClient(address)
db = client["game_server"]
collection = db["games"]
GAME_DB = collection.find_one({"_id": "a1a809890993"})  # take in id(s)

DB_TEAMS = ["_team_one", "_team_two"]
DB_PLAYERS = "_players"

if __name__ == "__main__":
    map = Map(GAME_DB)
    map.set_players()
