import cv2
from PyQt5.QtGui import QPixmap
import MainGUI.Layout.InformationShowManager as ISM
from FileAction.readImageByCV import imageConvertion

#高斯去噪
def GaussianDenoising(var):

    var.GSFlag = True
    #第二的参数是高斯矩阵的大小，第三个参数是标准差，标准差取0时OpenCV会根据高斯矩阵的尺寸自己计算。概括地讲，高斯矩阵的尺寸越大，标准差越大，处理过的图像模糊程度越大。
    # cv2.GaussianBlur(var.img, (var.GSKernel, var.GSKernel), 0)
    var.img = cv2.GaussianBlur(var.img, (19, 19), 0)

    var.imagePixmap = QPixmap.fromImage(imageConvertion(var))
    ISM.openImageLayout(var, var.imagePixmap)  # 显示结果

# 高斯滤波
def GaussianDenoisingKernel(var, event):
    delta = event.pixelDelta().y()

    if delta > 0:
        var.GSKernel = var.GSKernel + 2
    else:
        if var.GSKernel > 1:
            var.GSKernel = var.GSKernel - 2

    GaussianDenoising(var)