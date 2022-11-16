# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_pic(object):
    def setupUi(self, pic):
        if not pic.objectName():
            pic.setObjectName(u"pic")
        pic.resize(473, 178)
        self.picBox = QLabel(pic)
        self.picBox.setObjectName(u"picBox")
        self.picBox.setGeometry(QRect(10, 10, 451, 101))
        self.text = QLabel(pic)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(10, 120, 451, 31))

        self.retranslateUi(pic)

        QMetaObject.connectSlotsByName(pic)
    # setupUi

    def retranslateUi(self, pic):
        pic.setWindowTitle(QCoreApplication.translate("pic", u"pic", None))
        self.picBox.setText(QCoreApplication.translate("pic", u"TextLabel", None))
        self.text.setText(QCoreApplication.translate("pic", u"TextLabel", None))
    # retranslateUi

