from domino import Domino
from random import shuffle

class Talon:
    def __init__(self,mode=7):
        self.talon=[Domino(i,j) for i in range(0,7) for j in range(i,7)]
        shuffle(self.talon)

    def piocher(self,talon):
        pass
