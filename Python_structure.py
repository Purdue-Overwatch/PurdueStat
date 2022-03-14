import json

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
    return {}

def getStatsPerMinute():
    return {}

def getUltTimings():
    return []

def getHeroesPlayed():
    return {}

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
if __name__ == '__main__':
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