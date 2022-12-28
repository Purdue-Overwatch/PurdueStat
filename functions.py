'''
Defines getter functions and organizes them into dictionaries to be imported into other files. 

Defines utility function readLogFile for reading in an Overwatch log file and seperating it into an event file, a CSV file, and an
info file.
'''

import os
import pymongo

address = os.getenv('PURDUESTAT_MONGO_ADDRESS')
client = pymongo.MongoClient(address)
db = client['game_server']
collection = db['games']
game_db = collection.find_one({'_id': 'dbecea12163e'}) # take in id


'''Constants'''
TANKS = ['Reinhardt', 'Winston', 'Orisa', 'Wrecking Ball', 'Roadhog', 'Zarya', 'Sigma', 'D.Va', ]
DPS = ['Echo', 'Pharah', 'Doomfist', 'Junkrat', 'Mei', 'Sombra', 'Torbjorn', 'Genji', 'Hanzo', 'Symmetra', 'Reaper', 'Soldier: 76', 'Tracer', 'Bastion', 'Ashe', 'Cassidy', 'Widowmaker', 'Sojourn', ]
SUPPORTS = ['L\u00c3\u00bacio', 'Brigitte', 'Mercy', 'Moira', 'Zenyatta', 'Baptiste', 'Ana', 'Kiriko', ]

# Begin basic functions
def get_map_name(game) -> str:
    return game_db['_map_name']

# Required?
# def getMapScore():
#     return [0, 0]


def get_team(name) -> str:
    for i in range(6):
        if name is game_db['_team_one']['_players'][i]['_name']:
            return 'team1'
    return 'team2'

def define_role(heroes) -> str:
    if heroes in TANKS:
        return 'Tank'
    if heroes in DPS:
        return 'Dps'
    if heroes in SUPPORTS:
        return 'Support'

def assignRoles(players, heroes):
    hero1 = heroes[0]
    hero2 = heroes[1]
    output = []
    if define_role(heroes[0]) == 'Tank':
        for hero in TANKS:
            if hero1 == hero:
                output.append(players[0])
                output.append(players[1])
                break
            elif hero2 == hero:
                output.append(players[1])
                output.append(players[0])
                break
    elif define_role(heroes[0]) == 'Dps':
        for hero in DPS:
            if hero1 == hero:
                output.append(players[0])
                output.append(players[1])
                break
            elif hero2 == hero:
                output.append(players[1])
                output.append(players[0])
                break
    elif define_role(heroes[0]) == 'Support':
        for hero in SUPPORTS:
            if hero1 == hero:
                output.append(players[0])
                output.append(players[1])
                break
            elif hero2 == hero:
                output.append(players[1])
                output.append(players[0])
                break
    return output


def makePlayerDict(array):
    names = []
    heroes = []
    team1players = []
    team1heroes = []
    team2players = []
    team2heroes = []
    ordered_names = []
    for j in range(0, 12):
        info = array[j][1:3]
        names.append(info[0])
        heroes.append(info[1])
    for i in range(0, 12):
        team = get_team(names[i])
        if team == 'team1':
            team1players.append(names[i])
            team1heroes.append(heroes[i])
        elif team == 'team2':
            team2players.append(names[i])
            team2heroes.append(heroes[i])
        else:
            pass
    for [team, heroes] in [[team1players, team1heroes], [team2players, team2heroes]]:
        tankplayers = []
        tankheroes = []
        dpsplayers = []
        dpsheroes = []
        supportplayers = []
        supportheroes = []
        for i in range(0,6):
            if define_role(heroes[i]) == 'Tank':
                tankplayers.append(team[i])
                tankheroes.append(heroes[i])
            elif define_role(heroes[i]) == 'Dps':
                dpsplayers.append(team[i])
                dpsheroes.append(heroes[i])
            elif define_role(heroes[i]) == 'Support':
                supportplayers.append(team[i])
                supportheroes.append(heroes[i])
            else:
                pass
        sortedtank = assignRoles(tankplayers, tankheroes)
        sorteddps = assignRoles(dpsplayers, dpsheroes)
        sortedsupport = assignRoles(supportplayers, supportheroes)
        ordered_names.append(sortedtank[0])
        ordered_names.append(sortedtank[1])
        ordered_names.append(sorteddps[1])
        ordered_names.append(sorteddps[0])
        ordered_names.append(sortedsupport[0])
        ordered_names.append(sortedsupport[1])
    return ordered_names


# Iterate through players from array, when the player names match up return the role they played

def getRole(player_name, array) -> str:
    count = 0
    for player in array:
        if player == player_name:
            if count % 6 == 0:
                return 'main_tank'
            elif count % 6 == 1:
                return 'off_tank'
            elif count % 6 == 2:
                return 'hitscan_dps'
            elif count % 6 == 3:
                return 'flex_dps'
            elif count % 6 == 4:
                return 'main_support'
            elif count % 6 == 5:
                return 'flex_support'
        count += 1


    for j in range(0, 12):
        if array[j][1] == player_name:
            return define_role(array[j][2])
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


# start final stat functions

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



def getAllDamageDealt(input_name, array) -> float:
    return float(getBarrierDamage(input_name, array)) + float(getHeroDamageDealt(input_name, array))



def getBarrierDamage(input_name, array) -> float:
    return getFinalInfo(input_name, array, 5)



def getCooldown1(input_name, array) -> float:
    return getFinalInfo(input_name, array, 25)



def getCooldown2(input_name, array) -> float:
    return getFinalInfo(input_name, array, 26)



def getDamageBlocked(input_name, array) -> float:
    return getFinalInfo(input_name, array, 6)



def getDamageTaken(input_name, array) -> float:
    return getFinalInfo(input_name, array, 7)



def getDeaths(input_name, array) -> float:
    return getFinalInfo(input_name, array, 8)



def getEliminations(input_name, array) -> float:
    return getFinalInfo(input_name, array, 9)



def getEnviroDeaths(input_name, array) -> float:
    return getFinalInfo(input_name, array, 11)



def getEnviroKills(input_name, array) -> float:
    return getFinalInfo(input_name, array, 12)



def getFinalBlows(input_name, array) -> float:
    return getFinalInfo(input_name, array, 10)



def getHealingDealt(input_name, array) -> float:
    return getFinalInfo(input_name, array, 13)



def getHealingReceived(input_name, array) -> float:
    return getFinalInfo(input_name, array, 18)



def getHeroDamageDealt(input_name, array) -> float:
    return getFinalInfo(input_name, array, 4)



def getObjectiveKills(input_name, array) -> float:
    return getFinalInfo(input_name, array, 14)



def getSoloKills(input_name, array) -> float:
    return getFinalInfo(input_name, array, 15)



def getUltimateCharge(input_name, array) -> float:
    return getFinalInfo(input_name, array, 19)



def getUltimatesEarned(input_name, array) -> float:
    return getFinalInfo(input_name, array, 16)



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
        'all_damage_dealt': getAllDamageDealt(name, array),
        'barrier_damage_dealt': getBarrierDamage(name, array),
        'cooldown1': getCooldown1(name, array),
        'cooldown2': getCooldown2(name, array),
        'damage_blocked': getDamageBlocked(name, array),
        'damage_taken': getDamageTaken(name, array),
        'deaths': getDeaths(name, array),
        'eliminations': getEliminations(name, array),
        'environmental_deaths': getEnviroDeaths(name, array),
        'environmental_kills': getEnviroKills(name, array),
        'final_blows': getFinalBlows(name, array),
        'healing_dealt': getHealingDealt(name, array),
        'healing_received': getHealingReceived(name, array),
        'hero_damage_dealt': getHeroDamageDealt(name, array),
        'objective_kills': getObjectiveKills(name, array),
        'solo_kills': getSoloKills(name, array),
        'ultimate_charge': getUltimateCharge(name, array),
        'ultimates_earned': getUltimatesEarned(name, array),
        'ultimates_used': getUltimatesUsed(name, array),
    }


def getStatsPerMin(name, array) -> dict:
    return {
        'all_damage_dealt': convertMin(getAllDamageDealt(name, array), array),
        'barrier_damage_dealt': convertMin(getBarrierDamage(name, array), array),
        'cooldown1': convertMin(getCooldown1(name, array), array),
        'cooldown2': convertMin(getCooldown2(name, array), array),
        'damage_blocked': convertMin(getDamageBlocked(name, array), array),
        'damage_taken': convertMin(getDamageTaken(name, array), array),
        'deaths': convertMin(getDeaths(name, array), array),
        'eliminations': convertMin(getEliminations(name, array), array),
        'environmental_deaths': convertMin(getEnviroDeaths(name, array), array),
        'environmental_kills': convertMin(getEnviroKills(name, array), array),
        'final_blows': convertMin(getFinalBlows(name, array), array),
        'healing_dealt': convertMin(getHealingDealt(name, array), array),
        'healing_received': convertMin(getHealingReceived(name, array), array),
        'hero_damage_dealt': convertMin(getHeroDamageDealt(name, array), array),
        'objective_kills': convertMin(getObjectiveKills(name, array), array),
        'solo_kills': convertMin(getSoloKills(name, array), array),
        'ultimate_charge': convertMin(getUltimateCharge(name, array), array),
        'ultimates_earned': convertMin(getUltimatesEarned(name, array), array),
        'ultimates_used': convertMin(getUltimatesUsed(name, array), array),
    }
