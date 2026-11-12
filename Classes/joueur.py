from Classes.talon import Talon
from Classes.domino import Domino
from random import random
from Classes.plateau import Plateau

class Joueur:

    def __init__(self, n):
        self.nom = n
        self.main=[]
        self.manches_gagnees=0
        self.ordre=0

    def __eq__(self,j2):
        return self.nom==j2.nom and self.main==j2.main and self.manche_gagnees==j2.manches_gagnees

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

    def plus_grand_double(self, mode):
        double_max = -1
        for i in range(mode):
            if self.est_present(Domino(i, i)) and i > double_max:
                double_max = i
        if double_max == -1:
            return None
        return double_max, Domino(double_max, double_max)

    def score_max(self,mode):
        score=0
        domino_score_max= Domino(0,0)
        for d in self.main:
            if d.score()>score:
                score = d.score()
                domino_score_max=d
        return score,domino_score_max

    def attribution_ordre(self,j2,mode):
        if self.plus_grand_double(mode) > j2.plus_grand_double(mode):
            self.ordre = 1
            j2.ordre = 2
            return self.plus_grand_double(mode)[1]
        elif self.plus_grand_double(mode) < j2.plus_grand_double(mode):
            self.ordre = 2
            j2.ordre = 1
            return j2.plus_grand_double(mode)[1]
        elif self.plus_grand_double(mode) == j2.plus_grand_double(mode):
            if self.score_max > j2.score_max:
                self.ordre = 1
                j2.ordre = 2
                return self.score_max(mode)[1]
            else:
                self.ordre = 2
                j2.ordre = 1
                return j2.score_max(mode)[1]


    def placer(self,i):
        return(self.main.pop(i-1))