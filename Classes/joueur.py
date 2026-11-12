from Classes.talon import Talon
from Classes.domino import Domino

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


    def first_to_play(self, mode):
        double_max = -float('inf')
        first_to_play = random(j1,j2)
        for i in range(mode):
            if j1.est_present(Domino(i, i)) and i > double_max:
                double_max = i
                first_to_play = j1
            if j2.est_present(Domino(i, i)) and i > double_max:
                double_max = i
                first_to_play = j2

    def plus_grand_double(self):
        meilleur_double = Domino(0,0)
        for i in range(len(self.main)):
            if self.main[i].is_double() and self.main[i].score > meilleur_double.score:
                meilleur_double = self.main[i]
        return meilleur_double

if __name__== "__main__":
    joueur1=Joueur("Mayeul")
    print(joueur1.nom)
    pioche=Talon(mode=7)
    print(pioche)
    print(joueur1.main)
    Joueur.piocher(joueur1,pioche)
    print(pioche)
    print([str(joueur1.main[i]) for i in range(len(joueur1.main))])     #on verifie que la pioche fonctionne

