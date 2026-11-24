import sys
from Projet import *
from PyQt5.QtWidgets import *
from UI_QtDesigner import Ui_Form


class FenetreJeu(QWidget):

    def __init__(self):
        global phase_exec
        super().__init__()

        # Initialisation de l'interface
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Variables du jeu
        self.joueurs = []
        self.plateau = None
        self.pioche = None
        self.liste_joueurs = []

        self.n_tour = 1
        self.indice_domino_selectionne = None
        self.partie_en_cours = False

        # Liste des boutons correspondant aux dominos
        self.boutons_dominos = [
            self.ui.d1_btn,
            self.ui.d2_btn,
            self.ui.d3_btn,
            self.ui.d4_btn,
            self.ui.d5_btn,
            self.ui.d6_btn,
            self.ui.d7_btn
        ]

        # Connexion des boutons
        for i, bouton in enumerate(self.boutons_dominos):
            bouton.clicked.connect(
                lambda checked=False, indice=i:
                    self.selectionner_domino(indice)
            )

        self.ui.pushButton.clicked.connect(
            lambda: self.jouer_domino("d")
        )

        self.ui.pushButton_2.clicked.connect(
            lambda: self.jouer_domino("g")
        )

        self.ui.ok_btn.clicked.connect(self.valider_saisie)

        self.ui.start_btn.clicked.connect(self.demarrer_partie)
        self.ui.label_victoire.hide()
        phase_exec=1


    def demarrer_partie(self):
        self.ui.label_instructions.setStyleSheet("background:27F5F5;color:red;")
        self.ui.label_instructions.setText("Veuillez choisir le nombre de joueurs (2 ou 4) ")

        self.ui.ok_btn.clicked.connect(self.saisie_n)


    def saisie_n(self):
        global n_joueurs,phase_exec
        if phase_exec==1:
            try:
                n_joueurs=int(self.ui.lineEdit_console.text())
                print(n_joueurs)

                self.ui.label_instructions.setStyleSheet("background:white;color:black;")
                self.ui.label_instructions.setText("Voulez-vous des IA? ")
                phase_exec +=1
            except:
                self.ui.label_instructions.setText("Erreur de saisie, choisisez 2 ou 4")

        elif phase_exec==2:
            try:
                n_joueurs = int(self.ui.lineEdit_console.text())
                print(n_joueurs)

                self.ui.label_instructions.setStyleSheet("background:white;color:black;")
                self.ui.label_instructions.setText("Voulez-vous des IA? ")
                phase_exec += 1
            except:
                self.ui.label_instructions.setText("Erreur de saisie, choisisez 2 ou 4")





    def afficher_tour(self):
        pass

    def afficher_main(self):
        pass

    def selectionner_domino(self, indice):
        pass

    def jouer_domino(self, cote):
        pass

    def actualiser_plateau(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = FenetreJeu()
    win.show()
    #app.exec_()
    sys.exit(app.exec_())"""





import sys
import random
from PyQt5 import QtWidgets

from UI_QtDesigner import Ui_Form
from Classes.joueur import Joueur
from Classes.talon import Talon
from Classes.plateau import Plateau


class FenetreJeu(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Configuration
        self.etape = -1
        self.n_joueur = 0
        self.jeu_avec_ia = False
        self.mode = None
        self.taille_main_depart = None

        # Éléments du jeu
        self.joueurs = []
        self.pioche = None
        self.plateau = None
        self.indice_joueur = 0
        self.indice_selectionne = None
        self.jeu_termine = False

        self.boutons_dominos = [
            self.ui.d1_btn,
            self.ui.d2_btn,
            self.ui.d3_btn,
            self.ui.d4_btn,
            self.ui.d5_btn,
            self.ui.d6_btn,
            self.ui.d7_btn
        ]

        # Connexions
        self.ui.start_btn.clicked.connect(self.commencer)
        self.ui.ok_btn.clicked.connect(self.valider_saisie)
        self.ui.lineEdit_console.returnPressed.connect(
            self.valider_saisie
        )

        self.ui.pushButton.clicked.connect(
            lambda: self.placer_selection("d")
        )
        self.ui.pushButton_2.clicked.connect(
            lambda: self.placer_selection("g")
        )

        for i, bouton in enumerate(self.boutons_dominos):
            bouton.clicked.connect(
                lambda checked=False, index=i:
                self.selectionner_domino(index)
            )

        self.ui.ok_btn.setVisible(False)
        self.ui.lineEdit_console.setVisible(False)

        self.ui.label_instructions.setText(
            "Cliquez sur COMMENCER pour lancer une partie."
        )

        self.ui.label_victoire.setText("")

        for bouton in self.boutons_dominos:
            bouton.setVisible(False)

        self.ui.pushButton.setVisible(False)
        self.ui.pushButton_2.setVisible(False)

    # --------------------------------------------------
    # CONFIGURATION DE LA PARTIE
    # --------------------------------------------------

    def commencer(self):
        self.etape = 0

        self.ui.start_btn.setVisible(False)
        self.ui.ok_btn.setVisible(True)
        self.ui.lineEdit_console.setVisible(True)

        self.demander("Combien de joueurs ? (2 ou 4)")

    def demander(self, message):
        self.ui.label_instructions.setText(message)
        self.ui.lineEdit_console.clear()
        self.ui.lineEdit_console.setFocus()

    def valider_saisie(self):
        saisie = self.ui.lineEdit_console.text().strip().lower()

        if self.etape == 0:

            if saisie not in ("2", "4"):
                self.demander("Choisissez 2 ou 4 joueurs.")
                return

            self.n_joueur = int(saisie)
            self.etape = 1

            self.demander("Voulez-vous jouer avec des IA ? (oui/non)")

        elif self.etape == 1:

            if saisie not in ("oui", "non", "o", "n"):
                self.demander("Répondez par oui ou non.")
                return

            self.jeu_avec_ia = saisie in ("oui", "o")

            if self.n_joueur == 2:
                self.etape = 2
                self.demander("Choisissez le mode (7, 8, 9 ou 10).")
            else:
                self.mode = 7
                self.taille_main_depart = 6
                self.etape = 3
                self.demander("Nom du joueur 1 :")

        elif self.etape == 2:

            if saisie not in ("7", "8", "9", "10"):
                self.demander("Choisissez 7, 8, 9 ou 10.")
                return

            self.mode = int(saisie)
            self.taille_main_depart = self.mode
            self.etape = 3

            self.demander("Nom du joueur 1 :")

        elif self.etape == 3:

            if not saisie:
                self.demander("Entrez un nom valide.")
                return

            self.nom_temporaire = saisie

            if self.jeu_avec_ia:
                self.etape = 4
                self.demander(
                    f"{saisie} est-il une IA ? (oui/non)"
                )
            else:
                self.joueurs.append(Joueur(saisie, False))
                self.joueur_suivant()


        elif self.etape == 4:

            print("TEST 1 : entrée dans étape 4", flush=True)

            if saisie not in ("oui", "non", "o", "n"):
                self.demander("Répondez par oui ou non.")

                return

            est_ia = saisie in ("oui", "o")

            print("TEST 2 : valeur IA =", est_ia, flush=True)

            joueur = Joueur(self.nom_temporaire, est_ia)

            print("TEST 3 : joueur créé", flush=True)

            self.joueurs.append(joueur)

            print("TEST 4 : joueur ajouté", flush=True)

            self.joueur_suivant()

            print("TEST 5 : joueur suivant appelé", flush=True)

            return

    def joueur_suivant(self):
        numero = len(self.joueurs) + 1

        if numero <= self.n_joueur:
            self.etape = 3
            self.demander(f"Nom du joueur {numero} :")
        else:
            self.etape = 6
            self.lancer_partie()

    # --------------------------------------------------
    # INITIALISATION ET DISTRIBUTION
    # --------------------------------------------------

    def lancer_partie(self):

        print("TEST 6 : début lancer_partie", flush=True)

        print("TEST 7 : joueurs =", len(self.joueurs), flush=True)

        for j in self.joueurs:
            print(j.nom, j.est_ia, flush=True)

        print("TEST 8 : création du talon", flush=True)

        distribution_valide = False

        while not distribution_valide:

            self.pioche = Talon(self.mode)
            self.plateau = Plateau()

            print("TEST 9 : distribution", flush=True)

            for joueur in self.joueurs:
                joueur.main = []

                for _ in range(self.taille_main_depart):
                    domino = self.pioche.piocher()

                    if domino is not None:
                        joueur.main.append(domino)

            print("TEST 10 : vérification des mains", flush=True)

            distribution_valide = all(
                joueur.main_valide(self.taille_main_depart)
                for joueur in self.joueurs
            )

        print("TEST 11 : attribution de l'ordre", flush=True)

        domino_depart = self.joueurs[0].attribution_ordre(
            self.joueurs, self.mode
        )

        print("TEST 12 : ordre attribué", flush=True)

    # --------------------------------------------------
    # AFFICHAGE
    # --------------------------------------------------

    def actualiser_affichage(self):

        self.ui.label_plateau.setText(str(self.plateau))

        for bouton in self.boutons_dominos:
            bouton.setVisible(False)
            bouton.setEnabled(False)

        if self.jeu_termine:
            return

        joueur = self.joueurs[self.indice_joueur]

        if not joueur.est_ia:
            for i, domino in enumerate(joueur.main[:7]):
                bouton = self.boutons_dominos[i]

                bouton.setText(str(domino))
                bouton.setVisible(True)
                bouton.setEnabled(True)

                if i == self.indice_selectionne:
                    bouton.setStyleSheet(
                        "background-color: lightgreen;"
                    )
                else:
                    bouton.setStyleSheet("")

        self.ui.label_tour.setText(
            f"Tour de {joueur.nom}"
        )

    # --------------------------------------------------
    # GESTION DES TOURS
    # --------------------------------------------------

    def preparer_tour(self):

        while not self.jeu_termine:

            joueur = self.joueurs[self.indice_joueur]

            self.indice_selectionne = None

            # Pioche automatique si aucun coup possible
            while (
                not joueur.peut_encore_jouer(self.plateau)
                and len(self.pioche.talon) > 0
            ):
                domino = self.pioche.piocher()

                if domino is not None:
                    joueur.main.append(domino)

            # Aucun coup possible
            if not joueur.peut_encore_jouer(self.plateau):

                if self.verifier_fin():
                    return

                self.ui.label_instructions.setText(
                    f"{joueur.nom} ne peut pas jouer. "
                    "Il passe son tour."
                )

                self.indice_joueur = (
                    self.indice_joueur + 1
                ) % self.n_joueur

                continue

            self.actualiser_affichage()

            # Tour humain
            if not joueur.est_ia:
                self.etape = 5
                self.ui.label_instructions.setText(
                    f"{joueur.nom}, choisissez un domino."
                    " Vous pouvez aussi saisir son numéro."
                )

                self.ui.ok_btn.setVisible(True)
                self.ui.lineEdit_console.setVisible(True)
                self.ui.lineEdit_console.clear()

                return

            # Tour IA
            else:
                coups = joueur.coups_possibles(self.plateau)

                if not coups:
                    self.indice_joueur = (
                        self.indice_joueur + 1
                    ) % self.n_joueur
                    continue

                indice, cote = random.choice(coups)

                domino = joueur.placer(indice)
                self.plateau.placer(domino, cote)

                self.ui.label_instructions.setText(
                    f"{joueur.nom} joue {domino} "
                    f"à {'droite' if cote == 'd' else 'gauche'}."
                )

                if self.verifier_fin():
                    return

                self.indice_joueur = (
                    self.indice_joueur + 1
                ) % self.n_joueur

    # --------------------------------------------------
    # SÉLECTION D'UN DOMINO
    # --------------------------------------------------

    def selectionner_domino(self, indice):

        joueur = self.joueurs[self.indice_joueur]

        if indice >= len(joueur.main):
            return

        self.indice_selectionne = indice
        domino = joueur.main[indice]

        self.actualiser_affichage()

        self.ui.label_instructions.setText(
            f"Domino sélectionné : {domino}. "
            "Choisissez Droite ou Gauche."
        )

    def selectionner_par_numero(self, saisie):

        if not saisie.isdigit():
            self.ui.label_instructions.setText(
                "Entrez un numéro de domino valide."
            )
            return

        numero = int(saisie)
        joueur = self.joueurs[self.indice_joueur]

        if numero < 1 or numero > len(joueur.main):
            self.ui.label_instructions.setText(
                "Ce numéro n'existe pas dans votre main."
            )
            return

        self.selectionner_domino(numero - 1)

        self.ui.lineEdit_console.clear()

    # --------------------------------------------------
    # PLACEMENT
    # --------------------------------------------------

    def placer_selection(self, cote):

        if self.jeu_termine:
            return

        if self.indice_selectionne is None:
            self.ui.label_instructions.setText(
                "Sélectionnez d'abord un domino."
            )
            return

        joueur = self.joueurs[self.indice_joueur]
        domino = joueur.main[self.indice_selectionne]

        if not domino.posable(self.plateau, cote):
            self.ui.label_instructions.setText(
                "Ce domino ne peut pas être placé de ce côté."
            )
            return

        domino = joueur.placer(self.indice_selectionne)
        self.plateau.placer(domino, cote)

        self.indice_selectionne = None

        self.ui.ok_btn.setVisible(False)
        self.ui.lineEdit_console.setVisible(False)

        if self.verifier_fin():
            return

        self.indice_joueur = (
            self.indice_joueur + 1
        ) % self.n_joueur

        self.preparer_tour()

    # --------------------------------------------------
    # FIN DE PARTIE
    # --------------------------------------------------

    def verifier_fin(self):

        joueur = self.joueurs[self.indice_joueur]

        # Un joueur n'a plus de dominos
        if len(joueur.main) == 0:
            self.terminer_partie(
                f"{joueur.nom} a gagné la partie !"
            )
            return True

        # Vérification du blocage
        if len(self.pioche.talon) == 0:

            personne_ne_peut_jouer = all(
                not j.peut_encore_jouer(self.plateau)
                for j in self.joueurs
            )

            if personne_ne_peut_jouer:

                score_min = min(
                    j.score_main() for j in self.joueurs
                )

                gagnants = [
                    j.nom for j in self.joueurs
                    if j.score_main() == score_min
                ]

                if len(gagnants) == 1:
                    message = (
                        f"{gagnants[0]} gagne ! "
                        "Partie bloquée."
                    )
                else:
                    message = (
                        "Égalité entre : "
                        + ", ".join(gagnants)
                    )

                self.terminer_partie(message)
                return True

        return False

    def terminer_partie(self, message):

        self.jeu_termine = True

        self.ui.label_victoire.setText(message)
        self.ui.label_instructions.setText(message)

        self.ui.ok_btn.setVisible(False)
        self.ui.lineEdit_console.setVisible(False)

        self.ui.pushButton.setVisible(False)
        self.ui.pushButton_2.setVisible(False)

        for bouton in self.boutons_dominos:
            bouton.setVisible(False)

        self.actualiser_affichage()


"""if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    fenetre = FenetreJeu()
    fenetre.show()

    sys.exit(app.exec_())"""


if __name__ == "__main__":
    import faulthandler
    faulthandler.enable()

    app = QtWidgets.QApplication(sys.argv)

    fenetre = FenetreJeu()
    fenetre.show()

    sys.exit(app.exec_())