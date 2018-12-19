from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os, filetype
import logging
from MainGUI.InformationShowManager import *
from MainGUI.FileManager import addFileDirectory
from FileAction.readImageByCV import readImage
from MainGUI.ImageInforShow import setWidgetStatus

#判断文件类型
def fileType(filename):

    kind = filetype.guess(filename)
    if kind is None:
        return False

    if kind.extension == 'png' or kind.extension == 'jpg' or kind.extension == 'bmp':
        return True
        # print('File extension: %s' % kind.extension)
        # print('File MIME type: %s' % kind.mime)

#打开文件
def openFile(var):

    try:
        var.im_path, _ = QFileDialog.getOpenFileName(None, '打开文件', '', 'Image Files(*.png *.jpg *.bmp)')

        if not os.path.exists(var.im_path):         #判断路径是否存在
            # QMessageBox.information(None, "提示", "该路径不存在", QMessageBox.Yes)  # 使用infomation信息框
            box_dir = QMessageBox(QMessageBox.Information, "提示", "该路径不存在")  # 将Yes换成"确定"
            box_dir.addButton(str('确定'), QMessageBox.YesRole)
            box_dir.exec_()
            return

        if fileType(var.im_path):       #判断打开的图像是否是.png, .jpg, .bmp

            imagePixmap = QPixmap.fromImage(readImage(var, var.im_path))
            openImageLayout(var, imagePixmap)                       #打开图像

            addFileDirectory(var, var.im_path)                      #文件显示列表
            var.statusBar().showMessage("已打开图像 '%s'" % var.im_path) #状态栏显示信息
            setLuminanceStatus(var)                                    #调节亮度
            setWidgetStatus(var)                                        #图像像素信息
        else:
            # QMessageBox.information(None, "提示", "无法读取该文件类型，只能读取（*.png, *.jpg, *.bmp）类型", QMessageBox.Yes)
            box_type = QMessageBox(QMessageBox.Information, "提示", "无法读取该文件类型，只能读取（*.png, *.jpg, *.bmp）类型")  # 将Yes换成"确定"
            box_type.addButton(str('确定'), QMessageBox.YesRole)
            box_type.exec_()
            return

    except Exception as e:
        logging.exception(e)

#打开下一个文件
def openNextFile(var):

    #判断是否打开文件
    flag = True
    try:
        var.im_path
    except Exception as e:
        flag = False

    if not flag:
        # QMessageBox.warning(None, "提示", "请先打开图像", QMessageBox.Yes)  # 使用warning信息框
        box = QMessageBox(QMessageBox.Information, "提示", "请先打开图像")      #将Yes换成"确定"
        box.addButton(str('确定'), QMessageBox.YesRole)
        box.exec_()
        return

    else:
        try:
            if not os.path.exists(var.im_path):         # 判断路径是否存在
                # QMessageBox.information(None, "提示", "路径不存在", QMessageBox.Yes)  # 使用infomation信息框
                box_dir = QMessageBox(QMessageBox.Information, "提示", "路径不存在")  # 将Yes换成"确定"
                box_dir.addButton(str('确定'), QMessageBox.YesRole)
                box_dir.exec_()
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

                        addFileDirectory(var, os.path.split(var.im_path)[0] + '/' + imageList[loc])  # 文件显示列表
                        var.statusBar().showMessage("已打开图像 '%s'" % var.im_path)  # 状态栏显示信息
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

                        addFileDirectory(var, os.path.split(var.im_path)[0] + '/' + imageList[loc])  # 文件显示列表
                        var.statusBar().showMessage("已打开图像 '%s'" % var.im_path)  # 状态栏显示信息
                        break
                    else:
                        loc = loc + 1

        except Exception as e:
            logging.exception(e)