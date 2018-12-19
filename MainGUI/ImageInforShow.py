from PyQt5.QtWidgets import QLabel, QGridLayout, QSlider, QDoubleSpinBox, QWidget, QGroupBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette


def imageInfor(var):

    inforBox = QGroupBox()
    inforLayout = QVBoxLayout()
    pixelBox = QGroupBox()
    positionBox = QGroupBox()
    pixelLayout = QHBoxLayout()
    positionGridLayout = QGridLayout()

    var.xInfor = QLabel('X: ')
    var.yInfor = QLabel('Y: ')
    var.zInfor = QLabel('Z: ')
    var.pixelInfor = QLabel('像素值:')
    var.rInfor = QLabel('R: ')
    var.gInfor = QLabel('G: ')
    var.bInfor = QLabel('B: ')

    var.xslid = QSlider(Qt.Horizontal, var)
    var.yslid = QSlider(Qt.Horizontal, var)
    var.zslid = QSlider(Qt.Horizontal, var)

    var.xspan = QDoubleSpinBox()
    var.yspan = QDoubleSpinBox()
    var.zspan = QDoubleSpinBox()
    var.rspan = QDoubleSpinBox()
    var.gspan = QDoubleSpinBox()
    var.bspan = QDoubleSpinBox()

    var.xslid.setFocusPolicy(Qt.NoFocus)
    var.xslid.setSingleStep(1)
    var.xslid.setMinimum(0)
    var.xslid.setEnabled(False)
    var.xslid.setTickPosition(QSlider.TicksAbove)       #设置刻度信息
    var.xslid.valueChanged.connect(var.xspan.setValue)

    var.yslid.setFocusPolicy(Qt.NoFocus)
    var.yslid.setSingleStep(1)
    var.yslid.setMinimum(0)
    var.yslid.setEnabled(False)
    var.yslid.setTickPosition(QSlider.TicksAbove)  # 设置刻度信息
    var.yslid.valueChanged.connect(var.yspan.setValue)

    var.zslid.setFocusPolicy(Qt.NoFocus)
    var.zslid.setSingleStep(1)
    var.zslid.setMinimum(0)
    var.zslid.setEnabled(False)
    var.zslid.setTickPosition(QSlider.TicksAbove)  # 设置刻度信息
    var.zslid.valueChanged.connect(var.zspan.setValue)

    var.xspan.setSingleStep(0.01)
    var.xspan.setWrapping(False)       #不开启循环
    var.xspan.setValue(0)
    var.xspan.setDecimals(2)
    var.xspan.setEnabled(False)
    var.xspan.valueChanged.connect(var.xslid.setValue)

    var.yspan.setSingleStep(0.01)
    var.yspan.setWrapping(False)
    var.yspan.setValue(0)
    var.yspan.setDecimals(2)
    var.yspan.setEnabled(False)
    var.yspan.valueChanged.connect(var.yslid.setValue)

    var.zspan.setSingleStep(0.01)
    var.zspan.setWrapping(False)
    var.zspan.setValue(0)
    var.zspan.setDecimals(2)
    var.zspan.setEnabled(False)
    var.zspan.valueChanged.connect(var.zslid.setValue)

    var.rspan.setRange(0, 255)
    var.rspan.setSingleStep(0.01)
    var.rspan.setWrapping(False)
    var.rspan.setValue(0)
    var.rspan.setDecimals(2)
    var.rspan.setEnabled(False)
    # self.rspan.valueChanged.connect(self.rslid.setValue)
    rPa = QPalette()
    rPa.setColor(QPalette.Window, Qt.red)
    var.rspan.setAutoFillBackground(True)
    var.rspan.setPalette(rPa)

    var.gspan.setRange(0, 255)
    var.gspan.setSingleStep(0.01)
    var.gspan.setWrapping(False)
    var.gspan.setValue(0)
    var.gspan.setDecimals(2)
    var.gspan.setEnabled(False)
    # self.gspan.valueChanged.connect(self.gslid.setValue)
    gPa = QPalette()
    gPa.setColor(QPalette.Window, Qt.green)
    var.gspan.setAutoFillBackground(True)
    var.gspan.setPalette(gPa)

    var.bspan.setRange(0, 255)
    var.bspan.setSingleStep(0.01)
    var.bspan.setWrapping(False)
    var.bspan.setValue(0)
    var.bspan.setDecimals(2)
    var.bspan.setEnabled(False)
    # self.bspan.valueChanged.connect(self.bslid.setValue)
    bPa = QPalette()
    bPa.setColor(QPalette.Window, Qt.blue)
    var.bspan.setAutoFillBackground(True)
    var.bspan.setPalette(bPa)

    positionGridLayout.addWidget(var.xInfor, 0, 0)
    positionGridLayout.addWidget(var.xslid, 0, 1)
    positionGridLayout.addWidget(var.xspan, 0, 2)
    positionGridLayout.addWidget(var.yInfor, 1, 0)
    positionGridLayout.addWidget(var.yslid, 1, 1)
    positionGridLayout.addWidget(var.yspan, 1, 2)
    positionGridLayout.addWidget(var.zInfor, 2, 0)
    positionGridLayout.addWidget(var.zslid, 2, 1)
    positionGridLayout.addWidget(var.zspan, 2, 2)

    pixelLayout.addWidget(var.pixelInfor)
    pixelLayout.addWidget(var.rspan)
    pixelLayout.addWidget(var.gspan)
    pixelLayout.addWidget(var.bspan)

    pixelBox.setLayout(pixelLayout)
    positionBox.setLayout(positionGridLayout)

    # inforBox.setLayout(gridLayout)

    # pixelBox.setFixedSize(400, 150)
    # positionBox.setFixedSize(400, 150)

    inforLayout.addWidget(pixelBox)
    inforLayout.addWidget(positionBox)
    inforLayout.addStretch()

    inforBox.setLayout(inforLayout)

    return inforBox

def setWidgetStatus(var):

    var.xslid.setEnabled(True)
    var.yslid.setEnabled(True)
    # var.zslid.setEnabled(True)
    var.xspan.setEnabled(True)
    var.yspan.setEnabled(True)
    # var.zspan.setEnabled(True)
    var.rspan.setEnabled(True)
    var.gspan.setEnabled(True)
    var.bspan.setEnabled(True)

    var.xslid.setMaximum(var.width)
    var.yslid.setMaximum(var.height)
    # var.zslid.setMaximum(512)
    var.xspan.setRange(0, var.width)
    var.yspan.setRange(0, var.height)
    # var.zspan.setRange(0, 512)