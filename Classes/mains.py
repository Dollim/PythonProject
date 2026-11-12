from Classes.domino import Domino
from

class Main():

    def __init__(self,list):
        self.list= list

    def retirer(self,Domino):
        pass

    def plus_grand_double(self,list,mode):
        meilleur_double = Domino(0,0)
        for i in range(len(list)):
            if list[i].is_double() and list[i].score > meilleur_double.score:
                meilleur_double = list[i]
        return meilleur_double








