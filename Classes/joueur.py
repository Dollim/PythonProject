class Joueur:

    def __init__(self, n):
        self.nom = n
        self.main=[]
        self.manches_gagnees=0

    def piocher(self,talon):
        return self.main.append(talon.piocher())

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





Mayeul=Joueur(1)
Mayeul.a_gagne()
print(Mayeul.manches_gagnees)