import sys
from PyQt5.QtWidgets import *
from UI_QtDesigner import Ui_Form

app = QApplication(sys.argv)
root = QWidget()
window=Ui_Form()
window.setupUi(root)









root.show()
sys.exit(app.exec_())










