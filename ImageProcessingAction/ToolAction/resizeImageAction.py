
# 放大图像响应
def enlargeImage(var):
    if var.trFlag is False or var.coFlag is False or var.saFlag is False or var.tdFlag is False:  # 判断是否双击
        var.enlargeFlag = True
        var.narrowFlag = False

        var.rectFlag = False        # 矩形套索不可用
        var.elliFlag = False        # 椭圆形套索不可用
        var.polyFlag = False        # 多边形套索不可用

# 缩小图像响应
def narrowImage(var):
    if var.trFlag is False or var.coFlag is False or var.saFlag is False or var.tdFlag is False:  # 判断是否双击
        var.enlargeFlag = False
        var.narrowFlag = True

        var.rectFlag = False        # 矩形套索不可用
        var.elliFlag = False        # 椭圆形套索不可用
        var.polyFlag = False        # 多边形套索不可用