from PyQt5.QtWidgets import QWidget
from MainGUI.FileManager import show
from MainGUI.InformationShowManager import *
from PyQt5.QtCore import Qt

def mainLayout(var):

    var.widget = QWidget()
    var.setCentralWidget(var.widget)

    #左侧信息显示区域
    var.addDockWidget(Qt.LeftDockWidgetArea, show(var))      #文件显示区域

    #基本信息显示区域
    helpInforDock = helpInforShow(var)      #帮助信息显示
    sliceDock = sliceManager(var)           #切换图像
    imageInforDock = imageInforShow(var)    #图像信息

    var.addDockWidget(Qt.LeftDockWidgetArea, helpInforDock)
    var.addDockWidget(Qt.LeftDockWidgetArea, sliceDock)
    var.addDockWidget(Qt.LeftDockWidgetArea, imageInforDock)
    var.tabifyDockWidget(helpInforDock, sliceDock)
    var.tabifyDockWidget(helpInforDock, imageInforDock)
    helpInforDock.raise_()

    #图像显示区域
    var.widget.setLayout(imageShow(var))

def openImageShow(self, image):

    self.widget.setLayout(image)
    self.show()