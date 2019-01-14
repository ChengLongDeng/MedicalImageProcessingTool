from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter, QPen, QPixmap, QPolygon, QPainterPath
import cv2, numpy
from FileAction.readImageByCV import readImage
import MainGUI.InformationShowManager as ISM


class labelModel(QLabel):

    def __init__(self, var, parent=None):
        super(labelModel, self).__init__(parent)
        self.var = var

        self.setMouseTracking(True)                         #跟踪鼠标
        self.setFocusPolicy(Qt.ClickFocus)                  #通过单击获取焦点

        self.var.x0 = self.var.x1 = self.var.y0 = self.var.y1 = 0

        self.rect = QRect()             #矩形模板
        self.var.chosen_points = QPolygon() #多边形模板
        self.path = QPainterPath()      #路径模板

        self.flag = False               #判断鼠标是否按下
        self.polyFlag = False           #选择多边形套索时，判断鼠标属否按下
        self.var.rectFlag = False       #判断是否选择矩形套索
        self.var.elliFlag = False       #判断是否选择椭圆形套索
        self.var.polyFlag = False       #判断是否选择多边形套索

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

    #画矩形
    def cusDrawRect(self, painter):
        self.rect.setRect(self.var.x0, self.var.y0, self.var.x1 - self.var.x0, self.var.y1 - self.var.y0)
        painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
        painter.drawRect(self.rect)

    #画圆形
    def cusDrawElli(self, painter):
        self.rect.setRect(self.var.x0, self.var.y0, self.var.x1 - self.var.x0, self.var.y1 - self.var.y0)
        painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
        painter.drawEllipse(self.rect)

    #画点
    def cusDrawPoint(self, qp):
        qp.setPen(QPen(Qt.red, 5))
        for pos in self.var.chosen_points:
            qp.drawPoint(pos)

    #画多边形
    def cusDrawPolyline(self, qp):
        qp.setPen(QPen(Qt.red, 1))
        qp.drawPolyline(self.var.chosen_points)

    def isDraw(self):
        if self.var.rectFlag is True or self.var.elliFlag is True or self.var.polyFlag is True:

            self.setCursor(Qt.CrossCursor)  # 鼠标指针显示为十字交叉
            painter = QPainter()
            painter.begin(self)

            if self.var.rectFlag is True:
                self.cusDrawRect(painter)  # 矩形套索
            if self.var.elliFlag is True:
                self.cusDrawElli(painter)
            if self.var.polyFlag is True:
                if self.polyFlag:
                    self.cusDrawPoint(painter)
                    self.cusDrawPolyline(painter)

            painter.end()

    def statusChanged(self, event):
        self.flag = True
        self.polyFlag = True
        self.var.x0 = event.pos().x()
        self.var.y0 = event.pos().y()
        self.var.x1 = self.var.x0
        self.var.y1 = self.var.y0
        self.var.chosen_points.append(event.pos())
        self.update()

    def mouseMoveEvent(self, event):            #鼠标移动事件
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
            self.path.lineTo(self.var.x1, self.var.y1)  #多边形路径
            self.update()

    def mousePressEvent(self, event):       #鼠标按下事件

        if self.var.trImageShow.pixmap():   # 判断是否加载图片
            self.statusChanged(event)

        if self.var.coImageShow.pixmap():       #判断是否加载图片
            self.statusChanged(event)

        if self.var.saImageShow.pixmap():       #判断是否加载图片
            self.statusChanged(event)

        if self.var.tdImageShow.pixmap():       #判断是否加载图片
            self.statusChanged(event)

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
                cv2.rectangle(self.var.img, (w0, h0), (w1, h1), (0, 255, 0), 1)     # 在图像上画矩形
                cv2.imwrite(self.var.im_path, self.var.img)

                self.var.imagePixmap = QPixmap.fromImage(readImage(self.var, self.var.im_path))
                ISM.openImageLayout(self.var, self.var.imagePixmap)                 # 显示结果

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
                ISM.openImageLayout(self.var, self.var.imagePixmap)  # 显示结果

        if self.var.polyFlag is True:

            if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:  # 小键盘和大键盘的回车键

                temp = []

                for pos in self.var.chosen_points:
                    x = int((float(self.var.width) / 450) * pos.x())
                    y = int((float(self.var.height) / 400) * pos.y())
                    temp.append([x, y])

                points = numpy.array(temp, numpy.int32)
                points = points.reshape(-1, 1, 2)

                cv2.polylines(self.var.img, [points], True, (0, 255, 0))
                cv2.imwrite(self.var.im_path, self.var.img)

                self.var.imagePixmap = QPixmap.fromImage(readImage(self.var, self.var.im_path))
                ISM.openImageLayout(self.var, self.var.imagePixmap)  # 显示结果

                self.var.chosen_points.clear()

    def paintEvent(self, event):        #套索工具
        super().paintEvent(event)

        if self.var.trImageShow.pixmap():
            self.isDraw()
        if self.var.coImageShow.pixmap():
            self.isDraw()

        if self.var.saImageShow.pixmap():
            self.isDraw()

        if self.var.tdImageShow.pixmap():
            self.isDraw()

