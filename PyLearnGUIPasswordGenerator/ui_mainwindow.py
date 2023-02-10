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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(315, 216)
        MainWindow.setMinimumSize(QSize(170, 0))
        icon = QIcon()
        icon.addFile(u"passicon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 105, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.rbn_1 = QRadioButton(self.centralwidget)
        self.rbn_1.setObjectName(u"rbn_1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbn_1.sizePolicy().hasHeightForWidth())
        self.rbn_1.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Bahnschrift Condensed"])
        font.setPointSize(16)
        self.rbn_1.setFont(font)
        self.rbn_1.setChecked(True)

        self.gridLayout.addWidget(self.rbn_1, 0, 0, 1, 1)

        self.rbn_2 = QRadioButton(self.centralwidget)
        self.rbn_2.setObjectName(u"rbn_2")
        sizePolicy.setHeightForWidth(self.rbn_2.sizePolicy().hasHeightForWidth())
        self.rbn_2.setSizePolicy(sizePolicy)
        self.rbn_2.setFont(font)

        self.gridLayout.addWidget(self.rbn_2, 1, 0, 1, 1)

        self.rbn_3 = QRadioButton(self.centralwidget)
        self.rbn_3.setObjectName(u"rbn_3")
        sizePolicy.setHeightForWidth(self.rbn_3.sizePolicy().hasHeightForWidth())
        self.rbn_3.setSizePolicy(sizePolicy)
        self.rbn_3.setFont(font)

        self.gridLayout.addWidget(self.rbn_3, 2, 0, 1, 1)

        self.btn_generate = QPushButton(self.centralwidget)
        self.btn_generate.setObjectName(u"btn_generate")
        sizePolicy.setHeightForWidth(self.btn_generate.sizePolicy().hasHeightForWidth())
        self.btn_generate.setSizePolicy(sizePolicy)
        self.btn_generate.setFont(font)
        self.btn_generate.setStyleSheet(u"background-color: rgb(255, 65, 0);")

        self.gridLayout.addWidget(self.btn_generate, 3, 0, 1, 1)

        self.linePassword = QLineEdit(self.centralwidget)
        self.linePassword.setObjectName(u"linePassword")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.linePassword.sizePolicy().hasHeightForWidth())
        self.linePassword.setSizePolicy(sizePolicy1)
        self.linePassword.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(12)
        self.linePassword.setFont(font1)
        self.linePassword.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.linePassword, 4, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 315, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.rbn_1.setText(QCoreApplication.translate("MainWindow", u"Standard Strength ", None))
        self.rbn_2.setText(QCoreApplication.translate("MainWindow", u"Extra Strong", None))
        self.rbn_3.setText(QCoreApplication.translate("MainWindow", u"Super Strong", None))
        self.btn_generate.setText(QCoreApplication.translate("MainWindow", u"Generate Password", None))
        self.linePassword.setText("")
    # retranslateUi

