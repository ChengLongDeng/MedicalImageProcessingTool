from PyQt5.QtWidgets import QMessageBox
import cv2

def saveFile(var):

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
        # filename, _ = QFileDialog.getSaveFileName(None, "选择保存的文件路径", var.im_path, "Image Files(*.png *.jpg *.bmp)")
        cv2.imwrite(var.im_path, var.img)

        var.statusBar().showMessage("保存 '%s'" % var.im_path, 2000)