

def RectLasso(var):
    var.rectFlag = True
    var.x0 = var.x1 = var.y0 = var.y1 = 0
    var.elliFlag = False


def elliLasso(var):
    var.elliFlag = True
    var.x0 = var.x1 = var.y0 = var.y1 = 0
    var.rectFlag = False