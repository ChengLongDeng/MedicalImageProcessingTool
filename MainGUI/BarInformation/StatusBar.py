from PyQt5.QtWidgets import QLabel

def statusbarAchieve(var):

    var.location = QLabel()     # 显示鼠标点位置信息
    var.pixel = QLabel()        # 显示鼠标点像素信息
    var.size = QLabel()        # 显示鼠标点像素信息

    var.statusBar().addPermanentWidget(var.size)
    var.statusBar().addPermanentWidget(var.location)
    var.statusBar().addPermanentWidget(var.pixel)