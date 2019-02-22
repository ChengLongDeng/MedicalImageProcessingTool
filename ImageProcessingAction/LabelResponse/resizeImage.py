from PyQt5.QtGui import QPixmap
from resizeimage import resizeimage
from FileAction.readImageByCV import opencv2pil, pil2opencv, imageConvertion, imageConvertionWithImgMirror

# 调整图像大小
def resizeImage(var, lvar, width, height):

    lvar.setFixedSize(lvar.width() + width, lvar.height() + height)  # 调整Label大小

    var.img = opencv2pil(var.img)       # opencv打开图像转换成PIL形式
    var.img = resizeimage.resize_cover(var.img, [var.width + width, var.height + height], validate=False)
    var.img = pil2opencv(var.img)       # PIL类型图像转换成opencv形式

# 放大图片
def enlargeImage(var, lvar, width, height):

    if var.width < 800:
        resizeImage(var, lvar, width, height)

        var.trImageShow.setPixmap(QPixmap(imageConvertion(var)))        # 重新显示在Label中
        var.size.setText('(%d × %d)' % (var.width, var.height))         # 状态栏显示图像大小

# 缩小图片
def narrowImage(var, lvar, width, height):

    if var.width > 200:
        resizeImage(var, lvar, width, height)

        var.trImageShow.setPixmap(QPixmap(imageConvertion(var)))
        var.size.setText('(%d × %d)' % (var.width, var.height))         # 状态栏显示图像大小

# 将图像恢复成默认大小
def restoreImageToDefault(var, lvar):
    lvar.setFixedSize(400, 400)                                         # 调整Label大小为默认大小
    var.trImageShow.setPixmap(QPixmap(imageConvertionWithImgMirror(var)))

    var.size.setText('(%d × %d)' % (var.width_mirror, var.height_mirror))             # 状态栏显示图像大小