from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from ImageProcessingAction.LabelModel.customLabel import labelModel
from ImageProcessingAction.LabelResponse.doubleMouseClick import settrLabelVisible, setcoLabelVisible, setsaLabelVisible, settDLabelVisible

class imageShowManager(QWidget):

    def __init__(self, var):
        super(imageShowManager, self).__init__()
        self.var = var
        self.var.trFlag = True
        self.var.coFlag = True
        self.var.saFlag = True
        self.var.tdFlag = True

    def createNewModel(self):
        model = labelModel(self.var)        # 新建自定义QLabel
        model.setAlignment(Qt.AlignCenter)
        model.setFixedSize(200, 200)
        imagePa = QPalette()
        imagePa.setColor(QPalette.Window, Qt.black)
        model.setAutoFillBackground(True)
        model.setPalette(imagePa)
        # model.setScaledContents(True)     # 图像自适应Label大小

        return model

    # 显示原图像
    def transverseImageShow(self):

        self.var.trImageShow = self.createNewModel()                                      # 新建自定义QLabel
        self.var.trImageShow.mouseDoubleClickEvent = self.trMouseDoubleClickResponse      # 判断是否双击
        return self.var.trImageShow

    # 将图像显示在Label上
    def setTransverseImagePixmap(self, imagePixmap):
        if self.var.width > 400 or self.var.height > 400:   # 当图像高度或宽度超过400时，让图像适应Label大小
            self.var.trImageShow.setScaledContents(True)
        return self.var.trImageShow.setPixmap(imagePixmap)

    # 双击响应事件
    def trMouseDoubleClickResponse(self, event=None):
        settrLabelVisible(self.var)

    def coronalImageShow(self):

        self.var.coImageShow = self.createNewModel()
        self.var.coImageShow.mouseDoubleClickEvent = self.coMouseDoubleClickResponse  # 判断是否双击
        return self.var.coImageShow

    def setCoronalImagePixmap(self, imagePixmap):
        if self.var.width > 400 or self.var.height > 400:
            self.var.coImageShow.setScaledContents(True)
        return self.var.coImageShow.setPixmap(imagePixmap)

    # 双击响应事件
    def coMouseDoubleClickResponse(self, event=None):
        setcoLabelVisible(self.var)

    def sagittalImageShow(self):

        self.var.saImageShow = self.createNewModel()
        self.var.saImageShow.mouseDoubleClickEvent = self.saMouseDoubleClickResponse  # 判断是否双击
        return self.var.saImageShow

    def setSagittalImagePixmap(self, imagePixmap):
        if self.var.width > 400 or self.var.height > 400:
            self.var.saImageShow.setScaledContents(True)
        return self.var.saImageShow.setPixmap(imagePixmap)

    # 双击响应事件
    def saMouseDoubleClickResponse(self, event=None):
        setsaLabelVisible(self.var)

    def tDImageShow(self):

        self.var.tdImageShow = self.createNewModel()
        self.var.tdImageShow.mouseDoubleClickEvent = self.tDMouseDoubleClickResponse  # 判断是否双击
        return self.var.tdImageShow

    def setTDImagePixmap(self, imagePixmap):
        if self.var.width > 400 or self.var.height > 400:
            self.var.tdImageShow.setScaledContents(True)
        return self.var.tdImageShow.setPixmap(imagePixmap)

    # 双击响应事件
    def tDMouseDoubleClickResponse(self, event=None):
        settDLabelVisible(self.var)