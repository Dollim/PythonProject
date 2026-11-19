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

    def __eq__(self, j2):
        return self.nom == j2.nom and self.main == j2.main and self.manches_gagnees == j2.manches_gagnees

    def piocher(self,talon):
        self.main.append(Talon.piocher(talon))

    def a_gagne(self):
        self.manches_gagnees+=1

    def double_max(self):
        L=[]
        for e in self.main:
            if e.g==e.d:
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

    def score_main(self):
        score = 0
        for domino in self.main:
            score += domino.score
        return score

    #def attribution_ordre(self,j2,mode):
        d1 = self.plus_grand_double(mode)
        d2 = j2.plus_grand_double(mode)
        val1 = d1[0] if d1 is not None else -1
        val2 = d2[0] if d2 is not None else -1

        if val1 > val2:
            self.ordre = 1
            j2.ordre = 2
            return d1[1]
        elif val1 < val2:
            self.ordre = 2
            j2.ordre = 1
            return d2[1]
        else:
            if self.score_max(mode)[0] > j2.score_max(mode)[0]:
                self.ordre = 1
                j2.ordre = 2
                return self.score_max(mode)[1]
            else:
                self.ordre = 2
                j2.ordre = 1
                return j2.score_max(mode)[1]

    def attribution_ordre(self, liste_joueurs, mode):

        if type(liste_joueurs) is not list:
            liste_joueurs = [self, liste_joueurs]


        meilleur_double_val = -1
        gagnant_double = None
        domino_double = None

        for j in liste_joueurs:
            d = j.plus_grand_double(mode)
            if d is not None and d[0] > meilleur_double_val:
                meilleur_double_val = d[0]
                gagnant_double = j
                domino_double = d[1]


        if gagnant_double is not None:
            premier = gagnant_double
            domino_depart = domino_double
        else:   #on prends celui qui a le meilleur score sinon
            meilleur_score_val = -1
            premier = liste_joueurs[0]
            domino_depart = None

            for j in liste_joueurs:
                s = j.score_max(mode)
                if s is not None and s[0] > meilleur_score_val:
                    meilleur_score_val = s[0]
                    premier = j
                    domino_depart = s[1]

        indice_du_premier = 0
        for i in range(len(liste_joueurs)):
            if liste_joueurs[i] == premier:
                indice_du_premier = i
        n = len(liste_joueurs)

        for i in range(n):
            joueur_courant = liste_joueurs[(indice_du_premier + i) % n]
            joueur_courant.ordre = i + 1

        return domino_depart

    def peut_encore_jouer(self, plateau):
        for d in self.main:
            if d.posable(plateau, "g") or d.posable(plateau, "d"):
                return True
        return False

    def placer(self,i):
        return(self.main.pop(i))

    #fonction victoire à copléter

    def victoire(self,plateau, pioche, liste_joueurs):
        if len(self.main)== 0:
            return True

        if len(pioche.talon) == 0: # si talon vide mais au moins un joueur peut encore jouer
            for joueur in liste_joueurs:
                if joueur.peut_encore_jouer(plateau):
                    return False

        #personne ne peut jouer : on cherche le score le plus bas
            plus_petit_score = liste_joueurs[0].score_main()
            for joueur in liste_joueurs:
                if joueur.score_main() < plus_petit_score:
                    plus_petit_score = joueur.score_main()

            gagnants = []
            for joueur in liste_joueurs:
                if joueur.score_main() == plus_petit_score:
                    gagnants.append(joueur)

            if len(gagnants)==1 and gagnants[0]==self:
                return True
        return False









