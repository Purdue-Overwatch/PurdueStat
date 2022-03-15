import json
from test import *

# opens a test .json file and writes the contents to that file
# only works if your folder is named PurdueStat for now
def writeJson(contents):
    f = open("PurdueStat/demofile.json", "w")
    f.write(contents)
    f.close()
    return

# all of these definitions output test data and need to be filled in later
def getMapName():
    return "Oasis"

def getMapScore():
    return [0,0]

def getMapType():
    return "Control"

def getName():
    return "Golex"

def getRole():
    return "main_tank"

def getTimeToUlt():
    return 88.375

def getTimeUltHeld():
    return 19.857

def getFinalStats():
    return {
        "all_damage_dealt": finalstatDfunc["getAllDamageDealt"],
        "barrier_damage_dealt": finalstatDfunc["getBarrierDamage"],
        "cooldown1": finalstatDfunc["getCooldown1"],
        "cooldown2": finalstatDfunc["getCooldown2"],
        "damage_blocked": finalstatDfunc["getDamageBlocked"],
        "damage_taken": finalstatDfunc["getDamageTaken"],
        "deaths": finalstatDfunc["getDeaths"],
        "eliminations": finalstatDfunc["getEliminations"],
        "environmental_deaths": finalstatDfunc["getEnviroDeaths"],
        "environmental_kills": finalstatDfunc["getEnviroKills"],
        "final_blows": finalstatDfunc["getFinalBlows"],
        "healing_dealt": finalstatDfunc["getHealingDealt"],
        "healing_received": finalstatDfunc["getHealingReceived"],
        "hero_damage_dealt": finalstatDfunc["getHeroDamageDealt"],
        "objective_kills": finalstatDfunc["getObjectiveKills"],
        "solo_kills": finalstatDfunc["getSoloKills"],
        "ultimate_charge": finalstatDfunc["getUltimateCharge"],
        "ultimates_earned": finalstatDfunc["getUltimatesEarned"],
        "ultimates_used": finalstatDfunc["getUltimatesUsed"]

    }

# Needs updated, uses finalDfunc not stats per minute
def getStatsPerMinute():
    return {
        "all_damage_dealt": finalstatDfunc["getAllDamageDealt"],
        "barrier_damage_dealt": finalstatDfunc["getBarrierDamage"],
        "cooldown1": finalstatDfunc["getCooldown1"],
        "cooldown2": finalstatDfunc["getCooldown2"],
        "damage_blocked": finalstatDfunc["getDamageBlocked"],
        "damage_taken": finalstatDfunc["getDamageTaken"],
        "deaths": finalstatDfunc["getDeaths"],
        "eliminations": finalstatDfunc["getEliminations"],
        "environmental_deaths": finalstatDfunc["getEnviroDeaths"],
        "environmental_kills": finalstatDfunc["getEnviroKills"],
        "final_blows": finalstatDfunc["getFinalBlows"],
        "healing_dealt": finalstatDfunc["getHealingDealt"],
        "healing_received": finalstatDfunc["getHealingReceived"],
        "hero_damage_dealt": finalstatDfunc["getHeroDamageDealt"],
        "objective_kills": finalstatDfunc["getObjectiveKills"],
        "solo_kills": finalstatDfunc["getSoloKills"],
        "ultimate_charge": finalstatDfunc["getUltimateCharge"],
        "ultimates_earned": finalstatDfunc["getUltimatesEarned"],
        "ultimates_used": finalstatDfunc["getUltimatesUsed"]

    }

def getUltTimings():
    return [[[52,57],[153,154]],[[64,120],[168,169],[294,309]],[[125,160],[234,277],[390,-1]]]

def getHeroesPlayed():
    return {
                "heroes": ["D.Va", "WreckingBall"],
                "D.Va":835,
                "WreckingBall":94
            }

# creates a dictionary of the functions specified above
functionDict = {
    "getMapName": getMapName(),
    "getMapScore": getMapScore(),
    "getMapType": getMapType(),
    "getName": getName(),
    "getRole": getRole(),
    "getTimeToUlt": getTimeToUlt(),
    "getTimeUltHeld": getTimeUltHeld(),
    "getFinalStats": getFinalStats(),
    "getStatsPerMin": getStatsPerMinute(),
    "getUltTimings": getUltTimings(),
    "getHeroesPlayed": getHeroesPlayed()
}

# this line only runs when this script is ran as main
def main(filepath: str) -> int:
    match = []
    # currently loops twice, would need to loop for as many files as we have
    # this loop adds entries into the match list, allowing more than 1 map be to represented
    for i in range(1,3):
        '''    map_name = "Oasis"
        map_score = [0,0]
        map_type = "Control"'''

        # creates the outermoust dictionary that is for each map
        map_dic = {
            "map": functionDict["getMapName"],
            "map_score": functionDict["getMapScore"],
            "map_type": functionDict["getMapType"],
        }

        # this loop creates each entry for the 12 player
        for i in range(1,13):
            player = {
                "name": functionDict["getName"],
                "role": functionDict["getRole"],
                "avg_time_to_ult": functionDict["getTimeToUlt"],
                "avg_time_ult_held": functionDict["getTimeUltHeld"],
                "final_stats": functionDict["getFinalStats"],
                "stats_per_minute": functionDict["getStatsPerMin"],
                "ult_timings": functionDict["getUltTimings"],
                "heroes_played": functionDict["getHeroesPlayed"]
            }
            player_number = "player" + str(i)
            # updates the map dictionary with the current player of the loop
            map_dic[player_number] = player

        # this line adds the map to the match list
        match.append(map_dic)

    # converts match to a json format
    json_match = json.dumps(match, indent=4)
    # the output printed to terminal
    print(json_match)

    # when uncommented this line will update the demofile.json
            # I commeneted it so that if your file structure was different it would not error
    #writeJson((json_match))
    
    # temp main, will explain later how this runs and how we can edit it to fit our needs
if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
