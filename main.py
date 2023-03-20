"""Main class."""
__author__ = "Park"

from src.map import Map

MAPS = ["a1a809890993"]
DB_TEAMS = ["_team_one", "_team_two"]
DB_PLAYERS = "_players"


def main(**argv):
    """Main function."""
    maps = argv
    for map_id in MAPS:
        game = Map(map_id)
        game.set_players()


if __name__ == "__main__":
    main()
