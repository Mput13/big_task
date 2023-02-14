import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QComboBox

from work_with_api import get_map


class MyWidget(QMainWindow):
    user_request: QLineEdit
    find_button: QPushButton
    type_choosing: QComboBox
    picture: QLabel

    def __init__(self, cords, spn):
        super().__init__()
        self.spn = spn
        self.cords = cords
        self.map_file = 'map.png'
        self.events = []
        uic.loadUi('main.ui', self)
        self.find_button.clicked.connect(self.show_picture)

    def show_picture(self):
        get_map(self.cords, self.spn)
        self.pixmap = QPixmap(self.map_file)
        self.picture.setPixmap(self.pixmap)


if __name__ == '__main__':
    cords = input().split()
    spn = input().split()
    app = QApplication(sys.argv)
    ex = MyWidget(cords, spn)
    ex.show()
    sys.exit(app.exec_())
