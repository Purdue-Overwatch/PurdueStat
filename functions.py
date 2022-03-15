'''
Defines getter functions and organizes them into dictionaries to be imported into other files. 

(Sherdy describe what you did here)
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

# converts the inputed CSV file to an array
def CSVToArray(filename):
    with open(filename) as CSVfile:
        file_read = csv.reader(CSVfile)
        array = list(file_read)
    return array


# start gen info functions
def getMapName():
    return "Oasis"


def getMapScore():
    return [0, 0]


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


def getGenFunctions():
    return {
        "getMapName": getMapName(),
        "getMapScore": getMapScore(),
        "getMapType": getMapType(),
        "getName": getName(),
        "getRole": getRole(),
        "getTimeToUlt": getTimeToUlt(),
        "getTimeUltHeld": getTimeUltHeld(),
        "getFinalStats": getFinalStats(),
        "getStatsPerMin": getStatsPerMin(),
        "getUltTimings": getUltTimings(),
        "getHeroesPlayed": getHeroesPlayed(),
    }
