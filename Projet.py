from Classes.mains import Main
from Classes.joueur import Joueur
from Classes.domino import  Domino
from Classes.talon import Talon
from Classes.plateau import Plateau


mode = int(input("Veuillez choisir le mode de jeu (nb de chiffres possibles:)"))

while n_joueur not in [2,4]:
    n_joueur = int(input("Veuillez choisir le nombre de joueurs (2 ou 4) "))
    if n_joueur not in [2,4]:
        print("mode de jeu indisponible")

#On nomme les n joueurs et on les ajoute à la liste temporaire

liste_des_joueurs_temporaire = []
for i in range(n_joueur):
    j"i" =Joueur(str(input("Comment se nomme le joueur" i " ? :")))
    liste_des_joueurs.append(j"i")

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
if n_joueur = 2:
    domino_start=Joueur.attribution_ordre(j1,j2,mode)

# ici faire le cas pour 4 joueurs
if n_joueur = 4:
    domino_start = Joueur.attribution_ordre(j1, j2, mode)

liste_des_joueurs = [0 for i in range(n_joueur)]
for i in range(n_joueur):
        liste_des_joueurs[liste_des_joueurs_temporaire[i].ordre]=liste_des_joueurs_temporaire[i]

### DEFINITION D'UN TOUR
partie_en_cours=True
n_tour = 1





while partie_en_cours:

    if n_tour==1:       # 1E tour
        plateau.placer(domino_start)
        j_actif=liste_des_joueurs[0]
        for i in range(len(j_actif.main)):
            if j_actif.main[i]==domino_start:
                j_actif.placer(i)
        n_tour+=1

    n_tour % n_joueur - 1

    j_actif= liste_des_joueurs[n_tour%n_joueur-1]

    print(f"C'est au tour du joueur" joueur_actif.nom "de jouer")

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


































