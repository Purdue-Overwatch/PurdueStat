__author__ = 'Park'

TANK_HEROES = ['Reinhardt', 'Winston', 'Orisa', 'Wrecking Ball', 'Roadhog', 'Zarya', 'Sigma', 'D.Va']
DAMAGE_HEROES = ['Echo', 'Pharah', 'Doomfist', 'Junkrat', 'Mei', 'Sombra', 'Torbjorn', 'Genji', 'Hanzo', 'Symmetra', 'Reaper', 'Soldier: 76', 'Tracer', 'Bastion', 'Ashe', 'Cassidy', 'Widowmaker']
SUPPORT_HEROES = ['L\u00c3\u00bacio', 'Brigitte', 'Mercy', 'Moira', 'Zenyatta', 'Baptiste', 'Ana']

class Player:
    '''
    A Player class that takes the name of the player, the game database, 
    the index of the player in the game database, and the team the player is on as input
    and calculates the rest of the data.
    '''
    def __init__(self, name: str, game_db: dict, index: int, team: str):
        self.name = name
        self.game_db = game_db
        self.index = index
        self.team = team
        self.data = game_db[team]['_players'][index]
        self.heroes_played = self.set_heroes()
        self.role = None
        self.avg_time_to_ult = None
        self.avg_time_ult_held = None
        self.final_stats = None
        self.stats_per_ten = None
        self.ult_timings = None

    def set_heroes(self):
        '''
        Sets the heroes the player played.
        '''
        game_length = len(self.game_db['_time_stamps'])
        heroes = set()
        for tick in range(game_length):
            hero = self.game_db[self.team]['_players'][self.index]['_heroes'][tick]
            heroes.add(hero)

        return heroes

    def set_role(self):
        '''
        Sets the role of the player based on the heroes they played.
        '''
        heroes = self.heroes_played
        if heroes in TANK_HEROES:
            return 'Tank'
        if heroes in DAMAGE_HEROES:
            return 'DPS'
        if heroes in SUPPORT_HEROES:
            return 'Support'

    def set_avg_time_to_ult(self):
        '''
        Sets the average time it takes for the player to get their ultimate.
        '''
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
        '''
        Sets the average time the player holds their ultimate.
        '''
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
        self.set_avg_time_ult_held = round(avg_time, 2)

    def set_final_stats(self):
        '''
        Sets the final stats of the player by accessing the final index of each array.
        '''
        hero_dmg = self.data['_hero_damage'][-1]
        barrier_dmg = self.data['_barrier_damage'][-1]
        final_stats = {
            "barrier_damage_dealt": barrier_dmg, 
            "all_damage_dealt": hero_dmg + barrier_dmg,
            "hero_damage_dealt": hero_dmg,
            "damage_blocked": self.data['_blocked_damage'][-1],
            "damage_taken": self.data['_taken_damage'][-1],
            "deaths": self.data['_deaths'][-1],
            "eliminations": self.data['_eliminations'][-1],
            "environmental_deaths": self.data['_environmental_deaths'][-1],
            "environmental_kills": self.data['_environmental_kills'][-1],
            "final_blows": self.data['_final_blows'][-1],
            "healing_dealt": self.data['_healing_dealt'][-1],
            "healing_received": self.data['_healing_received'][-1],
            "objective_kills": self.data['_objective_kills'][-1],
            "solo_kills": self.data['_solo_kills'][-1],
            "ultimates_earned": self.data['_ultimates_earned'][-1],
            "ultimates_used": self.data['_ultimates_used'][-1],
        }
        self.final_stats = final_stats

    def set_stats_per_ten(self):
        '''
        Sets the stats of the player per 10 minutes.
        '''
        hero_dmg = None
        barrier_dmg = None
        stats_per_ten = {
            "barrier_damage_dealt": None,
            "hero_damage_dealt": None,
            "all_damage_dealt": None,
            "damage_blocked": None,
            "damage_taken": None,
            "deaths": None,
            "eliminations": None,
            "environmental_deaths": None,
            "environmental_kills": None,
            "final_blows": None,
            "healing_dealt": None,
            "healing_received": None,
            "objective_kills": None,
            "solo_kills": None,
            "ultimates_earned": None,
            "ultimates_used": None,
        }
        self.stats_per_ten = stats_per_ten

    def set_ult_timings(self):
        '''
        Sets the timings of the player's ultimates.
        '''
        ult_charge_arr = self.data['_ultimate_charge']
        time_stamps = self.game_db['_time_stamps']
        ult_timings = []
        prev_charge = None
        start_time = None

        for charge, time in ult_charge_arr, time_stamps:
            if prev_charge != 100 and charge == 100:
                start_time = time
            if prev_charge == 100 and charge == 0:
                time_ult_held = time - start_time
                ult_timings.append(time_ult_held)
        
        self.ult_timings = ult_timings

