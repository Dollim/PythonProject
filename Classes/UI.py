import sys
from PyQt5.QtWidgets import QApplication,QWidget

class MyWindow(QWidget):
    def __init__(self,win):
        super().__init__()
        self.win=win
    def build(self):
        self.win.setWindowTitle("PyQt 5")
        self.win.setGeometry(100,100,400,150)

    def change_color(self):
        self.win.setStyleSheet("background : red;")

if __name__=="__main__":
    app = QApplication(sys.argv)
    root=QWidget()
    mywin=MyWindow(root)
    root.show()
    mywin.build()
    mywin.change_color()

    sys.exit(app.exec_())