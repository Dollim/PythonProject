from Classes.domino import Domino
from Classes.talon import Talon
from Classes.joueur import Joueur

class Main():

    def __init__(self,list):
        self.list= list

    def retirer(self,Domino):
        pass

if __name__== "__main__":
    pioche=Talon()
    print(pioche)
    j1 = Joueur('Thonny')
    for _ in range(7):
        j1.main.append(Talon.piocher(pioche))
    j1.main.plus_grand_double()







