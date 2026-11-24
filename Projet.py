from Classes.IA import*
from Classes.joueur import Joueur
from Classes.domino import  Domino
from Classes.talon import Talon
from Classes.plateau import Plateau
import time
import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

delai_tour = 0.5

prout="prout"       #tkt je fais mes test et il est tard XD
def test():
    global prout
    print(prout)

def execution():
    n_joueur=0
    while n_joueur not in [2,4]:
        n_joueur = int(input("Veuillez choisir le nombre de joueurs (2 ou 4) "))
        if n_joueur not in [2,4]:
            print("mode de jeu indisponible")
    jeu_avec_ia= input("Voulez-vous des IA? ")

    strategie_ia = "gloutonne"
    if jeu_avec_ia in ("o", "oui"):
        choix_ia = ""
        while choix_ia not in ("1", "2"):
            print("Choisissez le mode de IA :")
            print(" 1-IA gloutonne ")
            print(" 2-IA random ")
            choix_ia = input("Votre choix (1 ou 2) : ")
        strategie_ia = "gloutonne" if choix_ia == "1" else "random"

    if n_joueur == 2:
        mode = int(input("Veuillez choisir le mode de jeu (7,8,9 ou 10)"))  # Nombre de chiffres possibles (de 0 à mode-1)
        taille_main_depart = mode

    if n_joueur == 4:
        taille_main_depart = 6
        mode = 7

    #On nomme les n joueurs et on les ajoute à la liste temporaire

    joueurs_saisis = []

    for i in range(n_joueur):
        nom = input(f"Comment s'appelle le joueur {i + 1} ?: ")
        est_ia = False
        if jeu_avec_ia in ("o", "oui"):
            rep_ia = input("Est-ce une IA ? : ")
            if rep_ia in ("o", "oui"):
                est_ia = True
        joueur = Joueur(nom, est_ia)
        joueurs_saisis.append(joueur)



    ##Initialisation du plateau, et du talon selon le mode choisi
    plateau = Plateau()

    distribution_valide = False

    while not distribution_valide:
        pioche = Talon(mode)
        for j in joueurs_saisis:
            j.main = []
            for _ in range(taille_main_depart):
                domino_pioche = pioche.piocher()
                if domino_pioche is not None:
                    j.main.append(domino_pioche)
        # ici all remplace une succession de AND (c'est trop pratique)
        if all(j.main_valide(taille_main_depart) for j in joueurs_saisis):
            distribution_valide = True
            print("Distribution OK")
        else:
            print("main invalide --> redistribution")

    #print(f'Voici la main de {joueurs_saisis[0].nom} : {[(joueurs_saisis[0].main[i]) for i in range(len(joueurs_saisies[0].main))]}')
    #print(f'Voici la main de {joueurs_saisis[1].nom} : {[(joueurs_saisis[1].main[i]) for i in range(len(joueurs_saisies[1].main))]}')

    #On détermine le joueur qui commence

    domino_start=joueurs_saisis[0].attribution_ordre(joueurs_saisis,mode)

    liste_joueurs = [None for i in range(n_joueur)]
    for joueur in joueurs_saisis:
            liste_joueurs[joueur.ordre-1]=joueur

    ### DEFINITION D'UN TOUR
    partie_en_cours=True
    n_tour = 1


    while partie_en_cours:

        clear_console()
        time.sleep(delai_tour)

        print("\n" + "-" * 40)
        time.sleep(delai_tour)

        if n_tour == 1:
            j_actif = liste_joueurs[0]
            indice_premier_domino = None

            for i in range(len(j_actif.main)):
                if j_actif.main[i] == domino_start:
                    indice_premier_domino = i
                    break

            if indice_premier_domino is not None:
                domino_pose = j_actif.placer(indice_premier_domino)
                domino_a_poser = domino_pose if domino_pose is not None else domino_start
                plateau.placer(domino_a_poser, "d")
            else:
                print("Attention : domino_start introuvable dans la main du premier joueur.")
                plateau.placer(domino_start, "d")


            n_tour += 1
            continue

        j_actif= liste_joueurs[(n_tour - 1) % n_joueur]

        if j_actif.est_ia:
            fonction_ia = STRATEGIES_IA[strategie_ia]
            partie_en_cours = fonction_ia(j_actif, plateau, pioche, liste_joueurs, n_tour)
            n_tour += 1
            continue

        #je rajoute cette partie là pour si le joueur est une IA

            #coup = j_actif.choisir_coup_random(plateau)

            #if coup is None:
                #print(f"{j_actif.nom} (IA) ne peut pas jouer et pioche.")
                #domino_pioche = pioche.piocher()
                #if domino_pioche is not None:
                    #j_actif.main.append(domino_pioche)
                #else:
                    #print("Pioche vide : l'IA passe son tour")
                #n_tour += 1
                #continue

            #indice, cote = coup
            #domino = j_actif.placer(indice)
            #plateau.placer(domino, cote)
            #print(f"{j_actif.nom} (IA) pose {domino} à {'droite' if cote == 'd' else 'gauche'}.")

            #if j_actif.victoire(plateau, pioche, liste_joueurs):
                #print(f"Le joueur {j_actif.nom} (IA) a gagné !")
                #partie_en_cours = False

            #n_tour += 1
            #continue        # a quoi ca sert ce "continue"  ? - Mayeul en gros il sert à revenir en haut du while, c'est juste de l'efficacité



        print(f"Tour {n_tour} — C'est au tour de {j_actif.nom}")
        time.sleep(delai_tour)
        print("Plateau :", plateau)
        time.sleep(delai_tour)
        print(f"Ta main :{j_actif.main}")
        time.sleep(delai_tour)

        peut_jouer = False

        for i in range(len(j_actif.main)):      # A transformer en fonction de classe ?
            for cote in ["d", "g"]:
                if Domino.posable(j_actif.main[i],plateau,cote):
                    peut_jouer = True

        if peut_jouer == False:
            print("Vous ne pouvez pas poser de domino, vous devez piocher")
            time.sleep(delai_tour)
            domino_pioche = Talon.piocher(pioche)
            if domino_pioche is not None:
                j_actif.main.append(domino_pioche)
            else:
                print("Pioche vide : vous passez votre tour")
                time.sleep(delai_tour)
            n_tour+=1
            continue
        # j'itère jusqu'à ce qu'on considère que le joueur à fait un action
        while peut_jouer:

            indice = -1
            while indice < 0 or indice > len(j_actif.main) - 1:
                try:
                    saisie = int(input(f"Donnez le numéro du domino que vous voulez jouer (de 1 à {len(j_actif.main)}): "))
                    indice = saisie - 1
                    if indice < 0 or indice > len(j_actif.main) - 1:
                        print(f"Veuillez entrer un numéro entre 1 et {len(j_actif.main)}:")
                        time.sleep(delai_tour)
                except ValueError:
                    print("Saisie invalide : entrez un nombre entier.")
                    time.sleep(delai_tour)

            cote = ""
            while cote not in ["d", "g"]:
                cote = input("Où voulez vous le placer (d/g) ?")
                time.sleep(delai_tour)

            if Domino.posable(j_actif.main[indice], plateau, cote):
                domino = j_actif.placer(indice)
                plateau.placer(domino, cote)
                if j_actif.victoire(plateau,pioche,liste_joueurs):
                    print(f"Le joueur {j_actif.nom} a gagné")
                    time.sleep(delai_tour)
                    partie_en_cours = False
                n_tour += 1
                peut_jouer = False
            else:
                print("ce domino ne peut pas être posé ici")
                time.sleep(delai_tour)

if __name__=="__main__":
    execution()