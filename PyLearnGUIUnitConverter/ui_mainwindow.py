# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(238, 151)
        MainWindow.setMinimumSize(QSize(238, 0))
        icon = QIcon()
        icon.addFile(u"convert_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(1, 145, 153);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe Print"])
        font.setPointSize(12)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.cmb_par = QComboBox(self.centralwidget)
        self.cmb_par.setObjectName(u"cmb_par")
        sizePolicy.setHeightForWidth(self.cmb_par.sizePolicy().hasHeightForWidth())
        self.cmb_par.setSizePolicy(sizePolicy)
        self.cmb_par.setFont(font)
        self.cmb_par.setStyleSheet(u"background-color: rgb(0, 200, 255);")

        self.gridLayout.addWidget(self.cmb_par, 0, 1, 1, 1)

        self.cmb_unit_1 = QComboBox(self.centralwidget)
        self.cmb_unit_1.setObjectName(u"cmb_unit_1")
        sizePolicy.setHeightForWidth(self.cmb_unit_1.sizePolicy().hasHeightForWidth())
        self.cmb_unit_1.setSizePolicy(sizePolicy)
        self.cmb_unit_1.setFont(font)
        self.cmb_unit_1.setStyleSheet(u"background-color: rgb(0, 200, 255);")

        self.gridLayout.addWidget(self.cmb_unit_1, 1, 0, 1, 1)

        self.cmb_unit_2 = QComboBox(self.centralwidget)
        self.cmb_unit_2.setObjectName(u"cmb_unit_2")
        sizePolicy.setHeightForWidth(self.cmb_unit_2.sizePolicy().hasHeightForWidth())
        self.cmb_unit_2.setSizePolicy(sizePolicy)
        self.cmb_unit_2.setFont(font)
        self.cmb_unit_2.setStyleSheet(u"background-color: rgb(0, 200, 255);")

        self.gridLayout.addWidget(self.cmb_unit_2, 1, 1, 1, 1)

        self.lineEdit_1 = QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy1)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setStyleSheet(u"background-color: rgb(0, 200, 255);")

        self.gridLayout.addWidget(self.lineEdit_1, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(0, 200, 255);")
        self.lineEdit_2.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 238, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Unit Converter", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"   Convert", None))
        self.cmb_par.setCurrentText("")
        self.cmb_unit_1.setCurrentText("")
        self.cmb_unit_2.setCurrentText("")
    # retranslateUi

