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
        self.spn_step = 2
        self.coord_step = 1
        self.spn = spn
        self.cords = cords
        self.map_file = 'map.png'
        self.events = []
        uic.loadUi('main.ui', self)
        self.find_button.clicked.connect(self.find_object)
        self.type_choosing.currentTextChanged.connect(self.on_combobox_changed)
        get_map(self.cords, self.spn, str(self.type_choosing.currentText()))
        self.show_picture()

    def show_picture(self):
        self.pixmap = QPixmap(self.map_file)
        self.picture.setPixmap(self.pixmap)

    def find_object(self):
        data = get_map_by_request(self.user_request, str(self.type_choosing.currentText()))
        self.cords = data[0]
        self.spn = data[1]
        self.show_picture()

    def keyPressEvent(self, event):
        x = float(self.cords[0])
        y = float(self.cords[1])
        self.spn = float(self.spn)
        if event.key() == Qt.Key_PageDown:
            if self.spn - self.spn_step >= 0.0:
                self.spn -= self.spn_step
                get_map(self.cords, str(self.spn), str(self.type_choosing.currentText()))
                self.show_picture()
                if self.spn * 0.1 > 0.000001:
                    self.coord_step = self.spn * 0.1
        if event.key() == Qt.Key_PageUp:
            if self.spn + self.spn_step <= 90.0:
                self.spn += self.spn_step
                get_map(self.cords, str(self.spn), str(self.type_choosing.currentText()))
                self.show_picture()
                if self.spn * 0.1 > 0.000001:
                    self.coord_step = self.spn * 0.1
        if event.key() == Qt.Key_Up:
            if float(self.cords[1]) + self.coord_step <= 87:
                self.setFocus()
                y += self.coord_step
                self.cords[1] = str(y)
                get_map(self.cords, str(self.spn), str(self.type_choosing.currentText()))
                self.show_picture()
        if event.key() == Qt.Key_Down:
            if float(self.cords[1]) - self.coord_step >= -87:
                self.setFocus()
                y -= self.coord_step
                self.cords[1] = str(y)
                get_map(self.cords, str(self.spn), str(self.type_choosing.currentText()))
                self.show_picture()
        if event.key() == Qt.Key_Right:
            if float(self.cords[0]) + self.coord_step < 179:
                self.setFocus()
                x += self.coord_step
                self.cords[0] = str(x)
                get_map(self.cords, str(self.spn), str(self.type_choosing.currentText()))
                self.show_picture()
        if event.key() == Qt.Key_Left:
            if float(self.cords[0]) - self.coord_step > -179:
                self.setFocus()
                x -= self.coord_step
                self.cords[0] = str(x)
                get_map(self.cords, str(self.spn), str(self.type_choosing.currentText()))
                self.show_picture()

    def on_combobox_changed(self):
        get_map(self.cords, self.spn, str(self.type_choosing.currentText()))
        self.show_picture()


if __name__ == '__main__':
    start_cords = ['0', '0']
    start_spn = '90'
    app = QApplication(sys.argv)
    ex = MyWidget(start_cords, start_spn)
    ex.show()
    sys.exit(app.exec_())
