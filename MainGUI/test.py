from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys



class MyLabel(QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)

    def mouseDoubleClickEvent(self, e):
        print
        'mouse double clicked'

    def mousePressEvent(self, e):
        print
        'mousePressEvent'

    def focusInEvent(self, e):
        print
        'focusInEvent'

    def focusOutEvent(self, e):
        print
        'focusOutEvent'

    def moveEvent(self, e):
        print
        'moveEvent'

    def leaveEvent(self, e):  # 鼠标离开label
        print
        'leaveEvent'

    def enterEvent(self, e):  # 鼠标移入label
        print
        'enterEvent'

    def mouseMoveEvent(self, e):
        print
        'mouseMoveEvent'


class TestDialog(QDialog):
    def __init__(self, parent=None):
        super(TestDialog, self).__init__(parent)
        self.statusLabel = MyLabel(self)
        self.statusLabel.setGeometry(QRect(95, 220, 151, 41))
        self.statusLabel.setText("hello label")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = TestDialog()
    dialog.show()