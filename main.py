from cgi import test
import json
import functions
import sys
import os


def main(filenames):
    # initializes the match list that is appended once for every logfile
    match = []
    for j in range(0, len(filenames)):
        path = os.path.dirname(__file__)
        # breaks the logfile up into its temp files
        functions.readLogfile(f"{path}\\{filenames[j]}")

        # creates an array for the csvfile that was converted
        CSVarray = functions.CSVToArray(f"{path}\\testingTempfiles\\tempCSV.txt")
        array_json = json.dumps(CSVarray, indent=4)
        f = open("arrayfile.json", "w")
        f.write(array_json)
        f.close()

        # creates the outermost dictionary that is for each map
        map_dict = {
            "map": functions.getMapName("testingTempfiles/tempMapInfo.txt"),
            "map_score": functions.getMapScore(),
            "map_type": functions.getMapType("testingTempfiles/tempMapInfo.txt"),
        }

        # these lines set default values for the player variables so that they can't be undefined
        player_number = -1
        player = {}

        playerDict = functions.makePlayerDict(CSVarray)

        # this loop creates each entry for the 12 player
        for i in range(0, 12):
            playerNumber = "player" + str(i)
            playerName = playerDict[i]
            player = {
                "name": playerName,
                "role": functions.getRole(playerName, playerDict),
                "avg_time_to_ult": functions.getTimeToUlt(),
                "avg_time_ult_held": functions.getTimeUltHeld(),
                "final_stats": functions.getFinalStats(playerName, CSVarray),
                "stats_per_minute": functions.getStatsPerMin(playerName, CSVarray),
                "ult_timings": functions.getUltTimings(playerName, CSVarray),
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


if __name__ == '__main__':

    filenames = ['MoreScrims/testscrim2/Log-2022-04-11-20-06-16.txt',
                 'MoreScrims/testscrim2/Log-2022-04-11-20-25-37.txt',
                 'MoreScrims/testscrim2/Log-2022-04-11-20-46-40.txt',
                 'MoreScrims/testscrim2/Log-2022-04-11-21-04-58.txt',
                 'MoreScrims/testscrim2/Log-2022-04-11-21-24-25.txt',
                 'MoreScrims/testscrim2/Log-2022-04-11-21-45-31.txt']

    main(filenames)
