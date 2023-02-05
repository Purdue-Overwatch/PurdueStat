# Main class
__author__ = 'Park'

import os
import pymongo
from player import Player
# from map import Map

address = os.getenv('PURDUESTAT_MONGO_ADDRESS')
client = pymongo.MongoClient(address)
db = client['game_server']
collection = db['games']
GAME_DB = collection.find_one({'_id': '7e08c64b7c38'}) # take in id(s)

DB_TEAMS = ['_team_one', '_team_two']
DB_PLAYERS = '_players'

if __name__ == '__main__':
    for team in DB_TEAMS:
        for (index, player_json) in enumerate(GAME_DB[team][DB_PLAYERS]):
            player = Player(GAME_DB, index, team)

            player.set_all()
            player.print_all_attributes()
            print()

    # map = Map(GAME_DB)
    # map.set_players()



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
