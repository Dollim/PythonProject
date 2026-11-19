import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton

class MyWindow(QWidget):
    def __init__(self,win):
        super().__init__()
        self.win=win

    def action(self):
        print(self.textbox.text())
    def action_bouton(self):
        self.but.setText("POUSSE")

    def build(self):
        self.win.setWindowTitle("PyQt 5")
        self.win.setGeometry(100,100,400,150)

        self.label=QLabel(self.win)
        self.label.setGeometry(20,30,350,50)
        self.label.setText("PUTE")
        self.label.setStyleSheet("left-padding:50px;font-size : 60px;font-weight : bold")

        self.textbox=QLineEdit(self.win)
        self.textbox.setGeometry(50,100,200,50)
        self.textbox.setStyleSheet("background:black;color:yellow;font-size:28px;")
        self.textbox.textChanged.connect(self.action)

        self.but=QPushButton(self.win)
        self.but.setText("BOUTON")
        self.but.setStyleSheet("color=green;")
        self.but.clicked.connect(self.action_bouton)


    def change_color(self):
        self.win.setStyleSheet("background : red;")

if __name__=="__main__":
    app = QApplication(sys.argv)

    root=QWidget()
    mywin=MyWindow(root)

    mywin.build()
    mywin.change_color()
    root.show()
    sys.exit(app.exec_())