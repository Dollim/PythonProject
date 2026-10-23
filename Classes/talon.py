from domino import Domino
from random import shuffle

class Talon:
    def __init__(self,mode=7):
        self.talon=[Domino(i,j) for i in range(0,mode) for j in range(i,mode)]
        shuffle(self.talon)

    def piocher(self):
        if len(self.talon)>0:
            return self.talon.pop(0)
        return None

    def __str__(self):
        t=""
        if len(self.talon)>1:
            for e in self.talon[:-2]:
                t+=str(e)+" , "
        t+=str(self.talon[-1])
        return t


if __name__== "__main__":
    t=Talon(7)
    print(t)
    t.piocher()
    print(t)
