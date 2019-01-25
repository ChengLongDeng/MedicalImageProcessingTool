from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter, QPolygon, QPainterPath
import ImageProcessingAction.LabelResponse.drawingGraphics as DG
import ImageProcessingAction.LabelResponse.resizeImage as RI
import ImageProcessingAction.Preprocessing.denoisingMethod as DM
import cv2

class labelModel(QLabel):

    def __init__(self, var, parent=None):
        super(labelModel, self).__init__(parent)
        self.var = var

        self.setMouseTracking(True)                         # 跟踪鼠标
        self.setFocusPolicy(Qt.ClickFocus)                  # 通过单击获取焦点

        self.var.x0 = self.var.x1 = self.var.y0 = self.var.y1 = 0
        self.img_aspect_ratio = float(self.height()) / self.width()  # Label纵横比
        self.var.GSKernel = 3                               # 高斯核大小

        self.var.rect = QRect()                 # 矩形模板
        self.var.chosen_points = QPolygon()     # 多边形模板
        self.path = QPainterPath()              # 路径模板

        self.flag = False                       # 判断鼠标是否按下
        self.var.GSFlag = False                 # 判断是否进行高斯滤波
        self.var.rectFlag = False               # 判断是否选择矩形套索
        self.var.elliFlag = False               # 判断是否选择椭圆形套索
        self.var.polyFlag = False               # 判断是否选择多边形套索
        self.var.enlargeFlag = False            # 判断是否放大图像
        self.var.narrowFlag = False             # 判断是否缩小图像

    # 在状态栏上显示
    def valueChanged(self, event):

        self.var.size.setText('(%d × %d)' % (self.var.width, self.var.height))                          # 状态栏显示图像大小
        self.var.location.setText('(x : %d, y : %d, z : %d)' % (event.pos().x(), event.pos().y(), 0))   # 鼠标位置信息

        if event.pos().x() >= self.var.width or event.pos().y() >= self.var.height:     # 鼠标所在位置超过图像大小
            self.var.pixel.setText('(r : %d, g : %d, b : %d)' % (0, 0, 0))
        else:
            self.var.pixel.setText('(r : %d, g : %d, b : %d)' % (self.var.img[event.pos().y()][event.pos().x()][2], self.var.img[event.pos().y()][event.pos().x()][1], self.var.img[event.pos().y()][event.pos().x()][0]))  # 鼠标所在位置像素信息

    # 判断是否选择画笔
    def isDraw(self):
        if self.var.rectFlag is True or self.var.elliFlag is True or self.var.polyFlag is True:

            self.setCursor(Qt.CrossCursor)  # 鼠标指针显示为十字交叉
            painter = QPainter()
            painter.begin(self)

            if self.var.rectFlag is True:
                DG.cusDrawRect(self.var, painter)             # 矩形套索
            if self.var.elliFlag is True:
                DG.cusDrawElli(self.var, painter)             # 椭圆形套索
            if self.var.polyFlag is True:
                if self.polyFlag:
                    DG.cusDrawPoint(self.var, painter)        # 多边形点
                    DG.cusDrawPolyline(self.var, painter)     # 多边形线

            painter.end()

    def statusChanged(self, event):
        self.flag = True
        self.var.x0 = event.pos().x()
        self.var.y0 = event.pos().y()
        self.var.x1 = self.var.x0
        self.var.y1 = self.var.y0
        self.var.chosen_points.append(event.pos())
        self.update()

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        if self.var.trImageShow.pixmap():       # 判断是否加载图片
            self.valueChanged(event)

        if self.var.coImageShow.pixmap():       # 判断是否加载图片
            self.valueChanged(event)

        if self.var.saImageShow.pixmap():       # 判断是否加载图片
            self.valueChanged(event)

        if self.var.tdImageShow.pixmap():       # 判断是否加载图片
            self.valueChanged(event)

        if self.flag:                           # 记录坐标信息
            self.var.x1 = event.pos().x()
            self.var.y1 = event.pos().y()
            self.path.lineTo(self.var.x1, self.var.y1)  # 多边形路径
            self.update()

    # 鼠标按下事件
    def mousePressEvent(self, event):

        if self.var.trImageShow.pixmap():       # 判断是否加载图片
            self.statusChanged(event)

        if self.var.coImageShow.pixmap():       # 判断是否加载图片
            self.statusChanged(event)

        if self.var.saImageShow.pixmap():       # 判断是否加载图片
            self.statusChanged(event)

        if self.var.tdImageShow.pixmap():       # 判断是否加载图片
            self.statusChanged(event)

        if self.var.trFlag is False or self.var.coFlag is False or self.var.saFlag is False or self.var.tdFlag is False:    #判断是否双击
            if self.var.enlargeFlag:
                RI.enlargeImage(self.var, self, 50, 50)   # 放大图像
            elif self.var.narrowFlag:
                RI.narrowImage(self.var, self, -50, -50)    # 缩小图像


    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        self.flag = False

    # 按键事件
    def keyPressEvent(self, event):
        super().keyPressEvent(event)

        if self.var.rectFlag is True:   # 画矩形

            if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:     #小键盘和大键盘的回车键
                DG.drawRectByOpenCV(self.var, self)

        if self.var.elliFlag is True:   # 画椭圆形

            if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:  # 小键盘和大键盘的回车键
                DG.drawElliByOpenCV(self.var, self)

        if self.var.polyFlag is True:   # 画多边形

            if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:  # 小键盘和大键盘的回车键
                DG.drawPolyByOpenCV(self.var, self)

        if self.var.GSFlag is True:     # 高斯滤波

            if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:  # 小键盘和大键盘的回车键
                cv2.imwrite(self.var.img)

    # 滚轮事件
    def wheelEvent(self, event):
        if self.var.GSFlag:
            DM.GaussianDenoisingKernel(self.var, event)

    # 绘画事件
    def paintEvent(self, event):        # 套索工具
        super().paintEvent(event)

        if self.var.trImageShow.pixmap():
            self.isDraw()
        if self.var.coImageShow.pixmap():
            self.isDraw()
        if self.var.saImageShow.pixmap():
            self.isDraw()
        if self.var.tdImageShow.pixmap():
            self.isDraw()

