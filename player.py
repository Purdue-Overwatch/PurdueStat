'''
A Player class that stores the name of the player, the game database, 
the index of the player in the game database, and the team the player is on.
'''
# TODO: add dmg, healing, and elims done by player, and add a function to set the role of the player
__author__ = 'Park'

TANK_HEROES = ['Reinhardt', 'Winston', 'Orisa', 'Wrecking Ball', 'Roadhog', 'Zarya', 'Sigma', 'D.Va']
DAMAGE_HEROES = ['Echo', 'Pharah', 'Doomfist', 'Junkrat', 'Mei', 'Sombra', 'Torbjorn', 'Genji', 'Hanzo', 'Symmetra', 'Reaper', 'Soldier: 76', 'Tracer', 'Bastion', 'Ashe', 'Cassidy', 'Widowmaker']
SUPPORT_HEROES = ['L\u00c3\u00bacio', 'Brigitte', 'Mercy', 'Moira', 'Zenyatta', 'Baptiste', 'Ana']

class Player:
    def __init__(self, name, game_db, index, team):
        self.name = name
        self.game_db = game_db
        self.index = index
        self.team = team
        self.data = game_db[team][index]
        self.heroes_played = None
        self.role = None
        self.avg_time_to_ult = None
        self.avg_time_ult_held = None
        self.final_stats = None
        self.stats_per_minute = None
        self.ult_timings = None
        self.heroes_played = None

    def set_heroes(self):
        team = self.team()
        index = self.index()

        game_length = len(self.game_db['_time_stamps'])
        heroes = set()
        for tick in range(game_length):
            hero = self.game_db[team]['_players'][index]['_heroes'][tick]
            heroes.add(hero)

        self.heroes = heroes

    def set_role(self):
        heroes = self.get_heroes_played()
        if heroes in TANK_HEROES:
            self.role('Tank')
        if heroes in DAMAGE_HEROES:
            self.role('DPS')
        if heroes in SUPPORT_HEROES:
            self.role('Support')

    def set_avg_time_to_ult(self):
        ult_charge_arr = self.data['_ultimate_charge']
        time_stamps = self.game_db['_time_stamps']
        time_arr = []
        prev_charge = None
        start_time = None

        for charge, time in ult_charge_arr, time_stamps:
            if prev_charge != 0 and charge == 0:
                start_time = time
            if prev_charge != 100 and charge == 100:
                time_to_ult = time - start_time
                time_arr.append(time_to_ult)
        
        avg_time = sum(time_arr) / len(time_arr)
        return round(avg_time, 2)

    def set_avg_time_ult_held(self):
        ult_charge_arr = self.data['_ultimate_charge']
        time_stamps = self.game_db['_time_stamps']
        time_arr = []
        prev_charge = None
        start_time = None

        for charge, time in ult_charge_arr, time_stamps:
            if prev_charge != 100 and charge == 100:
                start_time = time
            if prev_charge == 100 and charge == 0:
                time_ult_held = time - start_time
                time_arr.append(time_ult_held)
        
        avg_time = sum(time_arr) / len(time_arr)
        return round(avg_time, 2)
