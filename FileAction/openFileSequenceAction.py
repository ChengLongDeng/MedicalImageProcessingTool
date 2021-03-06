import os, filetype
from PyQt5.QtWidgets import QFileDialog
import logging
from PyQt5.QtGui import QPixmap
from MainGUI.Layout.FileManager import addFileDirectory
from MainGUI.Layout.InformationShowManager import *
from FileAction.readImageByCV import readImage


#判断文件类型
def fileType(filename):

    kind = filetype.guess(filename)
    if kind is None:
        return False

    if kind.extension == 'png' or kind.extension == 'jpg' or kind.extension == 'bmp':
        return True
        # print('File extension: %s' % kind.extension)
        # print('File MIME type: %s' % kind.mime)

def openFileSequence(var):

    try:
        var.im_dir = QFileDialog.getExistingDirectory(None, '打开文件夹', '')
        imageList = os.listdir(var.im_dir)
        var.im_num = 0  #记录图像张数
        flag = False
        var.regular_img = []

        for ilist in imageList:
            temList = var.im_dir + '/' + ilist
            if fileType(temList):
                var.im_num = var.im_num + 1

                imagePixmap = QPixmap.fromImage(readImage(var, temList))
                openImageLayout(var, imagePixmap)  # 打开图像
                var.regular_img.append(temList)     #将符合格式的图像保存起来

                addFileDirectory(var, var.im_dir + '/' + ilist)  # 文件显示列表
                flag = True
        if flag:
            var.statusBar().showMessage("已打开文件夹 '%s'" % var.im_dir)  # 状态栏显示信息

    except Exception as e:
        logging.exception(e)