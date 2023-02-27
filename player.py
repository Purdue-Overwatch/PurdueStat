"""This module contains the Player class, which is used to store the data of a
player."""
__author__ = "Park"
# look into using numpy arrays over lists if speed is an issue

import decimal
import json

decimal.getcontext().prec = 2

TANK_HEROES = [
    "Reinhardt",
    "Winston",
    "Orisa",
    "Wrecking Ball",
    "Roadhog",
    "Zarya",
    "Sigma",
    "D.Va",
]

DAMAGE_HEROES = [
    "Echo",
    "Pharah",
    "Doomfist",
    "Junkrat",
    "Mei",
    "Sombra",
    "Torbjorn",
    "Genji",
    "Hanzo",
    "Symmetra",
    "Reaper",
    "Soldier: 76",
    "Tracer",
    "Bastion",
    "Ashe",
    "Cassidy",
    "Widowmaker",
]

SUPPORT_HEROES = [
    "L\u00c3\u00bacio",
    "Brigitte",
    "Mercy",
    "Moira",
    "Zenyatta",
    "Baptiste",
    "Ana",
]


class Player:
    """A player class that calculates a player's various statistics.

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
    stats_per_minute : dict
        the stats of the player per minute
    ult_timings : list
        the times the player earns and uses their ultimate

    Methods
    -------
    set_heroes_played()
        Sets the heroes the player played.
    set_role()
        Sets the role of the player based on the heroes they played.
    set_ult_time_stats()
        Sets the time related stats of the player's ultimates.
    set_final_stats()
        Sets the final stats of the player.
    set_stats_per_minute()
        Sets the stats of the player per minute.
    set_ult_timings()
        Sets the times the player earns and uses their ultimate.
    set_all()
        Sets all the attributes of the player.
    """

    def __init__(self, game_db: dict, index: int, team: str):
        self.game_db = game_db
        self.index = index
        self.team = team
        self.data = game_db[team]["_players"][index]
        self.name = self.data["_name"]
        self.heroes_played = []
        self.role = None
        self.avg_time_to_ult = None
        self.avg_time_ult_held = None
        self.final_stats = None
        self.stats_per_minute = {}
        self.ult_timings = None

    def set_heroes_played(self):
        """Sets the heroes the player played."""
        heroes = set(self.data["_heroes"])
        self.heroes_played = list(heroes)

    def set_role(self):
        """Sets the role of the player based on the heroes they played."""
        hero = self.heroes_played[0]

        if hero in TANK_HEROES:
            self.role = "Tank"
        elif hero in DAMAGE_HEROES:
            self.role = "DPS"
        elif hero in SUPPORT_HEROES:
            self.role = "Support"

    def set_ult_time_stats(self):
        """Sets the time related stats of the player's ultimates."""
        ult_charge_arr = self.data["_ultimate_charge"]
        time_stamp_arr = self.game_db["_time_stamps"]

        ult_timings = []
        held_ult_arr = []
        to_ult_arr = []
        prev_charge = 0
        round_start = 0
        prev_time = 0
        start_time = 0
        earn_time = 0

        round_index = -1  # offset by 1 to account for first round

        for charge, time in zip(ult_charge_arr, time_stamp_arr):
            round_starting = time - prev_time > 3
            ult_earned = prev_charge != 100 and charge == 100
            ult_used = prev_charge == 100 and charge == 0

            if round_starting:
                round_index += 1
                ult_timings.append([])
                ult_timings[round_index] = []
                round_start = time
                start_time = time
            elif ult_earned:
                earn_time = time
                time_to_ult = time - start_time
                to_ult_arr.append(time_to_ult)
            elif ult_used:
                start_time = time
                time_ult_held = time - earn_time
                ult_timings[round_index].append(
                    [
                        int(decimal.Decimal(earn_time - round_start)),
                        int(decimal.Decimal(time - round_start)),
                    ]
                )
                held_ult_arr.append(time_ult_held)

            prev_charge = charge
            prev_time = time

        avg_time_to_ult = round(
            sum(to_ult_arr) / len(to_ult_arr), 2
        )  # FIXME: time part is wrong
        avg_time_ult_held = round(
            sum(held_ult_arr) / len(held_ult_arr), 2
        )  # FIXME: time part is wrong

        self.avg_time_to_ult = float(decimal.Decimal(avg_time_to_ult))
        self.avg_time_ult_held = float(decimal.Decimal(avg_time_ult_held))
        self.ult_timings = ult_timings

    def set_in_game_stats(self):
        """Sets the in-game related stats of the player.

        Final stats are set by accessing the final index of each array.
        Stats per min are set by dividing the final stat by the game
        length in seconds and multiplying by 60.
        """
        hero_dmg = self.data["_hero_damage"][-1]
        barrier_dmg = self.data["_barrier_damage"][-1]
        final_stats = {
            "all_damage_dealt": hero_dmg + barrier_dmg,
            "barrier_damage_dealt": barrier_dmg,
            "hero_damage_dealt": hero_dmg,
            "damage_blocked": self.data["_blocked_damage"][-1],
            "damage_taken": self.data["_taken_damage"][-1],
            "deaths": self.data["_deaths"][-1],
            "eliminations": self.data["_eliminations"][-1],
            "environmental_deaths": self.data["_environmental_deaths"][-1],
            "environmental_kills": self.data["_environmental_kills"][-1],
            "final_blows": self.data["_final_blows"][-1],
            "healing_dealt": self.data["_healing_dealt"][-1],
            "healing_received": self.data["_healing_received"][-1],
            "objective_kills": self.data["_object_kills"][-1],
            "solo_kills": self.data["_solo_kills"][-1],
            "ultimates_earned": self.data["_ultimates_earned"][-1],
            "ultimates_used": self.data["_ultimates_used"][-1],
        }

        time_stamps = self.game_db["_time_stamps"]
        game_length = 0
        prev_time = 0
        start_time = time_stamps[0]
        for time in time_stamps:
            if time - prev_time > 5:  # if new round
                game_length += time - start_time  # add round length
                start_time = time
            prev_time = time
        game_length += prev_time - start_time  # add last round

        stats_per_minute = {}
        for key, val in final_stats.items():
            stats_per_minute[key] = float(
                decimal.Decimal(round(val / game_length * 60, 2))
            )

        self.final_stats = final_stats
        self.stats_per_minute = stats_per_minute

    def set_all(self):
        """Sets all the player's stats."""
        self.set_heroes_played()  # heroes_played
        self.set_role()  # role
        self.set_ult_time_stats()  # avg_time_to_ult, avg_time_ult_held, ult_timings
        self.set_in_game_stats()  # final_stats, stats_per_minute

    def print_all_attributes(self):
        """Prints all the player's attributes."""
        print(f"name = {self.name}")
        print(f"heroes_played = {self.heroes_played}")
        print(f"role = {self.role}")
        print(f"avg_time_to_ult = {self.avg_time_to_ult}")
        print(f"avg_time_ult_held = {self.avg_time_ult_held}")
        print(f"ult_timings = {self.ult_timings}")
        print(f"final_stats = {json.dumps(self.final_stats, indent=2)}")
        print(f"stats_per_minute = {json.dumps(self.stats_per_minute, indent=2)}")

    def print_ticks(self):
        """Prints the number of ticks in the game."""
        for charge, (tick, time) in zip(
            self.data["_ultimate_charge"], enumerate(self.game_db["_time_stamps"])
        ):
            print(f"tick {tick}: {time}, {charge}")
