"""
A Player Class
Updated: 5/12/2022 - TechnoWizzy
"""


class Player:
    """
    Player object
    """

    def __init__(self, name, hero, role):
        self._role = role
        self._hero = hero
        self._name = name
        self._final_blows = 0
        self._deaths = 0
        self._hero_dmg = 0
        self._barrier_dmg = 0
        self._heals = 0
        self._dmg = 0
        self._ults_earned = 0
        self._ults_used = 0
        self._avg_ult_time = 0
        self._avg_ult_held = 0
