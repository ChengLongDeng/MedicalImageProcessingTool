from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette

class imageShowManager(QWidget):

    def __init__(self):
        super(imageShowManager, self).__init__()

    def transverseImageShow(self):

        self.trImageShow = QLabel()
        self.trImageShow.setAlignment(Qt.AlignCenter)
        self.trImageShow.setFixedSize(450, 400)
        imagePa = QPalette()
        imagePa.setColor(QPalette.Window, Qt.black)
        self.trImageShow.setAutoFillBackground(True)
        self.trImageShow.setPalette(imagePa)

        return self.trImageShow

    def setTransverseImagePixmap(self, imagePixmap):
        return self.trImageShow.setPixmap(imagePixmap)

    def coronalImageShow(self):

        self.coImageShow = QLabel()
        self.coImageShow.setAlignment(Qt.AlignCenter)
        self.coImageShow.setFixedSize(450, 400)
        self.imagePa = QPalette()
        self.imagePa.setColor(QPalette.Window, Qt.black)
        self.coImageShow.setAutoFillBackground(True)
        self.coImageShow.setPalette(self.imagePa)

        return self.coImageShow

    def setCoronalImagePixmap(self, imagePixmap):
        return self.coImageShow.setPixmap(imagePixmap)

    def sagittalImageShow(self):

        self.saImageShow = QLabel()
        self.saImageShow.setAlignment(Qt.AlignCenter)
        self.saImageShow.setFixedSize(450, 400)
        self.imagePa = QPalette()
        self.imagePa.setColor(QPalette.Window, Qt.black)
        self.saImageShow.setAutoFillBackground(True)
        self.saImageShow.setPalette(self.imagePa)

        return self.saImageShow

    def setSagittalImagePixmap(self, imagePixmap):
        return self.saImageShow.setPixmap(imagePixmap)

    def tDImageShow(self):

        self.tdImageShow = QLabel()
        self.tdImageShow.setAlignment(Qt.AlignCenter)
        self.tdImageShow.setFixedSize(450, 400)
        self.imagePa = QPalette()
        self.imagePa.setColor(QPalette.Window, Qt.black)
        self.tdImageShow.setAutoFillBackground(True)
        self.tdImageShow.setPalette(self.imagePa)

        return self.tdImageShow

    def setTDImagePixmap(self, imagePixmap):
        return self.tdImageShow.setPixmap(imagePixmap)
