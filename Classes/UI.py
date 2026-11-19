import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
"""
class Fenetre(QWidget):
    def __init__(self,w,h):
        super().__init__()
        self.titre=QLabel("Jeu de dominos")
        titre.setStyleSheet("font-size : 60px;font-weight : bold;")
        titre.adjustSize()
        titre.move"""



#window=Fenetr()


def afficher_message():
    label.setText("Bonjour ! Bienvenue dans PyQt5.")

app = QApplication(sys.argv)
fenetre=QWidget()

fenetre.setWindowTitle("Mon premier programme PyQt")
fenetre.resize(400, 200)

label = QLabel("Cliquez sur le bouton")
bouton = QPushButton("Cliquez ici")

# Connexion du bouton à la fonction
bouton.clicked.connect(afficher_message)

fenetre.show()
sys.exit(app.exec_())



