'''
Creating Player class so we can have multiple player objects exist at the same time to query player statistics against each other in the future.
'''
class Player:
    '''
    Player object
    '''

    def get_role():
        return "role"

    def set_role(self, role):
        self._role = role