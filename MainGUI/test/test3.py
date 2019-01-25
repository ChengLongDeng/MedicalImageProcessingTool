from PIL import Image
import cv2, numpy

from resizeimage import resizeimage


# with open('/Users/dengchenglong/images/000001_03_01_088_11.png', 'r+b') as f:
#     with Image.open(f) as image:
#         cover = resizeimage.resize_cover(image, [800, 800], validate=False)
#         print(image.format)
        # cover.save('/Users/dengchenglong/images/000001_03_01_088_11.png', image.format)

# img = cv2.imread('/Users/dengchenglong/images/000001_03_01_088_55.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img_pil = Image.fromarray(img)
# cover = resizeimage.resize_cover(img_pil, [800, 800], validate=False)
# cover.save('/Users/dengchenglong/images/000001_03_01_088_77.png')

# pil_image = Image.open('/Users/dengchenglong/images/000001_03_01_088_55.png').convert('RGB')
# open_cv_image = numpy.array(pil_image)
# # Convert RGB to BGR
# open_cv_image = open_cv_image[:, :, ::-1].copy()
# print(open_cv_image.shape)


# for i in range(0, 512):
#     for j in range(0, 512):
#         if img[i][j][0] == open_cv_image[i][j][0] and img[i][j][1] == open_cv_image[i][j][1] and img[i][j][2] == open_cv_image[i][j][2]:
#             print(img[i][j])
#             print(open_cv_image[i][j])
#             print('-----------------------')

# cover = resizeimage.resize_cover(img, [800, 800], validate=False)
# cover.save('/Users/dengchenglong/images/000001_03_01_088_11.png')

# img = cv2.imread('/Users/dengchenglong/images/000001_03_01_088.png')
#
# img = cv2.resize(img, (800, 800), 0, 0, interpolation=cv2.INTER_CUBIC)
# cv2.imwrite('/Users/dengchenglong/images/000001_03_01_088_66.png', img)

import sys

from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QApplication
from PyQt5.QtCore import QEvent

class Widget(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.le = QLineEdit()
        lay = QVBoxLayout(self)
        lay.addWidget(self.le)

        self.le.installEventFilter(self)

    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
            # do something
        return QWidget.eventFilter(self, watched, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())