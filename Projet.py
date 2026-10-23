from Classes.main import Main
from Classes.joueur import Joueur
from Classes.domino import  Domino
from Classes.talon import Talon
import random


# Générer les dominos et les joueurs

plateau=[Domino(i,j) for i in range(0,7) for j in range(i,7)]
random.shuffle(plateau)
Joueur(n).main = [pop(plateau) for _ in range(7)]
talon


















