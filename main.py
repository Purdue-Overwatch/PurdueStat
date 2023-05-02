"""Main class."""
__author__ = "Park"

import sys

from src.map import Map

MAPS = ["a1a809890993"]
DB_TEAMS = ["_team_one", "_team_two"]
DB_PLAYERS = "_players"


def main():
    """Main function."""
    for map_id in MAPS:  # replace MAPS with sys.argv[1:]:
        game = Map(map_id)
        game.set_players()
        print(game.map_name)


if __name__ == "__main__":
    main()
