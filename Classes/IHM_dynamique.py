import sys
from Projet import *
from PyQt5.QtWidgets import *
from UI_QtDesigner import Ui_Form


class FenetreJeu(QWidget):

    def __init__(self):
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
        self.ui.start_btn.clicked.connect(self.demarrer_partie)

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

        self.ui.label_victoire.hide()

    def demarrer_partie(self):
        pass

    def valider_saisie(self):
        pass

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
    sys.exit(app.exec_())










