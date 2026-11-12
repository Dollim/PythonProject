from Classes.mains import Main
from Classes.joueur import Joueur
from Classes.domino import  Domino
from Classes.talon import Talon
from random import shuffle

mode = int(input("Veuillez choisir le mode de jeu (nb de chiffres possibles:)"))

#On nomme les deux joueurs
j1=Joueur(str(input("Comment se nomme le joueur 1 ? :")))
j2=Joueur(str(input("Comment se nomme le joueur 2 ? :")))

##Initialisation du talon selon le mode choisi
pioche = Talon(mode)

# Distribution des mains de départ
taille_main_depart=7
distrib_valide=False
while distrib_valide == False:
    for _ in range(taille_main_depart):
        j1.main.append(Talon.piocher(pioche))
        j2.main.append(Talon.piocher(pioche))
    if Joueur.main_valide(j1,mode) and Joueur.main_valide(j2,mode):         #Ce paragraphe ditribu jusqu'a ce que la main soit valide
        distrib_valide=True
        print("Distribution OK")
    else:
        print("Main invalide, redistribution")



print(f'Voici la main de {j1.nom} : {[(j1.main[i]) for i in range(len(j1.main))]}')
print(f'Voici la main de {j2.nom} : {[(j2.main[i]) for i in range(len(j2.main))]}')
# Attention ici je print cette expression  compliquée car {j1.main} renvoie une liste de <hfefbzbfa>

#On détermine le joueur qui commence

if j1.plus_grand_double(mode)>j2.plus_grand_double(mode):
    j1.ordre = 1
    j2.ordre = 2
else:
    j1.ordre = 2
    j2.ordre = 1
if j1.plus_grand_double(mode)==j2.plus_grand_double(mode):
    if j1.score_max>j2.score_max:
        j1.ordre = 1
        j2.ordre = 2
    else:
        j1.ordre = 2
        j2.ordre = 1

if j1.ordre == 1:
    print("le joueur est "+j1.nom)
else :
    print("le joueur est " +j2.nom)



### DEFINITION D'UN TOUR
partie_en_cours=True
while partie_en_cours:





















