from Classes.talon import Talon
from Classes.domino import Domino
from random import random
from Classes.plateau import Plateau

class Joueur:

    def __init__(self, n):
        self.nom = n
        self.main=[]
        self.manches_gagnees=0

    def piocher(self,talon):
        self.main.append(Talon.piocher(talon))

    def a_gagne(self):
        self.manches_gagnees+=1

    def double_max(self):
        L=[]
        for e in self.main:
            if e[0]==e[1]:
                L.append(e)
        if L!=[]:
            return min(L)
        else:
            return None

    def est_present(self,d):
        return d in self.main

    def main_valide(self,mode):          #verifie la validité de la main pour commencer à jouer
        for i in range(mode):
            taille_fam=0
            for d in self.main:
                if i in [d.d,d.g]:
                    taille_fam+=1
            if taille_fam>=5:
                return False
        return True


    def first_to_play(self,j1,j2, mode):
        double_max = -float('inf')
        first_to_play = j1
        for i in range(mode):
            if j1.est_present(Domino(i, i)) and i > double_max:
                double_max = i
                first_to_play = j1
            if j2.est_present(Domino(i, i)) and i > double_max:
                double_max = i
                first_to_play = j2
        return double_max, first_to_play


if __name__== "__main__":
    joueur1=Joueur("Mayeul")
    joueur2=Joueur("Aimélien")
    pioche=Talon(mode=7)
    for _ in range(7):
        joueur1.main.append(Talon.piocher(pioche))
        joueur2.main.append(Talon.piocher(pioche))
    print(joueur1.main)
    print(Joueur.first_to_play(j1=joueur1,j2=joueur2,mode=7))
