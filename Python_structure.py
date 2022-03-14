import json

def getName():
    return "Golex"

def getRole():
    return "main_tank"

def getTimeToUlt():
    return 88.375

def getTimeUltHeld():
    return 19.857

def finalStats():
    return {}

functionDict = {
    "getName": getName,
    "getRole": getRole,
    "getTimeToUlt": getTimeToUlt,
    "getTimeUltHeld": getTimeUltHeld,
    "finalStats":finalStats,
}

if __name__ == '__main__':
    match = []
    for i in range(1,3):
        map_name = "Oasis"
        map_score = [0,0]
        map_type = "Control"

        map_dic = {
            "map": map_name,
            "map_score": '',
            "map_type": '',
        }

        name = "Golex"
        role = "main_tank"
        avg_time_to_ult = 88.375
        avg_time_ult_held = 19.857
        final_stats = {}
        stats_per_minute = {}
        ult_timings = []
        heroes_played = {}

        for i in range(1,13):
            player = {
                "name": name,
                "role": role,
                "avg_time_to_ult": avg_time_to_ult,
                "avg_time_ult_held": avg_time_ult_held,
                "final_stats": final_stats,
                "stats_per_minute": stats_per_minute,
                "ult_timings": ult_timings,
                "heroes_played": heroes_played
            }
            player_number = "player" + str(i)
            map_dic[player_number] = player

        print(map_dic)
        match.append(map_dic)

    print(match)
    json_match = json.dumps(match)
    print(json_match)