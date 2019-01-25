from PyQt5.QtGui import QPen, QPixmap
from PyQt5.QtCore import Qt
import cv2, numpy
import MainGUI.Layout.InformationShowManager as ISM
from FileAction.readImageByCV import readImage, imageConvertion

# 画矩形
def cusDrawRect(var, painter):
    var.rect.setRect(var.x0, var.y0, var.x1 - var.x0, var.y1 - var.y0)
    painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
    painter.drawRect(var.rect)

# 使用opencv在图像上画矩形并写入磁盘，再读取
def drawRectByOpenCV(var, lvar):
    var.height, var.width, bytesPerComponent = var.img.shape    # 重新计算改变大小之后图像的大小
    w0 = int((float(var.width) / lvar.width()) * var.x0)
    h0 = int((float(var.height) / lvar.height()) * var.y0)
    w1 = int((float(var.width) / lvar.width()) * var.x1)
    h1 = int((float(var.height) / lvar.height()) * var.y1)

    cv2.rectangle(var.img, (w0, h0), (w1, h1), (0, 255, 0), 1)  # 在图像上画矩形
    # cv2.imwrite(var.im_path, var.img)

    var.imagePixmap = QPixmap.fromImage(imageConvertion(var))
    ISM.openImageLayout(var, var.imagePixmap)  # 显示结果

# 画圆形
def cusDrawElli(var, painter):
    var.rect.setRect(var.x0, var.y0, var.x1 - var.x0, var.y1 - var.y0)
    painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
    painter.drawEllipse(var.rect)

# 使用opencv在图像上画椭圆形并写入磁盘，再读取
def drawElliByOpenCV(var, lvar):
    var.height, var.width, bytesPerComponent = var.img.shape  # 重新计算改变大小之后图像的大小
    w0 = int((float(var.width) / lvar.width()) * var.x0)
    h0 = int((float(var.height) / lvar.height()) * var.y0)
    w1 = int((float(var.width) / lvar.width()) * var.x1)
    h1 = int((float(var.height) / lvar.height()) * var.y1)

    c_x = w0 + (w1 - w0) / 2
    c_y = h0 + (h1 - h0) / 2

    cv2.ellipse(var.img, (int(c_x), int(c_y)), (int((w1 - w0) / 2), int((h1 - h0) / 2)), 0.0, 0.0, 360.0, (0, 255, 0), 1)  # 在图像上画椭圆形
    cv2.imwrite(var.im_path, var.img)

    var.imagePixmap = QPixmap.fromImage(readImage(var, var.im_path))
    ISM.openImageLayout(var, var.imagePixmap)  # 显示结果

# 画点
def cusDrawPoint(var, qp):
    qp.setPen(QPen(Qt.red, 5))
    for pos in var.chosen_points:
        qp.drawPoint(pos)

# 画多边形
def cusDrawPolyline(var, qp):
    qp.setPen(QPen(Qt.red, 1))
    qp.drawPolyline(var.chosen_points)

# 使用opencv在图像上画多边形并写入磁盘，再读取
def drawPolyByOpenCV(var, lvar):
    var.height, var.width, bytesPerComponent = var.img.shape  # 重新计算改变大小之后图像的大小
    temp = []

    for pos in var.chosen_points:
        x = int((float(var.width) / lvar.width()) * pos.x())
        y = int((float(var.height) / lvar.height()) * pos.y())
        temp.append([x, y])

    points = numpy.array(temp, numpy.int32)
    points = points.reshape(-1, 1, 2)

    cv2.polylines(var.img, [points], True, (0, 255, 0))
    cv2.imwrite(var.im_path, var.img)

    var.imagePixmap = QPixmap.fromImage(readImage(var, var.im_path))
    ISM.openImageLayout(var, var.imagePixmap)  # 显示结果

    var.chosen_points.clear()