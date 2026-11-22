import sys
import Projet
from Projet import *
from PyQt5.QtWidgets import *
from UI_QtDesigner import Ui_Form



class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()

        Ui_Form.setupUi("interface.ui", self)

        self.ok_btn.clicked.connect(self.valider)

    def valider(self):
        try:
            joueurs = int(self.lineEdit_instructions.text())
        except:
            pass
        Projet.prout=joueurs

        test()





app = QApplication(sys.argv)
window=Fenetre()
window.show()
sys.exit(app.exec_())










