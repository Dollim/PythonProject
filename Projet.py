from Classes.mains import Main
from Classes.joueur import Joueur
from Classes.domino import  Domino
from Classes.talon import Talon
from Classes.plateau import Plateau


mode = int(input("Veuillez choisir le mode de jeu (nb de chiffres possibles:)"))
n_joueur=0
while n_joueur not in [2,4]:
    n_joueur = int(input("Veuillez choisir le nombre de joueurs (2 ou 4) "))
    if n_joueur not in [2,4]:
        print("mode de jeu indisponible")

#On nomme les n joueurs et on les ajoute à la liste temporaire

joueurs_saisies = []

for i in range(n_joueur):
    nom = input(f"Comment se nomme le joueur {i + 1} ? : ")
    joueur = Joueur(nom)
    joueurs_saisies.append(joueur)

##Initialisation du plateau, et du talon selon le mode choisi
pioche = Talon(mode)
plateau=Plateau()

# Distribution des mains de départ
taille_main_depart=7
distrib_valide=False
while distrib_valide == False:
    for _ in range(taille_main_depart):
        joueurs_saisies[0].main.append(Talon.piocher(pioche))
        joueurs_saisies[1].main.append(Talon.piocher(pioche))
    if Joueur.main_valide(joueurs_saisies[0],mode) and Joueur.main_valide(joueurs_saisies[1],mode):         #Ce paragraphe ditribu jusqu'a ce que la main soit valide
        distrib_valide=True
        print("Distribution OK")
    else:
        print("Main invalide, redistribution")



print(f'Voici la main de {joueurs_saisies[0].nom} : {[(joueurs_saisies[0].main[i]) for i in range(len(joueurs_saisies[0].main))]}')
print(f'Voici la main de {joueurs_saisies[1].nom} : {[(joueurs_saisies[1].main[i]) for i in range(len(joueurs_saisies[1].main))]}')

#On détermine le joueur qui commence
if n_joueur == 2:
    domino_start=Joueur.attribution_ordre(joueurs_saisies[0],joueurs_saisies[1],mode)

liste_joueurs = [None for i in range(n_joueur)]
for joueur in joueurs_saisies:
        liste_joueurs[joueur.ordre-1]=joueur

### DEFINITION D'UN TOUR
partie_en_cours=True
n_tour = 1


while partie_en_cours:
    print("\n" + "-" * 40)

    if n_tour == 1:
        j_actif = liste_joueurs[0]
        index_depart = None

        for i in range(len(j_actif.main)):
            if j_actif.main[i] == domino_start:
                index_depart = i
                break

        if index_depart is not None:
            domino_pose = j_actif.placer(index_depart)
            # Si j_actif.placer(i) ne retourne rien, on garde domino_start
            domino_a_poser = domino_pose if domino_pose is not None else domino_start
            plateau.placer(domino_a_poser, "d")
        else:
            print("Attention : domino_start introuvable dans la main du premier joueur.")
            plateau.placer(domino_start, "d")

        n_tour += 1
        j_actif= liste_joueurs[(n_tour - 1) % n_joueur]


        print(f"Tour {n_tour} — C'est au tour de {j_actif.nom}")
        print("Plateau :", plateau)

        print(f"Ta main :{j_actif.main}")

        peut_jouer = False

        for i in range(len(j_actif.main)):
            for cote in ["d", "g"]:
                if Domino.posable(j_actif.main[i],plateau,cote):
                    peut_jouer = True

        if peut_jouer == False:
            print("Vous ne pouvez pas poser de domino, vous devez piocher")
            j_actif.main.append(Talon.piocher(pioche))
            n_tour+=1

        while peut_jouer:
            indice = -1
            while indice<0 or indice > len(j_actif.main)-1:
                indice = int(input("Donnez l'indice du domino que vous voulez jouer")) - 1

            cote = ""
            while cote not in ["d", "g"]:
                cote = input("Où voulez vous le placer (d/g) ?")

            if Domino.posable(j_actif.main[indice], plateau, cote):
                domino = j_actif.placer(indice)
                plateau.placer(domino, cote)
                if j_actif.victoire(pioche):
                    print(f"Le joueur {j_actif.nom} a gagné")
                    partie_en_cours = False
                n_tour += 1
                peut_jouer = False
            else:
                print("Ce domino ne peut pas être posé ici")








































