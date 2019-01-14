
#矩形套索控制
def RectLasso(var):
    var.rectFlag = True
    var.x0 = var.x1 = var.y0 = var.y1 = 0
    var.elliFlag = False
    var.polyFlag = False

#椭圆形套索
def elliLasso(var):
    var.elliFlag = True
    var.x0 = var.x1 = var.y0 = var.y1 = 0
    var.rectFlag = False
    var.polyFlag = False

#多边形套索
def polyLasso(var):
    var.polyFlag = True
    var.x0 = var.x1 = var.y0 = var.y1 = 0
    var.rectFlag = False
    var.elliFlag = False
    var.chosen_points.clear()