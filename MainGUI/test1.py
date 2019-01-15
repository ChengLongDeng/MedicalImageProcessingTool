from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QHBoxLayout
from PyQt5.QtGui import QPainterPath, QPainter, QPen, QPolygon
from PyQt5.QtCore import Qt, QRect
import sys

class MyLabel(QLabel):

    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)

        self.x0 = self.y0 = self.x1 = self.y1 = 0
        self.flag = False
        self.rect = QRect()
        self.pFlag = False
        self.chosen_points = QPolygon()

        self.path = QPainterPath()
        self.num = 0

    def wheelEvent(self, event):
        # coor = event.angleDelta() / 8
        # if coor is not None:
        #     self.num = self.num + 1
        #     print('x : %s' % coor.x())
        #     print('y : %s' % coor.y())

        if event.angleDelta().y() < 0:
            print('down')
        else:
            print('up')

    def mouseMoveEvent(self, event):
        if self.flag:                           #记录坐标信息
            self.x1 = event.pos().x()
            self.y1 = event.pos().y()
            self.path.lineTo(self.x1, self.y1)
            self.update()

    def mousePressEvent(self, event):
        self.flag = True
        self.pFlag = True
        self.x0 = event.pos().x()
        self.y0 = event.pos().y()
        self.x1 = self.x0
        self.y1 = self.y0

        self.chosen_points.append(event.pos())

        self.update()

    def mouseReleaseEvent(self, event):
        self.flag = False

    def cusDrawElli(self, qp):
        self.rect.setRect(self.x0, self.y0, self.x1 - self.x0, self.y1 - self.y0)
        qp.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        qp.drawEllipse(self.rect)

    def cusDrawRect(self, qp):
        self.rect.setRect(self.x0, self.y0, self.x1 - self.x0, self.y1 - self.y0)
        qp.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        qp.drawRect(self.rect)

    def cusDrawPoint(self, qp):
        qp.setPen(QPen(Qt.red, 5))

        for pos in self.chosen_points:
            qp.drawPoint(pos)

    def cusDrawPolyline(self, qp):
        qp.setPen(QPen(Qt.red, 2))

        qp.drawPolyline(self.chosen_points)


    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        # self.cusDrawElli(self.qp)

        if self.pFlag:
            self.cusDrawPoint(self.qp)
            self.cusDrawPolyline(self.qp)

        self.qp.end()

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):

        ml = MyLabel()
        self.hLayout = QHBoxLayout()
        self.hLayout.addWidget(ml)

        self.setGeometry(300, 300, 300, 190)
        self.setWindowTitle('Points')
        self.setLayout(self.hLayout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    app.exec_()
