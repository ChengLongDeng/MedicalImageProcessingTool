from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PyQt5.QtGui import QPainter, QPainterPath
from PyQt5.QtCore import QSize, QPoint, pyqtSignal
import sys

class Drawer(QWidget):
    newPoint = pyqtSignal(QPoint)
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.path = QPainterPath()
        self.path2 = QPainterPath()

        self.x0 = self.y0 = self.x1 = self.y1 = 0
        self.flag = False

    def paintEvent(self, event):
        print('paint')
        painter = QPainter(self)

        rx = int((self.x1 - self.x0) / 2)
        ry = int((self.y1 - self.y0) / 2)

        self.path2.addEllipse(100, 200, rx, ry)

        # painter.drawPath(self.path)
        painter.drawPath(self.path2)

    def mousePressEvent(self, event):
        print('press')
        self.path.moveTo(event.pos())

        self.flag = True
        self.x0 = event.pos().x()
        self.y0 = event.pos().y()
        self.x1 = self.x0
        self.y1 = self.y0
        self.update()

    def mouseReleaseEvent(self, event):
        self.flag = False

    def mouseMoveEvent(self, event):
        print('move')
        self.path.lineTo(event.pos())
        self.newPoint.emit(event.pos())

        if self.flag:  # 记录坐标信息
            self.x1 = event.pos().x()
            self.y1 = event.pos().y()
            self.update()

    def sizeHint(self):
        return QSize(400, 400)

class MyWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QVBoxLayout())
        label = QLabel(self)
        drawer = Drawer(self)
        drawer.newPoint.connect(lambda p: label.setText('Coordinates: ( %d : %d )' % (p.x(), p.y())))
        self.layout().addWidget(label)
        self.layout().addWidget(drawer)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())