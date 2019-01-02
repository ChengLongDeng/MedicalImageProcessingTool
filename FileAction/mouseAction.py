from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter, QPen
import cv2


class labelModel(QLabel):

    def __init__(self, var, parent=None):
        super(labelModel, self).__init__(parent)
        self.var = var

        self.setMouseTracking(True)                         #跟踪鼠标
        self.setFocusPolicy(Qt.ClickFocus)                  #通过单击获取焦点

        self.x0 = self.x1 = self.y0 = self.y1 = 0
        self.flag = False
        self.rect = QRect()
        self.point0 = QPoint(self.x0, self.y0)
        self.point1 = QPoint(self.x1, self.y1)

    def valueChanged(self, event):

        self.setCursor(Qt.CrossCursor)  # 鼠标指针显示为十字交叉
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

        self.rect.setRect(self.x0, self.y0, self.x1 - self.x0, self.y1 - self.y0)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.drawRect(self.rect)
        # self.var.imagePixmap.save(self.var.im_path)


    def mouseMoveEvent(self, event):        #鼠标移动事件
        print('move')
        if self.var.trImageShow.pixmap():       #判断是否加载图片
            self.valueChanged(event)
            # self.cusDrawRect()

        if self.var.coImageShow.pixmap():       #判断是否加载图片
            self.valueChanged(event)

        if self.var.saImageShow.pixmap():       #判断是否加载图片
            self.valueChanged(event)

        if self.var.tdImageShow.pixmap():       #判断是否加载图片
            self.valueChanged(event)

        if self.flag:           #记录坐标信息
            self.x1 = event.pos().x()
            self.y1 = event.pos().y()
            self.update()

    def mousePressEvent(self, event):   #鼠标按下事件
        print('press')
        if self.var.trImageShow.pixmap():  # 判断是否加载图片
            self.flag = True
            self.x0 = event.pos().x()
            self.y0 = event.pos().y()
            self.x1 = self.x0
            self.y1 = self.y0
            self.update()

    def mouseReleaseEvent(self, event): #鼠标释放事件
        self.flag = False
        print('release')

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:     #小键盘和大键盘的回车键
            print('enterPressEvent')
            print(self.point0)
            print(self.point1)
            cv2.rectangle(self.var.img, (self.x0, self.y0), (self.x1, self.y1), (0, 255, 0), 1)
            cv2.imwrite(self.var.im_path, self.var.img)

    def paintEvent(self, event):        #套索工具
        print('paintEvent')
        super().paintEvent(event)

        if self.var.trImageShow.pixmap():
            painter = QPainter()
            painter.begin(self)
            self.cusDrawRect(painter)     #矩形套索
            painter.end()



        # if self.var.trImageShow.pixmap() is not None:       #判断是否加载图片
        #     self.cusDrawRect()     #矩形套索
        #
        # if self.var.coImageShow.pixmap() is not None:       #判断是否加载图片
        #     self.cusDrawRect()
        #
        # if self.var.saImageShow.pixmap() is not None:       #判断是否加载图片
        #     self.cusDrawRect()
        #
        # if self.var.tdImageShow.pixmap() is not None:       #判断是否加载图片
        #     self.cusDrawRect()

