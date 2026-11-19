import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

height=800
width=800


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PyQt Dominos")
window.setGeometry(600 , 100 , 800 , 800)


quit_button = QPushButton("Quit", window)
quit_button.setGeometry(100 , 100 , 120 , 30)
quit_button.clicked.connect(app.quit)

label=QLabel("DOMINOS",window)
label.setStyleSheet("font-size: 60px; font-weight: ;100;")
label.adjustSize()
label.setAlignment(Qt.AlignCenter)

window.show()
sys.exit(app.exec_())