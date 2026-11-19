from Classes.mains import Main
from Classes.joueur import Joueur
from Classes.domino import  Domino
from Classes.talon import Talon
from Classes.plateau import Plateau

def quijoue(n_tour,n_joueur):
    i=1
    while True:
        if n_tour%n_joueur == i:
            return i
        else :
            i+=1

mode = int(input("Veuillez choisir le mode de jeu (nb de chiffres possibles:)"))

while n_joueur not in [2,4]:
    n_joueur = int(input("Veuillez choisir le nombre de joueurs (2 ou 4) "))
    if n_joueur not in [2,4]:
        print("mode de jeu indisponible")

#On nomme les n joueurs
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
# Attention ici je print cette expression  compliquée car {j1.main} renvoie une liste de <hfefbzbfa>

#On détermine le joueur qui commence

domino_start=Joueur.attribution_ordre(j1,j2,mode)

if j1.ordre == 1:
    print("le 1e joueur est "+j1.nom)
else :
    print("le 1e joueur est "+j2.nom)



### DEFINITION D'UN TOUR
partie_en_cours=True

n_tour = 1



while partie_en_cours:
    if n_tour==1:       # 1E tour
        plateau.placer(domino_start)
        j_actif=j1 # a modifier avec la fonction qui donne le joueur actif.
        for i in range(len(j_actif.main)):
            if j_actif.main[i]==domino_start:
                j_actif.placer(i)
        n_tour+=1



    indice = int(input("Donnez l'indice du domino que vous voulez jouer")) - 1

    if 0 <= indice < len(j_actif.main):

        cote = input("Où voulez vous le placer (droite/gauche) ?")

        if cote in ["droite", "gauche", "d", "g"]:

            if Domino.posable(j_actif.main[indice], plateau, cote):
                domino = j_actif.placer(indice)
                plateau.placer(domino, cote)

            else:
                print("le domino n'est pas posable, veuillez en choisir un autre")
                # refaire prendre un domino au joueur

        else:
    # on redemande le coté

    else:
    # on redemande le domino

    # Condition de victoire
    if condition de victoire:
        partie_en_cours = False

    n_tour += 1


































