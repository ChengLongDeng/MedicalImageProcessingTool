from PyQt5.QtWidgets import QMessageBox, QFileDialog
import cv2

def saveAsFile(var):

    # 判断是否打开文件
    flag = True
    try:
        var.im_path
    except Exception as e:
        flag = False

    if not flag:
        QMessageBox.information(None, "提示", "请先打开图像", QMessageBox.Yes)  # 使用infomation信息框
        return
    else:
        filename, _ = QFileDialog.getSaveFileName(None, "选择保存的文件路径", var.im_path, "Image Files(*.png *.jpg *.bmp)")

        cv2.imwrite(filename, var.img)

        var.statusBar().showMessage("另存为 '%s'" % filename, 2000)