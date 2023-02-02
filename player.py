'''
This module contains the Player class, which is used to store the data of a player.
'''
__author__ = 'Park'

# TODO: look into using numpy arrays instead of lists if speed is an issue

TANK_HEROES = ['Reinhardt', 'Winston', 'Orisa', 'Wrecking Ball', \
    'Roadhog', 'Zarya', 'Sigma', 'D.Va']

DAMAGE_HEROES = ['Echo', 'Pharah', 'Doomfist', 'Junkrat', 'Mei', \
    'Sombra', 'Torbjorn', 'Genji', 'Hanzo', 'Symmetra', 'Reaper', \
    'Soldier: 76', 'Tracer', 'Bastion', 'Ashe', 'Cassidy', 'Widowmaker']

SUPPORT_HEROES = ['L\u00c3\u00bacio', 'Brigitte', 'Mercy', 'Moira', \
    'Zenyatta', 'Baptiste', 'Ana']

class Player:
    """
    A player class that stores the data of a player.

    Attributes
    ----------
    game_db : dict
        the game database
    index : int
        the index of the player in the game database
    team : str
        the team the player is on
    data : dict
        the player's data in the game database
    name : str
        the player's name
    heroes_played : list
        the heroes the player played
    role : str
        the role the player played
    avg_time_to_ult : float
        the average time it takes the player to get their ultimate
    avg_time_ult_held : float
        the average time the player holds their ultimate
    final_stats : dict
        the final stats of the player
    stats_per_ten : dict
        the stats of the player per 10 minutes
    ult_timings : list
        the times the player earns and uses their ultimate
    round_timings : list
        the times the player earns and uses their ultimate

    Methods
    -------
    set_name()
        Sets the name of the player.
    set_heroes()
        Sets the heroes the player played.
    set_role()
        Sets the role of the player based on the heroes they played.
    set_time_stats()
        Sets the timing, time held, and time to stats of the player's ultimates.
    set_final_stats()
        Sets the final stats of the player.
    set_stats_per_ten()
        Sets the stats of the player per 10 minutes.
    set_game_stats()
        Sets the game stats of the player.
    set_all()
        Sets all the attributes of the player.
    """
    def __init__(self, game_db: dict, index: int, team: str):
        self.game_db = game_db
        self.index = index
        self.team = team
        self.data = game_db[team]['_players'][index]
        self.name = None
        self.heroes_played = None
        self.role = None
        self.avg_time_to_ult = None
        self.avg_time_ult_held = None
        self.final_stats = None
        self.stats_per_ten = {}
        self.ult_timings = None

    def set_name(self):
        '''
        Sets the name of the player.
        '''
        self.name = self.data['_name']

    def set_heroes(self):
        '''
        Sets the heroes the player played.
        '''
        game_length = len(self.game_db['_time_stamps'])
        heroes = set()
        for tick in range(game_length):
            hero = self.game_db[self.team]['_players'][self.index]['_heroes'][tick]
            heroes.add(hero)

        self.heroes_played = list(heroes)

    def set_role(self):
        '''
        Sets the role of the player based on the heroes they played.
        '''
        heroes = self.heroes_played
        role = None
        if heroes in TANK_HEROES:
            role = 'Tank'
        elif heroes in DAMAGE_HEROES:
            role = 'DPS'
        elif heroes in SUPPORT_HEROES:
            role = 'Support'
        self.role = role

    def set_time_stats(self):
        '''
        Sets the timing, time held, and time to stats of the player's ultimates.
        '''
        ult_charge_arr = self.data['_ultimate_charge']
        time_stamp_arr = self.game_db['_time_stamps']

        ult_timings = []
        held_ult_arr = []
        to_ult_arr = []
        prev_charge = 0
        prev_time = 0
        round_index = -1 # offset by 1 to account for the first round

        for (charge, time) in zip(ult_charge_arr, time_stamp_arr):
            # the following is designed to prevent unnecessary checks while maintaining readability.
            # i think i could have made it more efficient, but it would be hard to understand.
            round_starting = time - prev_time > 10
            ult_earned = prev_charge != 100 and charge == 100
            ult_used = prev_charge == 100 and charge == 0
            if round_starting: # new round?
                round_index += 1
                ult_timings.append([])
                ult_timings[round_index] = []
                start_time = time
            elif ult_earned: # ult earned?
                earn_time = time
                time_to_ult = time - start_time
                to_ult_arr.append(time_to_ult)
            elif ult_used: # ult used?
                start_time = time
                time_ult_held = time - earn_time
                ult_times = [time_to_ult, time_ult_held]
                ult_timings[round_index].append(ult_times)
                held_ult_arr.append(time_ult_held)

            prev_charge = charge
            prev_time = time

        self.avg_time_to_ult = round(sum(to_ult_arr) / len(to_ult_arr), 2)
        self.avg_time_ult_held = round(sum(held_ult_arr) / len(held_ult_arr), 2)
        self.ult_timings = ult_timings

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
            "objective_kills": self.data['_object_kills'][-1],
            "solo_kills": self.data['_solo_kills'][-1],
            "ultimates_earned": self.data['_ultimates_earned'][-1],
            "ultimates_used": self.data['_ultimates_used'][-1],
        }
        self.final_stats = final_stats

    def set_per_ten_stats(self):
        '''
        Sets the average stats of the player per 10 minutes using the final stats.
        '''

        time_stamps = self.game_db['_time_stamps'] # line 188 to 197 calcultes the game length
        game_length = 0
        prev_time = 0
        start_time = time_stamps[0]
        for time in time_stamps:
            if time - prev_time > 5: #if new round
                game_length += prev_time - start_time #add round length
                start_time = time
            prev_time = time
        game_length = prev_time - start_time #add last round

        for key, val in self.final_stats.items():
            self.stats_per_ten[key] = val / game_length * 6

    def set_all(self):
        '''
        Sets all the player's stats.
        '''
        self.set_heroes()
        self.set_role()
        self.set_time_stats()
        self.set_final_stats()
        self.set_per_ten_stats()
