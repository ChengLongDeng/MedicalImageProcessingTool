import cv2, numpy
from PyQt5.QtGui import QImage
from PIL import Image

# 从磁盘读图像，Opencv与PyQt5之间相互转化
def readImage(var, imgDir):

    var.img = cv2.imread(imgDir)
    var.img_mirror = var.img
    var.height, var.width, bytesPerComponent = var.img.shape
    var.height_mirror, var.width_mirror, bytesPerComponent_mirror = var.img_mirror.shape
    bytesPerLine = 3 * var.width
    cv2.cvtColor(var.img, cv2.COLOR_BGR2RGB, var.img)       # 将图像从一个颜色空间转换为另一个颜色空间
    var.QImg = QImage(var.img.data, var.width, var.height, bytesPerLine, QImage.Format_RGB888)
    return var.QImg

# 将内存中img图像读出来，Opencv与PyQt5之间相互转化
def imageConvertion(var):
    var.height, var.width, bytesPerComponent = var.img.shape
    bytesPerLine = 3 * var.width
    cv2.cvtColor(var.img, cv2.COLOR_BGR2RGB, var.img)       # 将图像从一个颜色空间转换为另一个颜色空间
    var.QImg = QImage(var.img.data, var.width, var.height, bytesPerLine, QImage.Format_RGB888)
    return var.QImg

# 将内存中的img_mirror图像读出来，Opencv与PyQt5之间相互转化
def imageConvertionWithImgMirror(var):
    var.height_mirror, var.width_mirror, bytesPerComponent = var.img_mirror.shape
    bytesPerLine = 3 * var.width_mirror
    cv2.cvtColor(var.img_mirror, cv2.COLOR_BGR2RGB, var.img_mirror)       # 将图像从一个颜色空间转换为另一个颜色空间
    var.QImg = QImage(var.img_mirror.data, var.width_mirror, var.height_mirror, bytesPerLine, QImage.Format_RGB888)
    return var.QImg

# 将opencv读出的图像转换成PIL
def opencv2pil(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img)
    return img_pil

# 将PIL读出的图像转换成opencv
def pil2opencv(img):
    pil_image = img.convert('RGB')          # Convert RGB to BGR
    opencv_image = numpy.array(pil_image)
    opencv_image = opencv_image[:, :, ::-1].copy()
    return opencv_image