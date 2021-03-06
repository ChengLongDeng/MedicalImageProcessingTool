from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtGui import QIcon
from ImageProcessingAction.ToolAction.resizeImageAction import enlargeImage, narrowImage

def toolbarAchieve(var):

    openFileAction = QAction(QIcon('./Icon/open.tif'), '&打开', var)
    openFileAction.setStatusTip('打开图像')
    openFileAction.triggered.connect(qApp.quit)

    saveFileAction = QAction(QIcon('./Icon/save.tif'), '&保存', var)
    saveFileAction.setStatusTip('保存图像')
    saveFileAction.triggered.connect(qApp.quit)

    undoAction = QAction(QIcon('./Icon/undo.tif'), '&撤销', var)
    undoAction.setStatusTip('撤销操作')
    undoAction.triggered.connect(qApp.quit)

    rectangleLassoAction = QAction(QIcon('./Icon/rectangle.tif'), '&矩形套索工具', var)
    rectangleLassoAction.setStatusTip('矩形套索工具')
    rectangleLassoAction.triggered.connect(qApp.quit)

    ellipseLassoAction = QAction(QIcon('./Icon/ellipse.tif'), '&椭圆形套索工具', var)
    ellipseLassoAction.setStatusTip('椭圆形套索工具')
    ellipseLassoAction.triggered.connect(qApp.quit)

    customAction = QAction(QIcon('./Icon/custom.tif'), '&多边形套索工具', var)
    customAction.setStatusTip('多边形工具')
    customAction.triggered.connect(qApp.quit)

    enlargeImageAction = QAction(QIcon('./Icon/custom.tif'), '&图像放大', var)
    enlargeImageAction.setStatusTip('图像放大工具')
    enlargeImageAction.triggered.connect(lambda: enlargeImage(var))

    narrowImageAction = QAction(QIcon('./Icon/custom.tif'), '&图像缩小', var)
    narrowImageAction.setStatusTip('图像缩小工具')
    narrowImageAction.triggered.connect(lambda: narrowImage(var))

    graphcutAction = QAction(QIcon('./Icon/ellipse.png'), '&图切', var)
    graphcutAction.setStatusTip('图切')
    graphcutAction.triggered.connect(qApp.quit)

    thresholdAction = QAction(QIcon('./Icon/ellipse.png'), '&阈值分割', var)
    thresholdAction.setStatusTip('阈值分割')
    thresholdAction.triggered.connect(qApp.quit)

    toolbar = var.addToolBar('Exit')
    toolbar.addAction(openFileAction)
    toolbar.addAction(saveFileAction)
    toolbar.addAction(undoAction)
    toolbar.addAction(rectangleLassoAction)
    toolbar.addAction(ellipseLassoAction)
    toolbar.addAction(customAction)
    toolbar.addAction(enlargeImageAction)
    toolbar.addAction(narrowImageAction)
    toolbar.addAction(graphcutAction)
    toolbar.addAction(thresholdAction)