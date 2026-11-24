from Classes.joueur import*

#je sépare bien l'IA de projet car on prévoit d'en faire plusieurs


def jouer(joueur: Joueur, plateau, pioche, liste_joueurs, coup):

    partie_en_cours = True

    if coup is None:
        print(f"{joueur.nom} (IA) ne peut pas jouer et pioche.")
        domino_pioche = pioche.piocher()
        if domino_pioche is not None:
            joueur.main.append(domino_pioche)
        else:
            print("pioche vide : l'IA passe son tour")
        return partie_en_cours

    indice, cote = coup
    domino = joueur.placer(indice)
    plateau.placer(domino, cote)
    print(f"{joueur.nom} (IA) pose {domino} à {'droite' if cote == 'd' else 'gauche'}.")

    if joueur.victoire(plateau, pioche, liste_joueurs):
        print(f"Le joueur {joueur.nom} (IA) a gagné")
        partie_en_cours = False

    return partie_en_cours


def ia_random(joueur: Joueur, plateau, pioche, liste_joueurs):
    liste_des_coups = Joueur.coups_possibles(joueur, plateau)
    coup = None
    if liste_des_coups:
        indice, cote = random.choice(liste_des_coups)  #oui y'a une fonction choice dans random (pratique !)
        coup = (indice, cote)
    return jouer(joueur, plateau, pioche, liste_joueurs, coup)

def ia_gloutonne(joueur: Joueur, plateau, pioche, liste_joueurs):
    liste_des_coups = Joueur.coups_possibles(joueur, plateau)
    meilleur_coup = None
    if liste_des_coups:
        meilleur_coup = liste_des_coups[0]
        meilleur_score = joueur.main[meilleur_coup[0]].score()

        for coup in liste_des_coups[1:]:
            score = joueur.main[coup[0]].score()
            if score > meilleur_score:
                meilleur_score = score
                meilleur_coup = coup
    return jouer(joueur, plateau, pioche, liste_joueurs, meilleur_coup)

STRATEGIES_IA = {
    "gloutonne": ia_gloutonne,
    "random": ia_random
}





