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
    j1.main.append(piocher(pioche))
    j2.main.append(piocher(pioche))

print(f'Voici la main du joueur 1 : {j1.main}')
print(f'Voici la main du joueur 1 : {j2.main}')

#On détermine le joueur qui commence




























