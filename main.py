from cgi import test
import json
import functions
import sys

# opens a test .json file and writes the contents to that file
# only works if your folder is named PurdueStat for now

finalStatDict = functions.getFinalStats()

minStatDict = functions.getStatsPerMin()

genFunctDict = functions.getGenFunctions()


# ignore this for now
def main(filepath: str) -> int:
    pass


if __name__ == '__main__':
    # breaks the logfile up into its temp files
    functions.readLogfile("exampleData\src2.txt")

    # creates an array for the csvfile that was converted
    array = functions.CSVToArray("testingTempfiles/tempCSV.txt")
    array = json.dumps(array, indent=4)
    print(array)

    match = []
    # currently loops twice, would need to loop for as many files as we have
    # this loop adds entries into the match list, allowing more than 1 map be to represented
    for i in range(0,2):
        # creates the outermoust dictionary that is for each map
        map_dic = {
            "map": genFunctDict["getMapName"],
            "map_score": genFunctDict["getMapScore"],
            "map_type": genFunctDict["getMapType"],
        }

        # these lines set default values for the player variables so that they can't be undefined
        player_number = "NAN"
        player = {}

        # this loop creates each entry for the 12 player
        for i in range(1, 13):
            player = {
                "name": genFunctDict["getName"],
                "role": genFunctDict["getRole"],
                "avg_time_to_ult": genFunctDict["getTimeToUlt"],
                "avg_time_ult_held": genFunctDict["getTimeUltHeld"],
                "final_stats": genFunctDict["getFinalStats"],
                "stats_per_minute": genFunctDict["getStatsPerMin"],
                "ult_timings": genFunctDict["getUltTimings"],
                "heroes_played": genFunctDict["getHeroesPlayed"],
            }
            player_number = "player" + str(i)
        # updates the map dictionary with the current player of the loop
            map_dic[player_number] = player

        # this line adds the map to the match list
        match.append(map_dic)
        # print(map_dic)

    # converts match to a json format
    json_match = json.dumps(match, indent=4)
    # the output printed to terminal
    # print(json_match)

    f = open("testingTempfiles/demofile.json", "w")
    f.write(json_match)
    f.close()
