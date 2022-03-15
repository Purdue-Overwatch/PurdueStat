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


def getTeam(player_name):
    map_info = CSVToArray("testingTempfiles/tempMapInfo.txt")
    # team1 = map_info[0][1]
    # team2 = map_info[0][2]
    teamList = map_info[1][:]
    teamList[0] = teamList[0][11:]

    if player_name in teamList[0:6]:
        return "team1"
    elif player_name in teamList[6:12]:
        return "team2"
    else:
        return "notFound"

def defineRole(heroes):
    if heroes in ["Reinhart", "Orisa", "Winston"]:
        return "main_tank"
    if heroes in ["D.Va", "Roadhog", "Sigma", "WreckingBall", "Zarya"]:
        return "off_tank"
    if heroes in ["Ashe", "Bastion", "Cassidy", "Reaper", "Soldier76", "Sombra", "Tracer", "Widowmaker"]:
        return "hitscan_dps"
    if heroes in ["Doomfist", "Echo", "Genji", "Hanzo", "Junkrat", "Mei", "Pharah", "Symmetra", "Torbjorn"]:
        return "flex_dps"
    if heroes in ["Lucio", "Zenyatta", "Mercy", "Brigitte"]:
        return "main_support"
    if heroes in ["Ana", "Baptiste", "Moira"]:
        return "off_support"


def getName(i):
    for j in range(0, 13):
        info = array[j][1:3]
        name = info[0]
        hero = info[1]
        team = getTeam(name)
        role = defineRole(hero)
        roleList = ["main_tank", "off_tank", "hitscan_dps", "flex_dps", "main_support", "off_support"]
        # check if name is in team 1 array?
        # check if roles line up (if role = roleList[i]
        if (i >= 0 & i <= 6) & (team == "team1") & (role == roleList[i]):
            return name
        elif (i >= 7 & i <= 12) & (team == "team2") & (role == roleList[i - 6]):
            return name
        else:
            return "error"


print(getName(7))

def getRole(i):
    info = array[i][1:3]
    character = info[1]
    role = defineRole(character)
    return role



def getTimeToUlt():
    return 88.375


def getTimeUltHeld():
    return 19.857

    # what the fuck


def getUltTimings():
    return [
        [[52, 57], [153, 154]],
        [[64, 120], [168, 169], [294, 309]],
        [[125, 160], [234, 277], [390, -1]]
    ]


def getHeroesPlayed():
    return {
        "heroes": ["D.Va", "WreckingBall"],
        "D.Va": 835,
        "WreckingBall": 94
    }


# start final stat functions
def getAllDamageDealt():
    return 6942066.6


def getBarrierDamage():
    return 137.7


def getCooldown1():
    return 0.0


def getCooldown2():
    return 7.03


def getDamageBlocked():
    return 10730.0


def getDamageTaken():
    return 17221.91


def getDeaths():
    return 69


def getEliminations():
    return 53


def getEnviroDeaths():
    return 2


def getEnviroKills():
    return 1


def getFinalBlows():
    return 13


def getHealingDealt():
    return 0.0


def getHealingReceived():
    return 0.0


def getHeroDamageDealt():
    return 9416.48


def getObjectiveKills():
    return 12


def getSoloKills():
    return 2


def getUltimateCharge():
    return 100.0


def getUltimatesEarned():
    return 5


def getUltimatesUsed():
    return 2


# start per min stat functions
def getAllDamageMin():
    return 1123.652099031216


def getBarrierDamageMin():
    return 515.48


def getCooldown1Min():
    return 0.0


def getCooldown2Min():
    return 0.454


def getDamageBlockedMin():
    return 693.003


def getDamageTakenMin():
    return 1112.2869


def getDeathsMin():
    return 0.645855


def getEliminationsMin():
    return 1.94


def getEnviroDeathsMin():
    return 0.06458


def getEnviroKillsMin():
    return 0.0


def getFinalBlowsMin():
    return 0.8396


def getHealingDealtMin():
    return 0.0


def getHealingReceivedMin():
    return 0.0


def getHeroDamageDealtMin():
    return 608.1687


def getObjectiveKillsMin():
    return 0.775


def getSoloKillsMin():
    return 1000


def getUltimateChargeMin():
    return 6.458


def getUltimatesEarnedMin():
    return 0.322927


def getUltimatesUsedMin():
    return 0.12917


def getFinalStats():
    return {
        "all_damage_dealt": getAllDamageDealt(),
        "barrier_damage_dealt": getBarrierDamage(),
        "cooldown1": getCooldown1(),
        "cooldown2": getCooldown2(),
        "damage_blocked": getDamageBlocked(),
        "damage_taken": getDamageTaken(),
        "deaths": getDeaths(),
        "eliminations": getEliminations(),
        "environmental_deaths": getEnviroDeaths(),
        "environmental_kills": getEnviroKills(),
        "final_blows": getFinalBlows(),
        "healing_dealt": getHealingDealt(),
        "healing_received": getHealingReceived(),
        "hero_damage_dealt": getHeroDamageDealt(),
        "objective_kills": getObjectiveKills(),
        "solo_kills": getSoloKills(),
        "ultimate_charge": getUltimateCharge(),
        "ultimates_earned": getUltimatesEarned(),
        "ultimates_used": getUltimatesUsed(),
    }


def getStatsPerMin():
    return {
        "all_damage_dealt": getAllDamageMin(),
        "barrier_damage_dealt": getBarrierDamageMin(),
        "cooldown1": getCooldown1Min(),
        "cooldown2": getCooldown2Min(),
        "damage_blocked": getDamageBlockedMin(),
        "damage_taken": getDamageTakenMin(),
        "deaths": getDeathsMin(),
        "eliminations": getEliminationsMin(),
        "environmental_deaths": getEnviroDeathsMin(),
        "environmental_kills": getEnviroKillsMin(),
        "final_blows": getFinalBlowsMin(),
        "healing_dealt": getHealingDealtMin(),
        "healing_received": getHealingReceivedMin(),
        "hero_damage_dealt": getHeroDamageDealtMin(),
        "objective_kills": getObjectiveKillsMin(),
        "solo_kills": getSoloKillsMin(),
        "ultimate_charge": getUltimateChargeMin(),
        "ultimates_earned": getUltimatesEarnedMin(),
        "ultimates_used": getUltimatesUsedMin(),
    }


def getGenFunctions(filename):
    return {
        "getMapName": getMapName(filename),
        "getMapScore": getMapScore(),
        "getMapType": getMapType(filename),
        "getName": getName(),
        "getRole": getRole(),
        "getTimeToUlt": getTimeToUlt(),
        "getTimeUltHeld": getTimeUltHeld(),
        "getFinalStats": getFinalStats(),
        "getStatsPerMin": getStatsPerMin(),
        "getUltTimings": getUltTimings(),
        "getHeroesPlayed": getHeroesPlayed(),
    }
