import pytorch
import numpy as np 
from board_constants import *

def roll():

        roll = np.random.randint(1,7) + np.random.randint(1,7)
        return roll

class User():

    def __init__(self, name, money=1500, property={}, goj_card=False, railroad=0, utility=0, current_square=0) -> None:
        
        self.name = name
        self.money = money
        self.property = property   # Eg: {"property":"1 house"}
        self.goj_card = goj_card
        self.railroad = railroad
        self.utility = utility
        self.current_square = current_square
    


class Board():

    def __init__(self, players):

        self.user_dict = dict()
        np.random.shuffle(players)
        for p in players:
            self.user_dict[p] = User(p)
        
        self.remaining_properties = list(BOARD_PROPERTY.keys())
        self.property_map = {p:None for p in self.remaining_properties}

    
    def checkSquare(self, square):
        prop = BOARD_SQUARES[square]
        if prop in BOARD_PROPERTY.keys():    
            owner = self.property_map[prop]
            if owner:
                valuation = self.user_dict[owner].property[prop]
                rent = BOARD_PROPERTY[prop][valuation]
                return rent
            
            return AVAILABLE
        
        if prop in ["Chance", "Community Chest"]:
            pass # To be implemented - Do we group chance by cases and construct a function

    def updatePlayer(self, player, square):
        pass

    def movePlayer(self, player, roll): 

        value = roll()
        updated_square = (self.user_dict[player].current_square+value)%40
        self.user_dict[player].current_square = updated_square
    
    def chance_or_community(self):
            
        
if __name__ == "__main__":

    pass
        


    