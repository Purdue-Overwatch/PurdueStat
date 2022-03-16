'''
Defines getter functions and organizes them into dictionaries to be imported into other files. 

Defines utility function readLogFile for reading in an Overwatch log file and seperating it into an event file, a CSV file, and an
info file.
Defines utility function CSVToArray for converting an input CSV to a python 3 dimensional list
'''

import re
import csv

# This function takes in a logfile filename and creates 3 temp files that can be found in the testingTempfiles folder
# takes an input of a filepath and has no outputs
def readLogfile(filename):

    # opens each file in the mode needed
    logfile = open(filename, 'r')
    csvfile = open("testingTempfiles/tempCSV.txt", 'a')
    eventfile = open("testingTempfiles/tempEvents.txt", 'a')
    mapInfofile = open("testingTempfiles/tempMapInfo.txt", 'w')

    # removes the previous contents of these files since they are opened in append
    csvfile.truncate(0)
    eventfile.truncate(0)

    # if a word in this list is in the line it will move that line to the tempevents file
    listOfTriggers = ["False", "True", "FinalBlow"]

    # splits the first 2 lines that contain the map info into thier own file
    for i in range(0,2):
        mapLines = logfile.readline()
        mapInfofile.write(str(mapLines))

    # splits the events from the rest of the info so that a csv format file is left
    for line in logfile:
        if any(trigger in line for trigger in listOfTriggers) | (
                re.match("\[\d+:\d+:\d+] [0-9]+\.[0-9]+,(([0-9]+\.[0-9]+)|\d+),(([0-9]+\.[0-9]+)|\d+)\n", line) is not None):
            eventfile.write(line)
        else:
            csvfile.write(line)

    logfile.close()
    csvfile.close()
    eventfile.close()
    mapInfofile.close()
    pass

# convert the input CSV file to a list that holds each row of a matrix
# array is a list of lists where each entry in array is a line of the input file and that line is broken into a list using comas as seperators
# array[0][0] is the first line of the input file and the first seperated string
# array[0][1] is the first line and the second seperated string, and so on
def CSVToArray(filename):
    with open(filename) as CSVfile:
        file_read = csv.reader(CSVfile)
        array = list(file_read)
    return array


readLogfile("exampleData\src2.txt")

# creates an array for the csvfile that was converted
array = CSVToArray("testingTempfiles/tempCSV.txt")


# start gen info functions
# completed
def getMapName(filename):
    map_array = CSVToArray(filename)
    return map_array[0][0][11:]


def getMapScore():
    return [0, 0]


# completed
def getMapType(filename):
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
def getTeam(player_name):
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
def defineRole(heroes):
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
def getName(i):
    for j in range(0, 12):
        info = array[j][1:3]
        name = info[0]
        hero = info[1]
        team = getTeam(name)
        role = defineRole(hero)
        rolelist = ["main_tank", "off_tank", "hitscan_dps", "flex_dps", "main_support", "off_support"]
        # check if name is in team 1 array?
        # check if roles line up (if role = roleList[i]
        if (i >= 1) & (i <= 6) & (team == "team1"):
            if role == rolelist[i - 1]:
                return name
        elif (i >= 7) & (i <= 12) & (team == "team2"):
            if role == rolelist[i - 7]:
                return name
    return "Error"


# completed
def getRole(player_name):
    role = 'Error'
    for j in range(0, 12):
        info = array[j][1:3]
        name = info[0]
        if name == player_name:
            hero = info[1]
            role = defineRole(hero)
    return role


def getUltTimings():
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
def getFinalEntries(arr):
    length = len(arr)
    final_entries = []
    for i in range(1, 13):
        final_entries.append(arr[length - i])
    return final_entries

# completed
def getFinalInfo(input_name, statnum):
    final_entries = getFinalEntries(array)
    for j in range(0, 12):
        name = final_entries[j][1]
        if name == input_name:
            stat = final_entries[j][statnum - 1]
            return float(stat)
    return "Error"

# completed
def getAllDamageDealt(input_name):
    return getBarrierDamage(input_name) + getHeroDamageDealt(input_name)

# completed
def getBarrierDamage(input_name):
    return getFinalInfo(input_name, 5)

# completed
def getCooldown1(input_name):
    return getFinalInfo(input_name, 25)

# completed
def getCooldown2(input_name):
    return getFinalInfo(input_name, 26)

# completed
def getDamageBlocked(input_name):
    return getFinalInfo(input_name, 6)

# completed
def getDamageTaken(input_name):
    return getFinalInfo(input_name, 7)

# completed
def getDeaths(input_name):
    return getFinalInfo(input_name, 8)

# completed
def getEliminations(input_name):
    return getFinalInfo(input_name, 9)

# completed
def getEnviroDeaths(input_name):
    return getFinalInfo(input_name, 11)

# completed
def getEnviroKills(input_name):
    return getFinalInfo(input_name, 12)

# completed
def getFinalBlows(input_name):
    return getFinalInfo(input_name, 10)

# completed
def getHealingDealt(input_name):
    return getFinalInfo(input_name, 13)

# completed
def getHealingReceived(input_name):
    return getFinalInfo(input_name, 18)

# completed
def getHeroDamageDealt(input_name):
    return getFinalInfo(input_name, 4)

# completed
def getObjectiveKills(input_name):
    return getFinalInfo(input_name, 14)

# completed
def getSoloKills(input_name):
    return getFinalInfo(input_name, 15)

# completed
def getUltimateCharge(input_name):
    return getFinalInfo(input_name, 19)

# completed
def getUltimatesEarned(input_name):
    return getFinalInfo(input_name, 16)

# completed
def getUltimatesUsed(input_name):
    return getFinalInfo(input_name, 17)


# start per min stat functions

'''NOTE: PLEASE READ BELOW'''
''' PLEASE READ!!!!! '''
# convertMin does NOT exclude round pauses in its calculations!!!!
def convertMin(stat):
    finalStats = getFinalEntries(array)[0]
    finalSec = round(float(finalStats[0][11:]))
    initialSec = round(float(array[0][0][11:]))
    timeSec = finalSec - initialSec
    return stat / (timeSec / 60)


def getFinalStats(name):
    return {
        "all_damage_dealt": getAllDamageDealt(name),
        "barrier_damage_dealt": getBarrierDamage(name),
        "cooldown1": getCooldown1(name),
        "cooldown2": getCooldown2(name),
        "damage_blocked": getDamageBlocked(name),
        "damage_taken": getDamageTaken(name),
        "deaths": getDeaths(name),
        "eliminations": getEliminations(name),
        "environmental_deaths": getEnviroDeaths(name),
        "environmental_kills": getEnviroKills(name),
        "final_blows": getFinalBlows(name),
        "healing_dealt": getHealingDealt(name),
        "healing_received": getHealingReceived(name),
        "hero_damage_dealt": getHeroDamageDealt(name),
        "objective_kills": getObjectiveKills(name),
        "solo_kills": getSoloKills(name),
        "ultimate_charge": getUltimateCharge(name),
        "ultimates_earned": getUltimatesEarned(name),
        "ultimates_used": getUltimatesUsed(name),
    }


def getStatsPerMin(name):
    return {
        "all_damage_dealt": convertMin(getAllDamageDealt(name)),
        "barrier_damage_dealt": convertMin(getBarrierDamage(name)),
        "cooldown1": convertMin(getCooldown1(name)),
        "cooldown2": convertMin(getCooldown2(name)),
        "damage_blocked": convertMin(getDamageBlocked(name)),
        "damage_taken": convertMin(getDamageTaken(name)),
        "deaths": convertMin(getDeaths(name)),
        "eliminations": convertMin(getEliminations(name)),
        "environmental_deaths": convertMin(getEnviroDeaths(name)),
        "environmental_kills": convertMin(getEnviroKills(name)),
        "final_blows": convertMin(getFinalBlows(name)),
        "healing_dealt": convertMin(getHealingDealt(name)),
        "healing_received": convertMin(getHealingReceived(name)),
        "hero_damage_dealt": convertMin(getHeroDamageDealt(name)),
        "objective_kills": convertMin(getObjectiveKills(name)),
        "solo_kills": convertMin(getSoloKills(name)),
        "ultimate_charge": convertMin(getUltimateCharge(name)),
        "ultimates_earned": convertMin(getUltimatesEarned(name)),
        "ultimates_used": convertMin(getUltimatesUsed(name)),
    }

