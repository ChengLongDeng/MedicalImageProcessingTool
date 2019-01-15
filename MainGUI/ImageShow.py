from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from FileAction.mouseAction import labelModel

class imageShowManager(QWidget):

    def __init__(self, var):
        super(imageShowManager, self).__init__()
        self.var = var
        self.trFlag = True
        self.coFlag = True
        self.saFlag = True
        self.tdFlag = True

    def createNewModel(self):
        model = labelModel(self.var)        # 新建自定义QLabel
        model.setAlignment(Qt.AlignCenter)
        model.setFixedSize(450, 400)
        imagePa = QPalette()
        imagePa.setColor(QPalette.Window, Qt.black)
        model.setAutoFillBackground(True)
        model.setPalette(imagePa)
        model.setScaledContents(True)

        return model

    def transverseImageShow(self):

        self.var.trImageShow = self.createNewModel()            #新建自定义QLabel
        self.var.trImageShow.mouseDoubleClickEvent = self.trImageEnlarge    #判断是否双击
        return self.var.trImageShow

    def setTransverseImagePixmap(self, imagePixmap):
        return self.var.trImageShow.setPixmap(imagePixmap)

    def trImageEnlarge(self, event=None):           #这里必须加event参数，否则出错
        if self.var.trImageShow.pixmap():  # 判断是否加载图片
            if self.trFlag:
                self.var.coImageShow.setVisible(False)
                self.var.saImageShow.setVisible(False)
                self.var.tdImageShow.setVisible(False)
                self.trFlag = False
            else:
                self.var.coImageShow.setVisible(True)
                self.var.saImageShow.setVisible(True)
                self.var.tdImageShow.setVisible(True)
                self.trFlag = True

    def coronalImageShow(self):

        self.var.coImageShow = self.createNewModel()
        self.var.coImageShow.mouseDoubleClickEvent = self.coImageEnlarge  # 判断是否双击
        return self.var.coImageShow

    def setCoronalImagePixmap(self, imagePixmap):
        return self.var.coImageShow.setPixmap(imagePixmap)

    def coImageEnlarge(self, event=None):
        if self.var.coImageShow.pixmap():  # 判断是否加载图片
            if self.coFlag:
                self.var.trImageShow.setVisible(False)
                self.var.saImageShow.setVisible(False)
                self.var.tdImageShow.setVisible(False)
                self.coFlag = False
            else:
                self.var.trImageShow.setVisible(True)
                self.var.saImageShow.setVisible(True)
                self.var.tdImageShow.setVisible(True)
                self.coFlag = True

    def sagittalImageShow(self):

        self.var.saImageShow = self.createNewModel()
        self.var.saImageShow.mouseDoubleClickEvent = self.saImageEnlarge  # 判断是否双击
        return self.var.saImageShow

    def setSagittalImagePixmap(self, imagePixmap):
        return self.var.saImageShow.setPixmap(imagePixmap)

    def saImageEnlarge(self, event=None):
        if self.var.saImageShow.pixmap():  # 判断是否加载图片
            if self.saFlag:
                self.var.coImageShow.setVisible(False)
                self.var.trImageShow.setVisible(False)
                self.var.tdImageShow.setVisible(False)
                self.saFlag = False
            else:
                self.var.coImageShow.setVisible(True)
                self.var.trImageShow.setVisible(True)
                self.var.tdImageShow.setVisible(True)
                self.saFlag = True

    def tDImageShow(self):

        self.var.tdImageShow = self.createNewModel()
        self.var.tdImageShow.mouseDoubleClickEvent = self.tdImageEnlarge  # 判断是否双击
        return self.var.tdImageShow

    def setTDImagePixmap(self, imagePixmap):
        return self.var.tdImageShow.setPixmap(imagePixmap)

    def tdImageEnlarge(self, event=None):
        if self.var.tdImageShow.pixmap():       #判断是否加载图片
            if self.tdFlag:
                self.var.coImageShow.setVisible(False)
                self.var.saImageShow.setVisible(False)
                self.var.trImageShow.setVisible(False)
                self.tdFlag = False
            else:
                self.var.coImageShow.setVisible(True)
                self.var.saImageShow.setVisible(True)
                self.var.trImageShow.setVisible(True)
                self.tdFlag = True