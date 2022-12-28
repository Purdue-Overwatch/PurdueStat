'''
A Player class that stores the name of the player, the game database, 
the index of the player in the game database, and the team the player is on.

TODO: add dmg, healing, and elims done by player, and add a function to set the role of the player
'''
__author__ = "Park"
__version__ = "08/02/2022"


TANKS = ["Reinhardt", "Winston", "Orisa", "Wrecking Ball", "Roadhog", "Zarya", "Sigma", "D.Va"]
DPS = ["Echo", "Pharah", "Doomfist", "Junkrat", "Mei", "Sombra", "Torbjorn", "Genji", "Hanzo", "Symmetra", "Reaper", "Soldier: 76", "Tracer", "Bastion", "Ashe", "Cassidy", "Widowmaker"]
SUPPORTS = ["L\u00c3\u00bacio", "Brigitte", "Mercy", "Moira", "Zenyatta", "Baptiste", "Ana"]

class Player:
    def __init__(self, name, game_db, index, team):
        self.name = name
        self.game_db = game_db
        self.index = index
        self.team = team
        self.heroes = None
        self.role = None
    
    def set_role(self):
        heroes = self.get_heroes_played()
        if heroes in TANKS:
            self.role("Tank")
        if heroes in DPS:
            self.role("DPS")
        if heroes in SUPPORTS:
            self.role("Support")

    def set_heroes(self):
        team = self.team()
        index = self.index()

        game_length = len(self.game_db['_time_stamps'])
        heroes = set()
        for tick in range(game_length):
            hero = self.game_db[team]['_players'][index]['_heroes'][tick]
            heroes.add(hero)

        self.heroes = heroes