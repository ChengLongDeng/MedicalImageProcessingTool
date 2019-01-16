from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt

#画矩形
def cusDrawRect(var, painter):
    var.rect.setRect(var.x0, var.y0, var.x1 - var.x0, var.y1 - var.y0)
    painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
    painter.drawRect(var.rect)

#画圆形
def cusDrawElli(var, painter):
    var.rect.setRect(var.x0, var.y0, var.x1 - var.x0, var.y1 - var.y0)
    painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
    painter.drawEllipse(var.rect)

#画点
def cusDrawPoint(var, qp):
    qp.setPen(QPen(Qt.red, 5))
    for pos in var.chosen_points:
        qp.drawPoint(pos)

#画多边形
def cusDrawPolyline(var, qp):
    qp.setPen(QPen(Qt.red, 1))
    qp.drawPolyline(var.chosen_points)