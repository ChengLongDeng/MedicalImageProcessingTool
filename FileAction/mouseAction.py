from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel

class labelModel(QLabel):

    def __init__(self, var, parent=None):
        super(labelModel, self).__init__(parent)
        self.var = var

        self.setMouseTracking(True)                         #跟踪鼠标

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

    def mouseMoveEvent(self, event):
        if self.var.trImageShow.pixmap() is not None:       #判断是否加载图片
            self.valueChanged(event)

        if self.var.coImageShow.pixmap() is not None:       #判断是否加载图片
            self.valueChanged(event)

        if self.var.saImageShow.pixmap() is not None:       #判断是否加载图片
            self.valueChanged(event)

        if self.var.tdImageShow.pixmap() is not None:       #判断是否加载图片
            self.valueChanged(event)
