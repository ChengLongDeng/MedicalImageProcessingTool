import cv2

# 放大图片
def enlargeImageSize(var, width, height):
    var.img = cv2.resize(var.img, (width, height), 0, 0, interpolation=cv2.INTER_CUBIC)

# 缩小图片
def narrowImageSize(var, width, height):
    var.img = cv2.resize(var.img, (width, height), 0, 0, interpolation=cv2.INTER_AREA)

# 改变Label大小
def changeLabelSize(var, lvar, ratio, event):

    delta = event.pixelDelta().y()

    if delta > 0:
        if lvar.width() < 900 or lvar.height() < 800:
            lvar.setFixedSize(lvar.width() + delta, lvar.height() + delta)  # 放大Label
            enlargeImageSize(var, lvar.width(), lvar.height())                      # 放大图像
    else:
        if lvar.width() > 225 or lvar.height() > 200:
            lvar.setFixedSize(lvar.width() + delta, lvar.height() + delta)  # 缩小Label
            narrowImageSize(var, lvar.width(), lvar.height())                       # 缩小图像

