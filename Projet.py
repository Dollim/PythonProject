from Classes.mains import Main
from Classes.joueur import Joueur
from Classes.domino import  Domino
from Classes.talon import Talon
from random import shuffle


mode = int(input("Veuillez choisir le mode de jeu :"))

#On nomme les deux joueurs
j1=Joueur(str(input("Comment se nomme le joueur 1 ? :")))
j2=Joueur(str(input("Comment se nomme le joueur 2 ? :")))

##Initialisation du talon selon le mode choisi
pioche = Talon(mode)
for _ in range(7):
    j1.main.append(Talon.piocher(pioche))
    j2.main.append(Talon.piocher(pioche))

print(f'Voici la main du joueur 1 : {[str(j1.main[i]) for i in range(len(j1.main))]}')
print(f'Voici la main du joueur 2 : {[str(j2.main[i]) for i in range(len(j2.main))]}')  # Attention ici je print cette expression  compliquée car {j1.main} renvoie une liste de <hfefbzbfa>



#On détermine le joueur qui commence




























