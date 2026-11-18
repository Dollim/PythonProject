from Classes.joueur import Joueur
from Classes.domino import  Domino
from Classes.talon import Talon
from Classes.plateau import Plateau


def afficher_plateau(joueur_actuel, plateau_dominos, message=""):
    print("\n" * 50)
    print("=" * 60)
    print("Jeu de Dominos")
    print("=" * 60)

    print("\n[ Plateau ]")
    if not plateau_dominos.p:
        print("  (Le plateau est vide)")
    else:
        print(f"  {plateau_dominos}")

    print("-" * 60)

    print(f"\n[ Main de : {joueur_actuel.nom} ]")

    print("-" * 60)

    print(f"\n[ Informations ]")

    print("=" * 60)


mode = int(input("Veuillez choisir le mode de jeu (nb de chiffres possibles):"))

#On nomme les deux joueurs
j1=Joueur(str(input("Comment se nomme le joueur 1 ? :")))
j2=Joueur(str(input("Comment se nomme le joueur 2 ? :")))

##Initialisation du plateau, et du talon selon le mode choisi
pioche = Talon(mode)
plateau=Plateau()

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

#On détermine le joueur qui commence

domino_start=Joueur.attribution_ordre(j1,j2,mode)

if j1.ordre == 1:
    j_actif = j1
    j_inactif = j2
    print(f"Le 1er joueur est {j1.nom} (grâce au domino {domino_start})")
else:
    j_actif = j2
    j_inactif = j1
    print(f"Le 1er joueur est {j2.nom} grâce au domino {domino_start})")


### DEFINITION D'UN TOUR

# d'abord on pose le premier domino et le joueur actif n'est plus actif ( et on lui retire)

j_actif.main.remove(domino_start)
plateau.placer(domino_start, "droite")

#le premier tour revient à l'autre joueur
j_actif = j_inactif

partie_en_cours=True
n_tour=1

while partie_en_cours:

## affichage du plateau
    ##print("Tour de "+j_actif.nom)
    ##print("Plateau:    ",plateau)
    ##print("Main:    ",str(j_actif.main))

##

    indice=int(input("Donnez l'indice du domino que vous voulez jouer"))-1

    domino_a_tester = j_actif.main[indice]
    #avant de demander autre chose on voit si le joueur fait pas nimp
    if 0<=indice<len(j_actif.main):

        cote = input("Où voulez vous le placer (d/g) ?")


        if Domino.posable(j_actif.main[indice],plateau,cote):
            domino=j_actif.placer(indice)
            plateau.placer(domino,cote)




















