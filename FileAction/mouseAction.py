from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter, QPen, QPixmap
import cv2
from FileAction.readImageByCV import readImage
from MainGUI.InformationShowManager import *


class labelModel(QLabel):

    def __init__(self, var, parent=None):
        super(labelModel, self).__init__(parent)
        self.var = var

        self.setMouseTracking(True)                         #跟踪鼠标
        self.setFocusPolicy(Qt.ClickFocus)                  #通过单击获取焦点

        self.var.x0 = self.var.x1 = self.var.y0 = self.var.y1 = 0
        self.flag = False
        self.rect = QRect()

        self.var.rectFlag = False
        self.var.elliFlag = False

    def valueChanged(self, event):

        self.var.xslid.setValue(event.pos().x())  # 显示在滑动条上
        self.var.yslid.setValue(event.pos().y())

        self.var.xslid.setMaximum(self.var.width)
        self.var.yslid.setMaximum(self.var.height)
        # var.zslid.setMaximum(512)
        self.var.xspan.setRange(0, self.var.width)
        self.var.yspan.setRange(0, self.var.height)
        # var.zspan.setRange(0, 512)

        # 像素值显示
        self.var.rspan.setRange(self.var.img.min(), self.var.img.max())
        self.var.gspan.setRange(self.var.img.min(), self.var.img.max())
        self.var.bspan.setRange(self.var.img.min(), self.var.img.max())

        self.var.rspan.setValue(self.var.img[event.pos().x()][event.pos().y()][2])
        self.var.gspan.setValue(self.var.img[event.pos().x()][event.pos().y()][1])
        self.var.bspan.setValue(self.var.img[event.pos().x()][event.pos().y()][0])

        # print(self.var.img[event.pos().x()][event.pos().y()])

    def cusDrawRect(self, painter):

        self.rect.setRect(self.var.x0, self.var.y0, self.var.x1 - self.var.x0, self.var.y1 - self.var.y0)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.drawRect(self.rect)

    def cusDrawElli(self, painter):
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))

        c_x = int(self.var.x0 + (self.var.x1 - self.var.x0) / 2)
        c_y = int(self.var.y0 + (self.var.y1 - self.var.y0) / 2)

        center = QPoint(c_x, c_y)

        rx = int((self.var.x1 - self.var.x0) / 2)
        ry = int((self.var.y1 - self.var.y0) / 2)

        painter.drawEllipse(center, rx, ry)

    def mouseMoveEvent(self, event):            #鼠标移动事件
        print('move')
        if self.var.trImageShow.pixmap():       #判断是否加载图片
            self.valueChanged(event)

        if self.var.coImageShow.pixmap():       #判断是否加载图片
            self.valueChanged(event)

        if self.var.saImageShow.pixmap():       #判断是否加载图片
            self.valueChanged(event)

        if self.var.tdImageShow.pixmap():       #判断是否加载图片
            self.valueChanged(event)

        if self.flag:                           #记录坐标信息
            self.var.x1 = event.pos().x()
            self.var.y1 = event.pos().y()
            self.update()

    def mousePressEvent(self, event):       #鼠标按下事件
        if self.var.trImageShow.pixmap():   # 判断是否加载图片
            self.flag = True
            self.var.x0 = event.pos().x()
            self.var.y0 = event.pos().y()
            self.var.x1 = self.var.x0
            self.var.y1 = self.var.y0
            self.update()

    def mouseReleaseEvent(self, event): #鼠标释放事件
        self.flag = False

    def keyPressEvent(self, event):
        super().keyPressEvent(event)

        if self.var.rectFlag is True:

            if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:     #小键盘和大键盘的回车键
                w0 = int((float(self.var.width) / 450) * self.var.x0)
                h0 = int((float(self.var.height) / 400) * self.var.y0)
                w1 = int((float(self.var.width) / 450) * self.var.x1)
                h1 = int((float(self.var.height) / 400) * self.var.y1)
                cv2.rectangle(self.var.img, (w0, h0), (w1, h1), (0, 255, 0), 1) #在图像上画矩形
                cv2.imwrite(self.var.im_path, self.var.img)

                self.var.imagePixmap = QPixmap.fromImage(readImage(self.var, self.var.im_path))
                # openImageLayout(self.var, self.var.imagePixmap)  # 打开图像
                self.var.imageShow.setTransverseImagePixmap(self.var.imagePixmap)

        if self.var.elliFlag is True:

            if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:  # 小键盘和大键盘的回车键
                w0 = int((float(self.var.width) / 450) * self.var.x0)
                h0 = int((float(self.var.height) / 400) * self.var.y0)
                w1 = int((float(self.var.width) / 450) * self.var.x1)
                h1 = int((float(self.var.height) / 400) * self.var.y1)

                c_x = w0 + (w1 - w0) / 2
                c_y = h0 + (h1 - h0) / 2

                cv2.ellipse(self.var.img, (int(c_x), int(c_y)), (int((w1 - w0) / 2), int((h1 - h0) / 2)), 0.0, 0.0, 360.0, (0, 255, 0), 1)  # 在图像上画椭圆形
                cv2.imwrite(self.var.im_path, self.var.img)

                self.var.imagePixmap = QPixmap.fromImage(readImage(self.var, self.var.im_path))
                # openImageLayout(self.var, self.var.imagePixmap)  # 打开图像
                self.var.imageShow.setTransverseImagePixmap(self.var.imagePixmap)

    def paintEvent(self, event):        #套索工具
        super().paintEvent(event)
        print('paint')

        if self.var.rectFlag is True or self.var.elliFlag is True:

            self.setCursor(Qt.CrossCursor)  # 鼠标指针显示为十字交叉

            if self.var.trImageShow.pixmap():
                painter = QPainter()
                painter.begin(self)

                if self.var.rectFlag is True:
                    self.cusDrawRect(painter)     #矩形套索
                if self.var.elliFlag is True:
                    self.cusDrawElli(painter)

                painter.end()

            if self.var.coImageShow.pixmap():
                painter = QPainter()
                painter.begin(self)
                self.cusDrawRect(painter)     #矩形套索
                painter.end()

            if self.var.saImageShow.pixmap():
                painter = QPainter()
                painter.begin(self)
                self.cusDrawRect(painter)     #矩形套索
                painter.end()

            if self.var.tdImageShow.pixmap():
                painter = QPainter()
                painter.begin(self)
                self.cusDrawRect(painter)     #矩形套索
                painter.end()

