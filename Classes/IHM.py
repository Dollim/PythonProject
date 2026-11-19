import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("PyQt Dominos")
window.setGeometry(600 , 100 , 800 , 800)


quit_button = QPushButton("Quit", window)
quit_button.setGeometry(100 , 700, 120 , 30)
quit_button.clicked.connect(app.quit)

label=QLabel("DOMINOS",window)
label.setStyleSheet("font-size: 50px; font-weight: ;bold;")
label.adjustSize()
label.move(window.width()//2-label.width()//2,window.height()//10)

n=0
def start():
    global input_text,n
    input_text = QLineEdit(window)
    input_text.setPlaceholderText("Entrez votre nom...")
    input_text.setGeometry(10, 10, 300, 40)
    input_text.show()
    valider_button = QPushButton("Valider", window)
    valider_button.setGeometry(100, 200, 100, 100)
    valider_button.clicked.connect(valider)
    valider_button.show()


def valider():
    print(input_text.text())

start_button = QPushButton("Start", window)
start_button.setGeometry(700 , 700, 120 , 30)
start_button.clicked.connect(start)











window.show()
sys.exit(app.exec_())