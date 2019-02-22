from PyQt5.QtGui import QPixmap
from FileAction.readImageByCV import imageConvertion
from ImageProcessingAction.LabelResponse.resizeImage import restoreImageToDefault

def setToolDisable(var):
    # var.rectFlag = False        # 矩形套索不可用
    # var.elliFlag = False        # 椭圆形套索不可用
    # var.polyFlag = False        # 多边形套索不可用
    var.enlargeFlag = False     # 放大图像不可用
    var.narrowFlag = False      # 缩小图像不可用

# trLabel双击响应
def settrLabelVisible(var):
    if var.trImageShow.pixmap():                                    # 判断是否加载图片
        if var.trFlag:
            var.coImageShow.setVisible(False)
            var.saImageShow.setVisible(False)
            var.tdImageShow.setVisible(False)

            var.trImageShow.setPixmap(QPixmap(imageConvertion(var)))    # 重新显示图像
            var.trImageShow.setFixedSize(var.width, var.height)         # 设定大小
            var.trFlag = False
            setToolDisable(var)                                         # 放大、缩小工具不可用
        else:
            # 由于双击改变图像大小后，再双击变回原来大小时，实际图像的大小已经改变，但是这里没有体现
            restoreImageToDefault(var, var.trImageShow)
            var.coImageShow.setVisible(True)
            var.saImageShow.setVisible(True)
            var.tdImageShow.setVisible(True)
            var.trFlag = True

# coLabel双击响应
def setcoLabelVisible(var):
    if var.coImageShow.pixmap():                                 # 判断是否加载图片
        if var.coFlag:
            var.trImageShow.setVisible(False)
            var.saImageShow.setVisible(False)
            var.tdImageShow.setVisible(False)

            var.coImageShow.setPixmap(QPixmap(imageConvertion(var)))
            var.coImageShow.setFixedSize(var.width, var.height)
            var.coFlag = False
            setToolDisable(var)                                 # 放大、缩小工具不可用
        else:
            restoreImageToDefault(var, var.coImageShow)
            var.trImageShow.setVisible(True)
            var.saImageShow.setVisible(True)
            var.tdImageShow.setVisible(True)
            var.coFlag = True

def setsaLabelVisible(var):
    if var.saImageShow.pixmap():                                # 判断是否加载图片
        if var.saFlag:
            var.coImageShow.setVisible(False)
            var.trImageShow.setVisible(False)
            var.tdImageShow.setVisible(False)

            var.saImageShow.setPixmap(QPixmap(imageConvertion(var)))
            var.saImageShow.setFixedSize(var.width, var.height)
            var.coFlag = False
            setToolDisable(var)                                 # 放大、缩小工具不可用
        else:
            restoreImageToDefault(var, var.saImageShow)
            var.coImageShow.setVisible(True)
            var.trImageShow.setVisible(True)
            var.tdImageShow.setVisible(True)
            var.saFlag = True

def settDLabelVisible(var):
    if var.tdImageShow.pixmap():                                # 判断是否加载图片
        if var.tdFlag:
            var.coImageShow.setVisible(False)
            var.saImageShow.setVisible(False)
            var.trImageShow.setVisible(False)

            var.tdImageShow.setPixmap(QPixmap(imageConvertion(var)))
            var.tdImageShow.setFixedSize(var.width, var.height)
            var.coFlag = False
            setToolDisable(var)                                 # 放大、缩小工具不可用
        else:
            restoreImageToDefault(var, var.tdImageShow)
            var.coImageShow.setVisible(True)
            var.saImageShow.setVisible(True)
            var.trImageShow.setVisible(True)
            var.tdFlag = True