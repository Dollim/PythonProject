from talon import Talon

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


if __name__== "__main__":
    joueur1=Joueur("Mayeul")
    print(joueur1.nom)
    talon=Talon(mode=7)
    print(talon)
    print(joueur1.main)
    Joueur.piocher(joueur1,talon)
    print(talon)
    print(joueur1.main)

