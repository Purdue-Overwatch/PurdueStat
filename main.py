# Main class
__author__ = 'Park'

import os
import pymongo
from player import Player

address = os.getenv('PURDUESTAT_MONGO_ADDRESS')
client = pymongo.MongoClient(address)
db = client['game_server']
collection = db['games']
game_db = collection.find_one({'_id': 'dbecea12163e'}) # take in id

if __name__ == '__main__':
    pass


# Snippets
# =====================================================================================================================
# mode setter
'''
if self.map in ['Busan', 'Ilios', 'Lijiang Tower', 'Nepal', 'Oasis']:
    self.mode = 'Control'
elif self.map in ['Dorado', 'Havana', 'Junkertown', 'Rialto', 'Route 66', 'Watchpoint Gibraltar']:
    self.mode = 'Escort'
elif self.map in ['Blizzard World', 'Eichenwalde', 'Hollywood', 'King's Row', 'Numbani']:
    self.mode = 'Hybrid'
else:
    self.mode = 'Error. Unknown map.'
'''
# =====================================================================================================================