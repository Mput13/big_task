import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QComboBox

from work_with_api import get_map, get_map_by_request


class MyWidget(QMainWindow):
    user_request: QLineEdit
    find_button: QPushButton
    type_choosing: QComboBox
    picture: QLabel

    def __init__(self, cords: [str, str], spn: str):
        super().__init__()
        self.spn_step = 3
        self.coord_step = 3
        self.spn = spn
        self.cords = cords
        self.map_file = 'map.png'
        self.events = []
        uic.loadUi('main.ui', self)
        self.find_button.clicked.connect(self.find_object)
        get_map(self.cords, self.spn)
        self.show_picture()

    def show_picture(self):
        self.pixmap = QPixmap(self.map_file)
        self.picture.setPixmap(self.pixmap)

    def find_object(self):
        data = get_map_by_request(self.user_request)
        self.cords = data[0]
        self.spn = data[1]
        self.show_picture()

    def keyPressEvent(self, event):
        x = float(self.cords[0])
        y = float(self.cords[1])
        if event.key() == Qt.Key_PageDown:
            if self.spn - self.spn_step >= 0:
                self.spn -= self.spn_step
                get_map(self.cords, self.spn)
                self.show_picture()
        if event.key() == Qt.Key_PageUp:
            if self.spn + self.spn_step <= 90:
                self.spn += self.spn_step
                get_map(self.cords, self.spn)
                self.show_picture()
        if event.key() == Qt.Key_Up:
            y += self.coord_step
            get_map(self.cords, self.spn)
            self.show_picture()
        if event.key() == Qt.Key_Down:
            y -= self.coord_step
            get_map(self.cords, self.spn)
            self.show_picture()
        if event.key() == Qt.Key_Right:
            x += self.coord_step
            get_map(self.cords, self.spn)
            self.show_picture()
        if event.key() == Qt.Key_Left:
            x -= self.coord_step
            get_map(self.cords, self.spn)
            self.show_picture()


if __name__ == '__main__':
    start_cords = ['20.012', '15.0124']
    start_spn = '9'
    app = QApplication(sys.argv)
    ex = MyWidget(start_cords, start_spn)
    ex.show()
    sys.exit(app.exec_())
