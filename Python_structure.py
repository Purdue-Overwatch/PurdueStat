import json

def writeJson(contents):
    f = open("PurdueStat/demofile.json", "w")
    f.write(contents)
    f.close()
    return

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
    return {}

def getStatsPerMinute():
    return {}

def getUltTimings():
    return []

def getHeroesPlayed():
    return {}

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

if __name__ == '__main__':
    match = []
    for i in range(1,3):
        '''    map_name = "Oasis"
        map_score = [0,0]
        map_type = "Control"'''

        map_dic = {
            "map": functionDict["getMapName"],
            "map_score": functionDict["getMapScore"],
            "map_type": functionDict["getMapType"],
        }

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
            map_dic[player_number] = player

        #print(map_dic)
        match.append(map_dic)

    #print(match)
    json_match = json.dumps(match)
    print(json_match)
    writeJson((json_match))