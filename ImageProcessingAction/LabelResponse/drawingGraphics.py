from PyQt5.QtGui import QPen, QPixmap
from PyQt5.QtCore import Qt
import cv2, numpy
import MainGUI.Layout.InformationShowManager as ISM
from FileAction.readImageByCV import readImage, imageConvertion

def calculateRelativePosition(var, lvar):
    var.height, var.width, bytesPerComponent = var.img.shape  # 重新计算改变大小之后图像的大小

    # 计算在img图像上套索位置
    var.w0 = int((float(var.width) / lvar.width()) * var.x0)
    var.h0 = int((float(var.height) / lvar.height()) * var.y0)
    var.w1 = int((float(var.width) / lvar.width()) * var.x1)
    var.h1 = int((float(var.height) / lvar.height()) * var.y1)

    # 计算在img_mirror图像上套索位置
    var.w0_m = int((float(var.width_mirror) / lvar.width()) * var.x0)
    var.h0_m = int((float(var.height_mirror) / lvar.height()) * var.y0)
    var.w1_m = int((float(var.width_mirror) / lvar.width()) * var.x1)
    var.h1_m = int((float(var.height_mirror) / lvar.height()) * var.y1)


# 画矩形
def cusDrawRect(var, painter):
    var.rect.setRect(var.x0, var.y0, var.x1 - var.x0, var.y1 - var.y0)
    painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
    painter.drawRect(var.rect)

# 使用opencv在图像上画矩形并写入磁盘，再读取
def drawRectByOpenCV(var, lvar):

    calculateRelativePosition(var, lvar)            # 计算套索顶点相对位置

    cv2.rectangle(var.img, (var.w0, var.h0), (var.w1, var.h1), (0, 255, 0), 1)  # 在图像上画矩形
    cv2.rectangle(var.img_mirror, (var.w0_m, var.h0_m), (var.w1_m, var.h1_m), (0, 255, 0), 1)  # 在img_mirror图像上画矩形

    cv2.imwrite(var.im_path, var.img_mirror)               # 写入硬盘

    var.imagePixmap = QPixmap.fromImage(imageConvertion(var))
    ISM.openImageLayout(var, var.imagePixmap)  # 显示结果

# 画圆形
def cusDrawElli(var, painter):
    var.rect.setRect(var.x0, var.y0, var.x1 - var.x0, var.y1 - var.y0)
    painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
    painter.drawEllipse(var.rect)

# 使用opencv在图像上画椭圆形并写入磁盘，再读取
def drawElliByOpenCV(var, lvar):

    calculateRelativePosition(var, lvar)            # 计算套索顶点相对位置

    c_x = var.w0 + (var.w1 - var.w0) / 2
    c_y = var.h0 + (var.h1 - var.h0) / 2

    c_x_m = var.w0_m + (var.w1_m - var.w0_m) / 2
    c_y_m = var.h0_m + (var.h1_m - var.h0_m) / 2

    cv2.ellipse(var.img, (int(c_x), int(c_y)), (int((var.w1 - var.w0) / 2), int((var.h1 - var.h0) / 2)), 0.0, 0.0, 360.0, (0, 255, 0), 1)  # 在图像上画椭圆形
    cv2.ellipse(var.img, (int(c_x_m), int(c_y_m)), (int((var.w1_m - var.w0_m) / 2), int((var.h1_m - var.h0_m) / 2)), 0.0, 0.0, 360.0, (0, 255, 0), 1)  # 在图像上画椭圆形
    cv2.imwrite(var.im_path, var.img_mirror)

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
    var.height, var.width, bytesPerComponent = var.img.shape                        # 重新计算改变大小之后图像的大小
    temp = []
    temp_m = []

    # 在img图像上计算顶点位置
    for pos in var.chosen_points:
        x = int((float(var.width) / lvar.width()) * pos.x())
        y = int((float(var.height) / lvar.height()) * pos.y())
        temp.append([x, y])

    # 在img_mirror图像上计算顶点位置
    for pos in var.chosen_points:
        x_m = int((float(var.width_mirror) / lvar.width()) * pos.x())
        y_m = int((float(var.height_mirror) / lvar.height()) * pos.y())
        temp_m.append([x_m, y_m])

    points = numpy.array(temp, numpy.int32)
    points = points.reshape(-1, 1, 2)

    points_m = numpy.array(temp_m, numpy.int32)
    points_m = points_m.reshape(-1, 1, 2)

    cv2.polylines(var.img, [points], True, (0, 255, 0))
    cv2.polylines(var.img_mirror, [points_m], True, (0, 255, 0))
    cv2.imwrite(var.im_path, var.img_mirror)

    var.imagePixmap = QPixmap.fromImage(readImage(var, var.im_path))
    ISM.openImageLayout(var, var.imagePixmap)  # 显示结果

    var.chosen_points.clear()