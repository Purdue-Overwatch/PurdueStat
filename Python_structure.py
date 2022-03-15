from cgi import test
import json
import functions
import sys

# opens a test .json file and writes the contents to that file
# only works if your folder is named PurdueStat for now
def writeJson(contents):
    f = open("PurdueStat/demofile.json", "w")
    f.write(contents)
    f.close()
    return

finalStatDict = functions.getFinalStats()

minStatDict = functions.getStatsPerMin()

genFunctDict = functions.getGenFunctions()

# this line only runs when this script is ran as main
def main(filepath: str) -> int:
    match = []
    # currently loops twice, would need to loop for as many files as we have
    # this loop adds entries into the match list, allowing more than 1 map be to represented
    for i in range(1,3):
        # creates the outermoust dictionary that is for each map
        map_dic = {
            "map": genFunctDict["getMapName"],
            "map_score": genFunctDict["getMapScore"],
            "map_type": genFunctDict["getMapType"],
        }

        # this loop creates each entry for the 12 player
        

        for i in range(1,13):
            player = {
                "name": genFunctDict["getName"](),
                "role": genFunctDict["getRole"](),
                "avg_time_to_ult": genFunctDict["getTimeToUlt"](),
                "avg_time_ult_held": genFunctDict["getTimeUltHeld"](),
                "final_stats": genFunctDict["getFinalStats"](),
                "stats_per_minute": genFunctDict["getStatsPerMin"](),
                "ult_timings": genFunctDict["getUltTimings"](),
                "heroes_played": genFunctDict["getHeroesPlayed"](),
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
