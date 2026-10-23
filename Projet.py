from Classes.mains import Main
from Classes.joueur import Joueur
from Classes.domino import  Domino
from Classes.talon import Talon
from random import shuffle

#On nomme les deux joueurs

###

#On créé et on distribue les dominos aux joueurs, puis on met le reste dans le talon

mode = int(input("Veuillez choisir le mode de jeu :"))
j1=Joueur(str(input("Comment se nomme le joueur 1 ? :")))
j2=Joueur(str(input("Comment se nomme le joueur 2 ? :")))

##Initialisation du talon selon le mode choisi
pioche = Talon(mode)
shuffle(pioche)
for _ in range(mode):
    j1.main.append(piocher(pioche))
    j2.main.append(piocher(pioche))

print
























