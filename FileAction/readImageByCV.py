import cv2
from PyQt5.QtGui import QImage

#Opencv与PyQt5之间相互转化
def readImage(var, imgDir):

    var.img = cv2.imread(imgDir)
    var.height, var.width, bytesPerComponent = var.img.shape
    bytesPerLine = 3 * var.width
    cv2.cvtColor(var.img, cv2.COLOR_BGR2RGB, var.img)       #将图像从一个颜色空间转换为另一个颜色空间
    var.QImg = QImage(var.img.data, var.width, var.height, bytesPerLine, QImage.Format_RGB888)
    return var.QImg