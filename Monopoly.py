import numpy as np 

class User():

    def __init__(self, money=1500, property={}, goj_card=False) -> None:
        self.money = money
        self.property = property
        self.goj_card = goj_card