from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QFrame, QGroupBox, QSlider, QSpinBox, QTextEdit, QDockWidget, QGridLayout
from PyQt5.QtCore import Qt
from MainGUI.Layout.ImageInforShow import imageInfor
from ImageProcessingAction.LabelModel.labelModel import imageShowManager

def helpInforShow(var):

    helpInforDock = QDockWidget('帮助信息', var)

    helpContent = QTextEdit(var)
    helpContent.setFrameShape(QFrame.Panel | QFrame.Sunken)     # 边框样式
    helpContent.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)    # 内容显示样式
    helpContent.setEnabled(False)
    helpContent.setFocusPolicy(Qt.NoFocus)
    helpContent.setLineWrapMode(QTextEdit.NoWrap)   # 一行文本不换行
    helpContent.verticalScrollBar()                 # 垂直滚动
    helpContent.horizontalScrollBar()               # 水平滚动
    helpContent.setPlaceholderText('此处显示帮助文档')

    helpInforDock.setFeatures(QDockWidget.NoDockWidgetFeatures)
    helpInforDock.setWidget(helpContent)

    return helpInforDock

def sliceManager(var):

    sliceDock = QDockWidget('图像调节', var)
    sliceGroup = QGroupBox()
    vbox = QVBoxLayout()
    sliceHBox = QHBoxLayout()
    luminanceHBox = QHBoxLayout()

    contrastLabel = QLabel('对比度: ', var)
    luminanceLabel = QLabel('亮    度: ', var)

    var.contrastSlide = QSlider(Qt.Horizontal, var)
    var.luminanceSlide = QSlider(Qt.Horizontal, var)

    var.contrastSpin = QSpinBox(var)
    var.luminanceSpin = QSpinBox(var)

    var.contrastSlide.setFocusPolicy(Qt.NoFocus)
    var.contrastSlide.setSingleStep(1)
    var.contrastSlide.setMinimum(1)
    var.contrastSlide.setTickPosition(QSlider.TicksAbove)  # 设置刻度信息
    var.contrastSlide.setEnabled(False)
    # sliceSlide.setFixedSize(1, 100)

    var.luminanceSlide.setFocusPolicy(Qt.NoFocus)
    var.luminanceSlide.setSingleStep(1)
    var.luminanceSlide.setMinimum(1)
    var.luminanceSlide.setTickPosition(QSlider.TicksLeft)  # 设置刻度信息
    var.luminanceSlide.valueChanged.connect(var.luminanceSpin.setValue)
    var.luminanceSlide.setEnabled(False)

    var.contrastSpin.setSingleStep(1)
    # var.sliceSpin.setWrapping(True)   #是否循环
    var.contrastSpin.setValue(1)
    var.contrastSpin.setEnabled(False)

    var.luminanceSpin.setSingleStep(1)
    # var.luminanceSpin.setWrapping(True)
    var.luminanceSpin.setValue(1)
    var.luminanceSpin.setEnabled(False)
    var.luminanceSpin.valueChanged.connect(var.luminanceSlide.setValue)

    sliceHBox.addWidget(contrastLabel)
    sliceHBox.addWidget(var.contrastSlide)
    sliceHBox.addWidget(var.contrastSpin)

    luminanceHBox.addWidget(luminanceLabel)
    luminanceHBox.addWidget(var.luminanceSlide)
    luminanceHBox.addWidget(var.luminanceSpin)

    vbox.addLayout(sliceHBox)
    vbox.addLayout(luminanceHBox)
    vbox.addStretch()

    sliceGroup.setLayout(vbox)
    sliceDock.setFeatures(QDockWidget.NoDockWidgetFeatures)
    sliceDock.setWidget(sliceGroup)

    return sliceDock

# 调节图像亮度
def setLuminanceStatus(var):

    var.luminanceSlide.setEnabled(True)
    var.luminanceSpin.setEnabled(True)

    var.luminanceSlide.setMaximum(20)
    var.luminanceSpin.setRange(1, 20)


def imageInforShow(var):

    imageInforDock = QDockWidget('图像信息', var)

    imageInforDock.setFeatures(QDockWidget.DockWidgetClosable)
    imageInforDock.setWidget(imageInfor(var))

    return imageInforDock

# 显示空的图像区域
def imageShow(var):

    imageLayout = QGridLayout()
    var.imageShow = imageShowManager(var)

    imageLayout.addWidget(var.imageShow.transverseImageShow(), 0, 0)
    imageLayout.addWidget(var.imageShow.coronalImageShow(), 0, 1)
    imageLayout.addWidget(var.imageShow.sagittalImageShow(), 1, 0)
    imageLayout.addWidget(var.imageShow.tDImageShow(), 1, 1)

    # imageGroup.setLayout(imageLayout)
    return imageLayout

# 显示打开图像
def openImageLayout(var, imagePixmap):
    var.imageShow.setTransverseImagePixmap(imagePixmap)
    var.imageShow.setCoronalImagePixmap(imagePixmap)
    var.imageShow.setSagittalImagePixmap(imagePixmap)
    var.imageShow.setTDImagePixmap(imagePixmap)

