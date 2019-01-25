
#矩形套索控制
def RectLasso(var):
    var.rectFlag = True
    var.x0 = var.x1 = var.y0 = var.y1 = 0
    var.elliFlag = False
    var.polyFlag = False

    var.enlargeFlag = False     # 图像放大不可用
    var.narrowFlag = False      # 图像缩小不可用

#椭圆形套索
def elliLasso(var):
    var.elliFlag = True
    var.x0 = var.x1 = var.y0 = var.y1 = 0
    var.rectFlag = False
    var.polyFlag = False

    var.enlargeFlag = False     # 图像放大不可用
    var.narrowFlag = False      # 图像缩小不可用

#多边形套索
def polyLasso(var):
    var.polyFlag = True                     # 多边形套索
    var.x0 = var.x1 = var.y0 = var.y1 = 0   # 四个点归零
    var.rectFlag = False                    # 矩形套索
    var.elliFlag = False                    # 椭圆形套索

    var.enlargeFlag = False                 # 图像放大不可用
    var.narrowFlag = False                  # 图像缩小不可用

    var.chosen_points.clear()