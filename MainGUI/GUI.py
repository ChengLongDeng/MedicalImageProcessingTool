from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
import sys
from PyQt5.QtCore import Qt
from MainGUI.Layout.MainPageManager import mainLayout
from MainGUI.BarInformation.MenuBar import menubarAchieve
from MainGUI.BarInformation.ToolBar import toolbarAchieve
from MainGUI.BarInformation.StatusBar import statusbarAchieve

class GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):

        menubarAchieve(self)                          # 菜单栏
        toolbarAchieve(self)                          # 工具栏
        mainLayout(self)                              # 主页面布局
        statusbarAchieve(self)                        # 状态栏设置

        self.statusBar().showMessage('准备')
        self.setWindowTitle('宫颈癌辅助处理工具')
        self.resize(1100, 1100)
        self.center()
        # self.setStyleSheet('''background-color:white;''')
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.show()

    def center(self):

        screen = QDesktopWidget().screenGeometry()              # 获取屏幕大小
        size = self.geometry()                                  # 获取窗口大小
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) /2)        # 将窗口移动到屏幕中央

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = GUI()
    sys.exit(app.exec_())