# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(522, 517)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.upperThresh = QSlider(self.centralwidget)
        self.upperThresh.setObjectName(u"upperThresh")
        self.upperThresh.setGeometry(QRect(9, 40, 391, 22))
        self.upperThresh.setMaximum(255)
        self.upperThresh.setOrientation(Qt.Horizontal)
        self.lowerTheresh = QSlider(self.centralwidget)
        self.lowerTheresh.setObjectName(u"lowerTheresh")
        self.lowerTheresh.setGeometry(QRect(10, 90, 391, 22))
        self.lowerTheresh.setMaximum(255)
        self.lowerTheresh.setOrientation(Qt.Horizontal)
        self.erode = QSlider(self.centralwidget)
        self.erode.setObjectName(u"erode")
        self.erode.setGeometry(QRect(10, 240, 391, 22))
        self.erode.setMaximum(15)
        self.erode.setOrientation(Qt.Horizontal)
        self.dilate = QSlider(self.centralwidget)
        self.dilate.setObjectName(u"dilate")
        self.dilate.setGeometry(QRect(10, 310, 391, 22))
        self.dilate.setMaximum(15)
        self.dilate.setOrientation(Qt.Horizontal)
        self.medianBulr = QSlider(self.centralwidget)
        self.medianBulr.setObjectName(u"medianBulr")
        self.medianBulr.setGeometry(QRect(10, 380, 391, 22))
        self.medianBulr.setMinimum(1)
        self.medianBulr.setMaximum(15)
        self.medianBulr.setValue(3)
        self.medianBulr.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 111, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(410, 40, 141, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(410, 90, 141, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 210, 111, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 280, 111, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 350, 131, 16))
        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(10, 420, 121, 24))
        self.adaptiveThresholdBlock = QSlider(self.centralwidget)
        self.adaptiveThresholdBlock.setObjectName(u"adaptiveThresholdBlock")
        self.adaptiveThresholdBlock.setGeometry(QRect(10, 140, 391, 22))
        self.adaptiveThresholdBlock.setMinimum(1)
        self.adaptiveThresholdBlock.setMaximum(300)
        self.adaptiveThresholdBlock.setSingleStep(2)
        self.adaptiveThresholdBlock.setOrientation(Qt.Horizontal)
        self.adaptiveThresholdConstant = QSlider(self.centralwidget)
        self.adaptiveThresholdConstant.setObjectName(u"adaptiveThresholdConstant")
        self.adaptiveThresholdConstant.setGeometry(QRect(10, 180, 391, 22))
        self.adaptiveThresholdConstant.setMaximum(300)
        self.adaptiveThresholdConstant.setOrientation(Qt.Horizontal)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(410, 140, 141, 16))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(410, 180, 141, 16))
        self.recognizeButton = QPushButton(self.centralwidget)
        self.recognizeButton.setObjectName(u"recognizeButton")
        self.recognizeButton.setGeometry(QRect(150, 420, 81, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 522, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u043e\u0433\u043e\u0432\u044b\u0439 \u0430\u043d\u0430\u043b\u0438\u0437", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u0445\u043d\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u0436\u043d\u0435\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0440\u0443\u0448\u0435\u043d\u0438\u0435", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0434\u0438\u0430\u043d\u043d\u043e\u0435 \u0440\u0430\u0437\u043c\u044b\u0442\u0438\u0435", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043b\u043e\u043a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0441\u0442\u0430\u043d\u0442\u0430", None))
        self.recognizeButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u0442\u044c", None))
    # retranslateUi

