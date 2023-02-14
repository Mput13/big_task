# import sys
#
# from PyQt5 import uic
# from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QTimeEdit, QPushButton, QListWidget, QLineEdit
#
#
# class MyWidget(QMainWindow):
#     timeEdit: QTimeEdit
#     calendarWidget: QCalendarWidget
#     lineEdit: QLineEdit
#     pushButton: QPushButton
#     listWidget: QListWidget
#
#     def __init__(self):
#         super().__init__()
#         self.events = []
#         uic.loadUi('test.ui', self)
#         self.pushButton.clicked.connect(self.crete_event)
#
#     def crete_event(self):
#         event = f'{self.calendarWidget.selectedDate().toPyDate()} {self.timeEdit.time().toPyTime()} - {self.lineEdit.text()}'
#         self.events.append(event)
#         self.listWidget.clear()
#         temp = sorted(self.events)
#         for i in temp:
#             self.listWidget.addItem(i)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyWidget()
#     ex.show()
#     sys.exit(app.exec_())
print('я негр')