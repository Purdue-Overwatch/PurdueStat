'''
Defines getter functions and organizes them into dictionaries to be imported into other files. 

Defines utility function readLogFile for reading in an Overwatch log file and seperating it into an event file, a CSV file, and an
info file.
Defines utility function CSVToArray for converting an input CSV to a python 3 dimensional list
'''

import re
import csv
import os

path = os.path.dirname(__file__)

# This function takes in a logfile filename and creates 3 temp files that can be found in the testingTempfiles folder
# takes an input of a filepath and has no outputs

"""NOT COMPLETED"""
"""needs tested for not KOTH maps"""
def readLogfile(filename):

    # opens each file in the mode needed
    logfile = open(filename, 'r')
    csvfile = open(f"{path}\\testingTempfiles/tempCSV.txt", 'a')
    eventfile = open(f"{path}\\testingTempfiles/tempEvents.txt", 'a')
    mapInfofile = open(f"{path}\\testingTempfiles/tempMapInfo.txt", 'w')

    # removes the previous contents of these files since they are opened in append
    csvfile.truncate(0)
    eventfile.truncate(0)

    # if a word in this list is in the line it will move that line to the tempevents file
    listOfEventTriggers = ["FinalBlow", "Resurrected", "DuplicatingStart", "DuplicatingEnd"]
    listOfMapInfoTriggers = ["False", "True"]
    # splits the first 2 lines that contain the map info into thier own file
    for i in range(0,2):
        mapLines = logfile.readline()
        mapInfofile.write(str(mapLines))

    # splits the events from the rest of the info so that a csv format file is left
    for line in logfile:
        if any(trigger in line for trigger in listOfEventTriggers):
            eventfile.write(line)
        if any(trigger in line for trigger in listOfMapInfoTriggers) | (
                re.match("\[\d+:\d+:\d+] [0-9]+\.[0-9]+,(([0-9]+\.[0-9]+)|\d+),(([0-9]+\.[0-9]+)|\d+)\n", line) is not None):
            mapInfofile.write(line)
        else:
            csvfile.write(line)

    logfile.close()
    csvfile.close()
    eventfile.close()
    mapInfofile.close()
    pass


    ''' 
    convert the input CSV file to a list that holds each row of a matrix
    array is a list of lists where each entry in array is a line of the input file and that line is broken into a list 
    using comas as separators
    array[0][0] is the first line of the input file and the first separated string
    array[0][1] is the first line and the second separated string, and so on
    '''
def CSVToArray(filename) -> list:
    with open(filename) as CSVfile:
        file_read = csv.reader(CSVfile)
        array = list(file_read)
    return array


# start gen info functions
# completed
def getMapName(filename) -> str:
    map_array = CSVToArray(filename)
    return map_array[0][0][11:]


def getMapScore():
    return [0, 0]


# completed
def getMapType(filename) -> str:
    map_name = getMapName(filename)
    if map_name in ["Busan", "Ilios", "Lijiang Tower", "Nepal", "Oasis"]:
        return "Control"
    if map_name in ["Hanamura", "Horizon Lunar Colony", "Paris", "Temple of Anubis", "Volskaya Industries"]:
        return "Assault"
    if map_name in ["Dorado", "Havana", "Junkertown", "Rialto", "Route 66", "Watchpoint Gibraltar"]:
        return "Escort"
    if map_name in ["Blizzard World", "Eichenwalde", "Hollywood", "King's Row", "Numbani"]:
        return "Hybrid"
    else:
        print("NAN")


# completed
def getTeam(player_name) -> str:
    map_info = CSVToArray("testingTempfiles/tempMapInfo.txt")
    # team1 = map_info[0][1]
    # team2 = map_info[0][2]
    teamlist = map_info[1][:]
    teamlist[0] = teamlist[0][11:]

    if player_name in teamlist[0:6]:
        return "team1"
    elif player_name in teamlist[6:12]:
        return "team2"
    else:
        return "notFound"


# completed
# note for brody, from brody
# make a dictionary with each player as a key and assign each player a role based on priority of the hero they are playing
# to check priority find both players playing a role and loop through the possible heros until the hero the person is playing
# is found in the list, the first hero found will be the main tank, or flex dps, or main sup, and the other player will default
# to the other role, do this for each team
def defineRole(heroes) -> str:
    if heroes in ["Reinhardt", "Orisa", "Winston"]:
        return "main_tank"
    if heroes in ["D.Va", "Roadhog", "Sigma", "WreckingBall", "Zarya"]:
        return "off_tank"
    if heroes in ["Ashe", "Bastion", "Cassidy", "Reaper", "Soldier76", "Sombra", "Tracer", "Widowmaker"]:
        return "hitscan_dps"
    if heroes in ["Doomfist", "Echo", "Genji", "Hanzo", "Junkrat", "Mei", "Pharah", "Symmetra", "Torbjorn"]:
        return "flex_dps"
    if heroes in ["L\u00c3\u00bacio", "Zenyatta", "Mercy", "Brigitte"]:
        return "main_support"
    if heroes in ["Ana", "Baptiste", "Moira"]:
        return "off_support"


# completed
def getName(i, array) -> str:
    i = i + 1
    for j in range(0, 12):
        info = array[j][1:3]
        name = info[0]
        hero = info[1]
        team = getTeam(name)
        role = defineRole(hero)
        rolelist = ["main_tank", "off_tank", "hitscan_dps", "flex_dps", "main_support", "off_support"]
        # check if name is in team 1 array?
        # check if roles line up (if role = roleList[i]
        if (i >= 2) & (i <= 7) & (team == "team1"):
            if role == rolelist[i - 2]:
                return name
        elif (i >= 8) & (i <= 13) & (team == "team2"):
            if role == rolelist[i - 8]:
                return name

    for j in range(0, 12):
        info = array[j][1:3]
        name = info[0]
        hero = info[1]
        team = getTeam(name)
        role = defineRole(hero)
        rolelist = ["main_tank", "off_tank", "hitscan_dps", "flex_dps", "main_support", "off_support"]
        # check if name is in team 1 array?
        # check if roles line up (if role = roleList[i]
        if (i >= 2) & (i <= 7) & (team == "team1"):
            if role == (rolelist[i - 1] or rolelist[i - 2]):
                return name
        elif (i >= 8) & (i <= 13) & (team == "team2"):
            if (i == 13):
                if role == (rolelist[4] or rolelist[5]):
                    return name
            elif role == (rolelist[i - 7] or rolelist[i - 8]):
                return name
    return "Error"


# completed
"""
Iterate through players from array, when the player names match up return the role they played
"""
def getRole(player_name, array) -> str:
    for j in range(0, 12):
        if array[j][1] == player_name: 
            return defineRole(array[j][2]) 
    return 'Error'


def getUltTimings(player_name, array) -> list:
    # 18th thing
    ult_arr = []

    return [
        [[52, 57], [153, 154]],
        [[64, 120], [168, 169], [294, 309]],
        [[125, 160], [234, 277], [390, -1]]
    ]


def getTimeToUlt():
    return 88.375


def getTimeUltHeld():
    return 19.857


def getHeroesPlayed():
    return {
        "heroes": ["D.Va", "WreckingBall"],
        "D.Va": 835,
        "WreckingBall": 94
    }


# start final stat functions

# completed
def getFinalEntries(array) -> list:
    length = len(array)
    final_entries = []
    for i in range(1, 13):
        final_entries.append(array[length - i])
    return final_entries


def getFinalInfo(input_name, array, statnum) -> float:
    final_entries = getFinalEntries(array)
    for j in range(0, 12):
        name = final_entries[j][1]
        if name == input_name:
            stat = final_entries[j][statnum - 1]
            return float(stat)
    return None


# completed
def getAllDamageDealt(input_name, array) -> float:
    return float(getBarrierDamage(input_name, array)) + float(getHeroDamageDealt(input_name, array))


# completed
def getBarrierDamage(input_name, array) -> float:
    return getFinalInfo(input_name, array, 5)


# completed
def getCooldown1(input_name, array) -> float:
    return getFinalInfo(input_name, array, 25)


# completed
def getCooldown2(input_name, array) -> float:
    return getFinalInfo(input_name, array, 26)


# completed
def getDamageBlocked(input_name, array) -> float:
    return getFinalInfo(input_name, array, 6)


# completed
def getDamageTaken(input_name, array) -> float:
    return getFinalInfo(input_name, array, 7)


# completed
def getDeaths(input_name, array) -> float:
    return getFinalInfo(input_name, array, 8)


# completed
def getEliminations(input_name, array) -> float:
    return getFinalInfo(input_name, array, 9)


# completed
def getEnviroDeaths(input_name, array) -> float:
    return getFinalInfo(input_name, array, 11)


# completed
def getEnviroKills(input_name, array) -> float:
    return getFinalInfo(input_name, array, 12)


# completed
def getFinalBlows(input_name, array) -> float:
    return getFinalInfo(input_name, array, 10)


# completed
def getHealingDealt(input_name, array) -> float:
    return getFinalInfo(input_name, array, 13)


# completed
def getHealingReceived(input_name, array) -> float:
    return getFinalInfo(input_name, array, 18)


# completed
def getHeroDamageDealt(input_name, array) -> float:
    return getFinalInfo(input_name, array, 4)


# completed
def getObjectiveKills(input_name, array) -> float:
    return getFinalInfo(input_name, array, 14)


# completed
def getSoloKills(input_name, array) -> float:
    return getFinalInfo(input_name, array, 15)


# completed
def getUltimateCharge(input_name, array) -> float:
    return getFinalInfo(input_name, array, 19)


# completed
def getUltimatesEarned(input_name, array) -> float:
    return getFinalInfo(input_name, array, 16)


# completed
def getUltimatesUsed(input_name, array) -> float:
    return getFinalInfo(input_name, array, 17)


# start per min stat functions

'''NOTE: PLEASE READ BELOW'''
''' PLEASE READ!!!!! '''
# convertMin does NOT exclude round pauses in its calculations!!!!
def convertMin(stat, array) -> float:
    finalStats = getFinalEntries(array)[0]
    finalSec = round(float(finalStats[0][11:]))
    initialSec = round(float(array[0][0][11:]))
    timeSec = finalSec - initialSec
    return stat / (timeSec / 60)


def getFinalStats(name, array) -> dict:
    return {
        "all_damage_dealt": getAllDamageDealt(name, array),
        "barrier_damage_dealt": getBarrierDamage(name, array),
        "cooldown1": getCooldown1(name, array),
        "cooldown2": getCooldown2(name, array),
        "damage_blocked": getDamageBlocked(name, array),
        "damage_taken": getDamageTaken(name, array),
        "deaths": getDeaths(name, array),
        "eliminations": getEliminations(name, array),
        "environmental_deaths": getEnviroDeaths(name, array),
        "environmental_kills": getEnviroKills(name, array),
        "final_blows": getFinalBlows(name, array),
        "healing_dealt": getHealingDealt(name, array),
        "healing_received": getHealingReceived(name, array),
        "hero_damage_dealt": getHeroDamageDealt(name, array),
        "objective_kills": getObjectiveKills(name, array),
        "solo_kills": getSoloKills(name, array),
        "ultimate_charge": getUltimateCharge(name, array),
        "ultimates_earned": getUltimatesEarned(name, array),
        "ultimates_used": getUltimatesUsed(name, array),
    }


def getStatsPerMin(name, array) -> dict:
    return {
        "all_damage_dealt": convertMin(getAllDamageDealt(name, array), array),
        "barrier_damage_dealt": convertMin(getBarrierDamage(name, array), array),
        "cooldown1": convertMin(getCooldown1(name, array), array),
        "cooldown2": convertMin(getCooldown2(name, array), array),
        "damage_blocked": convertMin(getDamageBlocked(name, array), array),
        "damage_taken": convertMin(getDamageTaken(name, array), array),
        "deaths": convertMin(getDeaths(name, array), array),
        "eliminations": convertMin(getEliminations(name, array), array),
        "environmental_deaths": convertMin(getEnviroDeaths(name, array), array),
        "environmental_kills": convertMin(getEnviroKills(name, array), array),
        "final_blows": convertMin(getFinalBlows(name, array), array),
        "healing_dealt": convertMin(getHealingDealt(name, array), array),
        "healing_received": convertMin(getHealingReceived(name, array), array),
        "hero_damage_dealt": convertMin(getHeroDamageDealt(name, array), array),
        "objective_kills": convertMin(getObjectiveKills(name, array), array),
        "solo_kills": convertMin(getSoloKills(name, array), array),
        "ultimate_charge": convertMin(getUltimateCharge(name, array), array),
        "ultimates_earned": convertMin(getUltimatesEarned(name, array), array),
        "ultimates_used": convertMin(getUltimatesUsed(name, array), array),
    }

