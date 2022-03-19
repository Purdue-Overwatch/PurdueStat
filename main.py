from cgi import test
import json
import functions
import sys
import os

# opens a test .json file and writes the contents to that file
# only works if your folder is named PurdueStat for now

path = os.path.dirname(__file__)


if __name__ == '__main__':
    # breaks the logfile up into its temp files
    functions.readLogfile(f"{path}\\exampleData\\src2.txt")

    # creates an array for the csvfile that was converted
    CSVarray = functions.CSVToArray(f"{path}\\testingTempfiles\\tempCSV.txt")
    print(CSVarray)
    array_json = json.dumps(CSVarray, indent=4)
    f = open("arrayfile.json", "w")
    f.write(array_json)
    f.close()

    match = []
    # currently loops twice, would need to loop for as many files as we have
    # this loop adds entries into the match list, allowing more than 1 map be to represented
    for j in range(0, 1):
        # creates the outermost dictionary that is for each map
        map_dict = {
            "map": functions.getMapName("testingTempfiles/tempMapInfo.txt"),
            "map_score": functions.getMapScore(),
            "map_type": functions.getMapType("testingTempfiles/tempMapInfo.txt"),
        }

        # these lines set default values for the player variables so that they can't be undefined
        player_number = -1
        player = {}

        # this loop creates each entry for the 12 player
        for i in range(1, 13):
            playerNumber = "player" + str(i)
            playerName = functions.getName(i, CSVarray)
            player = {
                "name": playerName,
                "role": functions.getRole(playerName, CSVarray),
                "avg_time_to_ult": functions.getTimeToUlt(),
                "avg_time_ult_held": functions.getTimeUltHeld(),
                "final_stats": functions.getFinalStats(playerName, CSVarray),
                "stats_per_minute": functions.getStatsPerMin(playerName, CSVarray),
                "ult_timings": functions.getUltTimings(),
                "heroes_played": functions.getHeroesPlayed(),
            }
        # updates the map dictionary with the current player of the loop
            map_dict[playerNumber] = player

        # this line adds the map to the match list
        match.append(map_dict)
        # print(map_dic)

    # converts match to a json format
    json_match = json.dumps(match, indent=4)
    # the output printed to terminal
    # print(json_match)

    f = open("testingTempfiles/demofile.json", "w")
    f.write(json_match)
    f.close()
