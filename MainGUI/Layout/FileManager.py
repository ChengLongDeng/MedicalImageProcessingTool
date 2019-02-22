from PyQt5.QtWidgets import QListWidget, QDockWidget, QMessageBox
from PyQt5.QtGui import QPixmap, QColor
import os, time
from MainGUI.Layout.InformationShowManager import openImageLayout
from FileAction.readImageByCV import readImage

# 文件显示区域显示
def show(var):

    fileDock = QDockWidget(var)
    var.fileDirectory = QListWidget(var)

    var.fileDirectory.verticalScrollBar()                       # 垂直滚动条
    var.fileDirectory.horizontalScrollBar()                     # 水平滚动条
    # var.fileDirectory.setFixedSize(500, 300)
    # var.fileDirectory.itemDoubleClicked.connect(lambda: fileDirectoryDoubleClicked(var))

    fileDock.setFeatures(QDockWidget.NoDockWidgetFeatures)
    fileDock.setWidget(var.fileDirectory)
    # var.fileDirectory.setStyleSheet("QListWidget{ color:red; }")

    return fileDock

# 显示输出信息
def showOutputInfor(var, flag,  infor):

    if flag == '100':
        var.fileDirectory.addItem(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        var.fileDirectory.addItem('【打开文件】：' + infor)
        var.fileDirectory.item(var.fileDirectory.count() - 1).setForeground(QColor('blue'))
    elif flag == '201':
        var.fileDirectory.addItem(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        var.fileDirectory.addItem("【错误】：文件路径不存在")
        var.fileDirectory.item(var.fileDirectory.count() - 1).setForeground(QColor('red'))
    elif flag == '202':
        var.fileDirectory.addItem(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        var.fileDirectory.addItem('【错误】：请先打开图像')
        var.fileDirectory.item(var.fileDirectory.count() - 1).setForeground(QColor('red'))
    elif flag == '300':
        var.fileDirectory.addItem(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        var.fileDirectory.addItem('【错误】：无法读取 ' + infor + ' 只能读取（*.png, *.jpg, *.bmp）类型图像')
        var.fileDirectory.item(var.fileDirectory.count() - 1).setForeground(QColor('red'))

# 双击响应事件
def fileDirectoryDoubleClicked(var):
    var.im_path = var.fileDirectory.currentItem().text().strip().split('、')[1]
    if not os.path.exists(var.im_path):                                                 # 判断路径是否存在
        # QMessageBox.information(None, "提示", "该文件不存在", QMessageBox.Yes)           # 使用infomation信息框
        box = QMessageBox(QMessageBox.Information, "提示", "该文件不存在")                 # 将Yes换成"确定"
        box.addButton(str('确定'), QMessageBox.YesRole)
        box.exec_()
        # var.fileDirectory.takeItem(var.fileDirectory.currentRow())                    # 将无效的路径删除
        return

    imagePixmap = QPixmap.fromImage(readImage(var, var.im_path))

    openImageLayout(var, imagePixmap)  # 打开图像

# 添加文件路径
def addFileDirectory(var, directory):
    flag = False

    if var.fileDirectory.count() == 0:
        number = var.fileDirectory.count() + 1
        # var.fileDirectory.addItem('              ' + str(number) + '、' + directory)
        var.fileDirectory.addItem(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        var.fileDirectory.addItem('已打开文件 ' + directory)
        var.fileDirectory.addItem('-----------------------------')
    else:
        for i in range(var.fileDirectory.count()):
            if directory == var.fileDirectory.item(i).text().strip().split('、')[1]:
                flag = True
                break

        if flag:
            var.fileDirectory.item(i).setSelected(True)
        else:
            number = var.fileDirectory.count() + 1
            var.fileDirectory.addItem('              ' + str(number) + '、' + directory)
