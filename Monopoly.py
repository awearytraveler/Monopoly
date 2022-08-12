import numpy as np 

class Board():

    def __init__(self):

        pass

class User():

    def __init__(self, money=1500, property={}, goj_card=False, railroad=0, utility=0) -> None:
        self.money = money
        self.property = property
        self.goj_card = goj_card
        self.railroad = railroad
        self.utility = utility

    