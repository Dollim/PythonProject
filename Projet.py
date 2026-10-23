from Classes.mains import Main
from Classes.joueur import Joueur
from Classes.domino import  Domino
from Classes.talon import Talon
from random import shuffle

#On nomme les deux joueurs

###

#On créé et on distribue les dominos aux joueurs, puis on met le reste dans le talon

mode = int(input("Veuillez choisir le mode de jeu :"))

##Initialisation du talon selon le mode choisi
talon = Talon(mode)
shuffle(talon)
for _ in range(mode):
    Joueur(n).main.append(piocher(talon))
    Joueur(n).main.append(piocher(talon))

#






















