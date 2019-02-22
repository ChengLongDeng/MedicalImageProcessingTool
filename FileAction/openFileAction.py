from PyQt5.QtWidgets import QFileDialog
import os, filetype
import logging
from PyQt5.QtGui import QPixmap
from MainGUI.Layout.InformationShowManager import *
from MainGUI.Layout.FileManager import showOutputInfor
from FileAction.readImageByCV import readImage

# 判断文件类型
def fileType(filename):

    kind = filetype.guess(filename)
    if kind is None:
        return False

    if kind.extension == 'png' or kind.extension == 'jpg' or kind.extension == 'bmp':
        return True
        # print('File extension: %s' % kind.extension)
        # print('File MIME type: %s' % kind.mime)

# 打开文件
def openFile(var):

    try:
        var.im_path, _ = QFileDialog.getOpenFileName(None, '打开文件', '', 'Image Files(*.png *.jpg *.bmp)')

        if not os.path.exists(var.im_path):             # 判断路径是否存在
            showOutputInfor(var, '201', '')             # 显示路径不存在信息
            return

        if fileType(var.im_path):                                       # 判断打开的图像是否是.png, .jpg, .bmp

            var.imagePixmap = QPixmap.fromImage(readImage(var, var.im_path))
            openImageLayout(var, var.imagePixmap)                       # 打开图像

            showOutputInfor(var, '100', var.im_path)                    # 显示打开文件信息
            var.statusBar().showMessage("打开文件 '%s'" % var.im_path)   # 状态栏显示信息
            setLuminanceStatus(var)                                      # 调节亮度

            var.imageInforDock.raise_()                                 # 将像素信息Dock显示出来
        else:
            showOutputInfor(var, '300', var.im_path)                    # 显示图像格式不正确信息
            return

    except Exception as e:
        logging.exception(e)

# 打开下一个文件
def openNextFile(var):

    # 判断是否打开文件
    flag = True
    try:
        var.im_path
    except Exception as e:
        flag = False

    if not flag:
        showOutputInfor(var, '202', '')                                                 # 显示路径不存在信息
        return

    else:
        try:
            if not os.path.exists(var.im_path):                                          # 判断路径是否存在
                showOutputInfor(var, '201', '')                                         # 显示路径不存在信息
                return

            imageList = os.listdir(os.path.split(var.im_path)[0])
            loc = imageList.index(os.path.split(var.im_path)[1])

            if loc >= (len(imageList) - 1):
                loc = 0

                while True:
                    if loc > (len(imageList) - 1):
                        loc = 0
                    var.im_path = os.path.split(var.im_path)[0] + '/' + imageList[loc]
                    if fileType(var.im_path):
                        imagePixmap = QPixmap.fromImage(readImage(var, os.path.split(var.im_path)[0] + '/' + imageList[loc]))
                        # imagePixmap = QPixmap(os.path.split(var.im_path)[0] + '/' + imageList[loc])
                        openImageLayout(var, imagePixmap)  # 打开图像

                        showOutputInfor(var, '100', os.path.split(var.im_path)[0] + '/' + imageList[loc])      # 将打开文件信息显示出来
                        var.statusBar().showMessage("打开文件 '%s'" % var.im_path)                     # 状态栏显示信息
                        break
                    else:
                        loc = loc + 1

            else:
                loc = loc + 1

                while True:
                    if loc > (len(imageList) - 1):
                        loc = 0
                    var.im_path = os.path.split(var.im_path)[0] + '/' + imageList[loc]
                    if fileType(var.im_path):
                        imagePixmap = QPixmap.fromImage(readImage(var, os.path.split(var.im_path)[0] + '/' + imageList[loc]))
                        # imagePixmap = QPixmap(os.path.split(var.im_path)[0] + '/' + imageList[loc])
                        openImageLayout(var, imagePixmap)  # 打开图像

                        showOutputInfor(var, '100', os.path.split(var.im_path)[0] + '/' + imageList[loc])   # 将打开文件信息显示出来
                        var.statusBar().showMessage("打开文件 '%s'" % var.im_path)                         # 状态栏显示信息
                        break
                    else:
                        loc = loc + 1

        except Exception as e:
            logging.exception(e)