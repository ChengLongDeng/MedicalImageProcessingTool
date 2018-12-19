from PyQt5.QtWidgets import QAction, qApp, QMenu
from PyQt5.QtGui import QIcon, QFont
from FileAction.openFileAction import *
from FileAction.saveFileAction import *
from FileAction.saveAsFileAction import *
from FileAction.openFileSequenceAction import *

#菜单栏实现
def menubarAchieve(var):

    openfileAction = QAction('&打开图像', var)
    openfileAction.setShortcut('Ctrl+O')
    openfileAction.setStatusTip('打开图像')
    openfileAction.triggered.connect(lambda: openFile(var))

    opennextfileAction = QAction('&打开下一个', var)
    opennextfileAction.setShortcut('Ctrl+Shift+O')
    opennextfileAction.setStatusTip('打开下一张图像')
    opennextfileAction.triggered.connect(lambda: openNextFile(var))

    openseriesfileAction = QAction('&打开文件夹', var)
    openseriesfileAction.setStatusTip('打开图像文件夹')
    openseriesfileAction.triggered.connect(lambda: openFileSequence(var))

    closeAction = QAction('&退出', var)
    closeAction.setShortcut('Ctrl+W')
    closeAction.setStatusTip('退出')
    closeAction.triggered.connect(qApp.quit)

    saveAction = QAction('&保存', var)
    saveAction.setShortcut('Ctrl+S')
    saveAction.setStatusTip('保存图像')
    saveAction.triggered.connect(lambda: saveFile(var))

    saveasAction = QAction('&另存为', var)
    saveasAction.setStatusTip('图像另存为')
    saveasAction.triggered.connect(lambda: saveAsFile(var))

    # self.statusBar()

    # QMenuBar * menubar = new QMenuBar(0)

    menubar = var.menuBar()
    menubar.setFont(QFont('SansSerif', 15))
    menubar.setNativeMenuBar(False)
    fileMenu = menubar.addMenu('&文件')

    fileMenu.addAction(openfileAction)
    fileMenu.addAction(opennextfileAction)
    fileMenu.addAction(openseriesfileAction)
    fileMenu.addAction(saveAction)
    fileMenu.addAction(saveasAction)
    fileMenu.addAction(closeAction)

    #编辑菜单
    undoAction = QAction('&撤销', var)
    undoAction.setShortcut('Ctrl+Z')
    undoAction.setStatusTip('撤销操作')
    undoAction.triggered.connect(qApp.quit)

    doAction = QAction('&恢复', var)
    doAction.setShortcut('Ctrl+U')
    doAction.setStatusTip('恢复操作')
    doAction.triggered.connect(qApp.quit)

    clearAction = QAction('&清除图像痕迹', var)
    clearAction.setStatusTip('清除图像上痕迹')
    clearAction.triggered.connect(qApp.quit)

    compileMenu = menubar.addMenu('&编辑')
    compileMenu.addAction(undoAction)
    compileMenu.addAction(doAction)
    compileMenu.addAction(clearAction)

    #视图菜单
    imageInforAction = QAction('&图像信息', var, checkable = True)
    imageInforAction.setStatusTip('显示图像信息')
    imageInforAction.setChecked(True)
    imageInforAction.triggered.connect(qApp.quit)

    viewMenu = menubar.addMenu('&视图')
    viewMenu.addAction(imageInforAction)

    #图像操作菜单
    denoiseAction = QAction('&图像去噪', var)
    denoiseAction.setStatusTip('图像去噪操作')
    denoiseAction.triggered.connect(qApp.quit)

    smoothAction = QAction('&平滑处理', var)
    smoothAction.setStatusTip('平滑处理操作')
    smoothAction.triggered.connect(qApp.quit)

    contrastAction = QAction('&对比度增强', var)
    contrastAction.setStatusTip('增强图像对比度')
    contrastAction.triggered.connect(qApp.quit)

    lassoAction = QMenu('&套索工具', var)

    rectangleLassoAction = QAction(QIcon('./Icon/rectangle.png'), '&矩形套索工具', var)
    rectangleLassoAction.setStatusTip('矩形套索工具')
    rectangleLassoAction.triggered.connect(qApp.quit)
    lassoAction.addAction(rectangleLassoAction)

    ellipseLassoAction = QAction(QIcon('./Icon/ellipse.png'), '&椭圆形套索工具', var)
    ellipseLassoAction.setStatusTip('椭圆形套索工具')
    ellipseLassoAction.triggered.connect(qApp.quit)
    lassoAction.addAction(ellipseLassoAction)

    customLassoAction = QAction(QIcon('save.png'), '&磁性套索工具', var)
    customLassoAction.setStatusTip('磁性套索工具')
    customLassoAction.triggered.connect(qApp.quit)
    lassoAction.addAction(customLassoAction)

    segmentationAction = QMenu('&图像分割', var)

    thresholdAction = QAction('&阈值分割', var)
    thresholdAction.setStatusTip('阈值分割')
    thresholdAction.triggered.connect(qApp.quit)
    segmentationAction.addAction(thresholdAction)

    graphcutAction = QAction('&图切', var)
    graphcutAction.setStatusTip('图切')
    graphcutAction.triggered.connect(qApp.quit)
    segmentationAction.addAction(graphcutAction)


    processMenu = menubar.addMenu('&处理')
    processMenu.addAction(denoiseAction)
    processMenu.addAction(smoothAction)
    processMenu.addAction(contrastAction)
    processMenu.addMenu(lassoAction)
    processMenu.addMenu(segmentationAction)

    #帮助菜单
    helpAction = QAction(QIcon('help.png'), '&帮助文档', var)
    helpAction.setStatusTip('打开帮助文档')
    helpAction.triggered.connect(qApp.quit)

    helpMenu = menubar.addMenu('&帮助')
    helpMenu.addAction(helpAction)