from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from FileAction.mouseAction import labelModel

class imageShowManager(QWidget):

    def __init__(self, var):
        super(imageShowManager, self).__init__()
        self.var = var

    def transverseImageShow(self):

        self.var.trImageShow = labelModel(self.var)            #新建自定义QLabel
        self.var.trImageShow.setAlignment(Qt.AlignCenter)
        self.var.trImageShow.setFixedSize(450, 400)
        imagePa = QPalette()
        imagePa.setColor(QPalette.Window, Qt.black)
        self.var.trImageShow.setAutoFillBackground(True)
        self.var.trImageShow.setPalette(imagePa)
        self.var.trImageShow.setScaledContents(True)

        return self.var.trImageShow

    def setTransverseImagePixmap(self, imagePixmap):
        return self.var.trImageShow.setPixmap(imagePixmap)

    def coronalImageShow(self):

        self.var.coImageShow = labelModel(self.var)
        self.var.coImageShow.setAlignment(Qt.AlignCenter)
        self.var.coImageShow.setFixedSize(450, 400)
        self.imagePa = QPalette()
        self.imagePa.setColor(QPalette.Window, Qt.black)
        self.var.coImageShow.setAutoFillBackground(True)
        self.var.coImageShow.setPalette(self.imagePa)
        self.var.coImageShow.setScaledContents(True)

        return self.var.coImageShow

    def setCoronalImagePixmap(self, imagePixmap):
        return self.var.coImageShow.setPixmap(imagePixmap)

    def sagittalImageShow(self):

        self.var.saImageShow = labelModel(self.var)
        self.var.saImageShow.setAlignment(Qt.AlignCenter)
        self.var.saImageShow.setFixedSize(450, 400)
        self.imagePa = QPalette()
        self.imagePa.setColor(QPalette.Window, Qt.black)
        self.var.saImageShow.setAutoFillBackground(True)
        self.var.saImageShow.setPalette(self.imagePa)
        self.var.saImageShow.setScaledContents(True)

        return self.var.saImageShow

    def setSagittalImagePixmap(self, imagePixmap):
        return self.var.saImageShow.setPixmap(imagePixmap)

    def tDImageShow(self):

        self.var.tdImageShow = labelModel(self.var)
        self.var.tdImageShow.setAlignment(Qt.AlignCenter)
        self.var.tdImageShow.setFixedSize(450, 400)
        self.imagePa = QPalette()
        self.imagePa.setColor(QPalette.Window, Qt.black)
        self.var.tdImageShow.setAutoFillBackground(True)
        self.var.tdImageShow.setPalette(self.imagePa)
        self.var.tdImageShow.setScaledContents(True)

        return self.var.tdImageShow

    def setTDImagePixmap(self, imagePixmap):
        return self.var.tdImageShow.setPixmap(imagePixmap)
