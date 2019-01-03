from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QDesktopWidget
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPainter, QPen, QGuiApplication, QImage, QPixmap
from PyQt5.Qt import Qt
import cv2, sys

class myLabel(QLabel):
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    flag = False

    def mousePressEvent(self, event):
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()

    def mouseReleaseEvent(self, event):
        self.flag = False

    def mouseMoveEvent(self, event):
        if self.flag:
            self.x1 = event.x()
            self.y1 = event.y()
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        rect = QRect(self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0))
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
        painter.drawRect(rect)

        # desk = qApp.screens().at(0).grabWindow(QDesktopWidget().winId(), rect.left(),
        #     rect.top(),
        #     rect.width(),
        #     rect.height()).toImage())

        pqscreen = QGuiApplication.primaryScreen()
        pixmap2 = pqscreen.grabWindow(QGuiApplication.screens()[0].winId(), rect.left(), rect.top(), rect.width(), rect.height())
        pixmap2.save('/Users/dengchenglong/images/555.png')

        # pixmap2 = self.grab(QGuiApplication.screens()[0], rect.left(), rect.top(), rect.width(), rect.height())
        # pixmap2.save('/Users/dengchenglong/images/555.png')

        screen = QGuiApplication.screens()
        print(QWidget.winId(self))
        print(screen)

class Example(QWidget):
    def __init__(self):
        super.__init__()
        self.initUI()

    def initUI(self):
        self.resize(675, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--opencv、PyQt5的小小融合')

        self.lb = myLabel(self)
        self.lb.setGeometry(QRect(140, 30, 511, 241))

        img = cv2.imread('/Users/dengchenglong/images/11111111.png')
        height, width, bytesPerComponent = img.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(QImg)

        self.lb.setPixmap(pixmap)
        self.lb.setCursor(Qt.CrossCursor)

        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())