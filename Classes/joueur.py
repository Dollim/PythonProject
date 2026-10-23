
class Joueur():

    def __init__(self, n):
        self.nom = n
        self.main=[]
        self.manches_gagnees=0

    def piocher(self,talon):
        return self.main.append(talon.piocher())

    def tirage_au_sort(self):
        return 1

    def a_gagne(self):
        self.manches_gagnees+=1



Mayeul=Joueur(1)
Mayeul.a_gagne()
print(Mayeul.manches_gagnees)