
# 显示4张图像时，状态栏上显示的信息
def showInforInStatusBarWithFourImage(var, event):

    var.size.setText('(%d × %d)' % (var.width_mirror, var.height_mirror))                       # 状态栏显示图像大小
    var.location.setText('(x : %d, y : %d)' % (event.pos().x(), event.pos().y()))               # 鼠标位置信息

    if event.pos().x() >= var.width_mirror or event.pos().y() >= var.height_mirror:             # 鼠标所在位置超过图像大小
        var.pixel.setText('(r : %d, g : %d, b : %d)' % (0, 0, 0))
    else:
        var.pixel.setText('(r : %d, g : %d, b : %d)' % (var.img_mirror[event.pos().y()][event.pos().x()][2], var.img_mirror[event.pos().y()][event.pos().x()][1], var.img_mirror[event.pos().y()][event.pos().x()][0]))  # 鼠标所在位置像素信息

# 显示1张图像时，状态栏上显示的信息
def showInforInStatusBarWithOneImage(var, event):

    var.size.setText('(%d × %d)' % (var.width, var.height))                             # 状态栏显示图像大小
    var.location.setText('(x : %d, y : %d)' % (event.pos().x(), event.pos().y()))       # 鼠标位置信息

    if event.pos().x() >= var.width or event.pos().y() >= var.height:                   # 鼠标所在位置超过图像大小
        var.pixel.setText('(r : %d, g : %d, b : %d)' % (0, 0, 0))
    else:
        var.pixel.setText('(r : %d, g : %d, b : %d)' % (var.img[event.pos().y()][event.pos().x()][2], var.img[event.pos().y()][event.pos().x()][1], var.img[event.pos().y()][event.pos().x()][0]))  # 鼠标所在位置像素信息
