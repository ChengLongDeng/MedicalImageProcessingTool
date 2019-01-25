from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QHBoxLayout
from PyQt5.QtGui import QPainterPath, QPainter, QPen, QPolygon, QImage, QPixmap
from PyQt5.QtCore import Qt, QRect, pyqtSignal
import sys, cv2

from PIL import Image
from PIL.ImageQt import ImageQt
from resizeimage import resizeimage

class MyLabel(QLabel):

    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)
        self.clicked = pyqtSignal()

        self.x0 = self.y0 = self.x1 = self.y1 = 0
        self.flag = False
        self.rect = QRect()
        self.pFlag = False
        self.chosen_points = QPolygon()

        self.path = QPainterPath()
        self.num = 0

    def wheelEvent(self, event):

        if event.angleDelta().y() < 0:
            print('down')
            self.narrowImageSize()
        else:
            print('up')
            self.enlargeImageSize()

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

        self.clicked.emit()

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


    # def paintEvent(self, event):
    #     self.qp = QPainter()
    #     self.qp.begin(self)
    #     # self.cusDrawElli(self.qp)
    #
    #     if self.pFlag:
    #         self.cusDrawPoint(self.qp)
    #         self.cusDrawPolyline(self.qp)
    #
    #     self.qp.end()

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.InitUI()

    def enlargeImageSize(self):
        img = cv2.resize(self.img, (0, 0), fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('/Users/dengchenglong/images/000133_01_01_107——33.png', img)

    # 缩小图片
    def narrowImageSize(self):
        img = cv2.resize('/Users/dengchenglong/images/000133_01_01_107——11.png', None, -2, -2, interpolation=cv2.INTER_AREA)
        cv2.imwrite('/Users/dengchenglong/images/000133_01_01_107——11.png', img)

    def readImageByCv(self, imgDir):
        # self.img = cv2.imread(imgDir)
        # height, width, bytesPerComponent = self.img.shape
        # bytesPerLine = 3 * width
        # cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB, self.img)  # 将图像从一个颜色空间转换为另一个颜色空间
        # QImg = QImage(self.img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        # return QImg

        image = Image.open(imgDir)
        imageqt = ImageQt(image)
        qimage = QImage(imageqt)
        image.show()
        return qimage

    def readImage(self):
        # self.ml.setPixmap(QPixmap.fromImage(self.readImageByCv('/Users/dengchenglong/images/000001_03_01_088_22.png')))

        self.ml.setPixmap(QPixmap(self.readImageByCv('/Users/dengchenglong/images/000001_03_01_088_22.png')))

    def response(self):
        print('mouse press')

    def InitUI(self):

        self.ml = MyLabel()
        self.ml.clicked.connect(self.response)
        # self.readImage()
        # self.enlargeImageSize()
        self.hLayout = QHBoxLayout()
        self.hLayout.addWidget(self.ml)

        self.setGeometry(300, 300, 300, 190)
        self.setWindowTitle('Points')
        self.setLayout(self.hLayout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    app.exec_()
