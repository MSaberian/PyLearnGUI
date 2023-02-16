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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(247, 568)
        MainWindow.setMinimumSize(QSize(247, 568))
        MainWindow.setMaximumSize(QSize(268, 576))
        icon = QIcon()
        icon.addFile(u"ohhand.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn1_unvisivable = QPushButton(self.centralwidget)
        self.btn1_unvisivable.setObjectName(u"btn1_unvisivable")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1_unvisivable.sizePolicy().hasHeightForWidth())
        self.btn1_unvisivable.setSizePolicy(sizePolicy)
        self.btn1_unvisivable.setMinimumSize(QSize(56, 112))
        self.btn1_unvisivable.setMaximumSize(QSize(56, 112))
        font = QFont()
        font.setPointSize(33)
        self.btn1_unvisivable.setFont(font)
        self.btn1_unvisivable.setStyleSheet(u"background-color: rgb(0, 170, 0);")

        self.gridLayout.addWidget(self.btn1_unvisivable, 4, 0, 1, 1)

        self.btn_computer1 = QPushButton(self.centralwidget)
        self.btn_computer1.setObjectName(u"btn_computer1")
        sizePolicy.setHeightForWidth(self.btn_computer1.sizePolicy().hasHeightForWidth())
        self.btn_computer1.setSizePolicy(sizePolicy)
        self.btn_computer1.setMinimumSize(QSize(112, 112))
        self.btn_computer1.setMaximumSize(QSize(112, 112))
        self.btn_computer1.setFont(font)
        self.btn_computer1.setStyleSheet(u"background-color: rgb(0, 170, 0);")
        self.btn_computer1.setIconSize(QSize(112, 112))

        self.gridLayout.addWidget(self.btn_computer1, 1, 0, 1, 2)

        self.scoreboard_2 = QLabel(self.centralwidget)
        self.scoreboard_2.setObjectName(u"scoreboard_2")
        font1 = QFont()
        font1.setFamilies([u"Segoe Print"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.scoreboard_2.setFont(font1)

        self.gridLayout.addWidget(self.scoreboard_2, 6, 0, 1, 4)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 4)

        self.scoreboard = QLabel(self.centralwidget)
        self.scoreboard.setObjectName(u"scoreboard")
        self.scoreboard.setFont(font1)

        self.gridLayout.addWidget(self.scoreboard, 5, 0, 1, 4)

        self.btn_onhand = QPushButton(self.centralwidget)
        self.btn_onhand.setObjectName(u"btn_onhand")
        sizePolicy.setHeightForWidth(self.btn_onhand.sizePolicy().hasHeightForWidth())
        self.btn_onhand.setSizePolicy(sizePolicy)
        self.btn_onhand.setMinimumSize(QSize(112, 112))
        self.btn_onhand.setMaximumSize(QSize(112, 112))
        font3 = QFont()
        font3.setPointSize(13)
        self.btn_onhand.setFont(font3)
        self.btn_onhand.setStyleSheet(u"")
        self.btn_onhand.setIcon(icon)
        self.btn_onhand.setIconSize(QSize(120, 112))

        self.gridLayout.addWidget(self.btn_onhand, 7, 0, 1, 2)

        self.btn_computer2 = QPushButton(self.centralwidget)
        self.btn_computer2.setObjectName(u"btn_computer2")
        sizePolicy.setHeightForWidth(self.btn_computer2.sizePolicy().hasHeightForWidth())
        self.btn_computer2.setSizePolicy(sizePolicy)
        self.btn_computer2.setMinimumSize(QSize(112, 112))
        self.btn_computer2.setMaximumSize(QSize(112, 112))
        self.btn_computer2.setFont(font)
        self.btn_computer2.setStyleSheet(u"background-color: rgb(0, 170, 0);")
        self.btn_computer2.setIconSize(QSize(112, 112))

        self.gridLayout.addWidget(self.btn_computer2, 1, 2, 1, 2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 3)

        self.btn2_unvisivable = QPushButton(self.centralwidget)
        self.btn2_unvisivable.setObjectName(u"btn2_unvisivable")
        sizePolicy.setHeightForWidth(self.btn2_unvisivable.sizePolicy().hasHeightForWidth())
        self.btn2_unvisivable.setSizePolicy(sizePolicy)
        self.btn2_unvisivable.setMinimumSize(QSize(56, 112))
        self.btn2_unvisivable.setMaximumSize(QSize(56, 112))
        self.btn2_unvisivable.setFont(font)
        self.btn2_unvisivable.setStyleSheet(u"background-color: rgb(0, 170, 0);")

        self.gridLayout.addWidget(self.btn2_unvisivable, 4, 3, 1, 1)

        self.how_win = QLabel(self.centralwidget)
        self.how_win.setObjectName(u"how_win")
        font4 = QFont()
        font4.setFamilies([u"Segoe Print"])
        font4.setPointSize(15)
        font4.setBold(True)
        self.how_win.setFont(font4)
        self.how_win.setStyleSheet(u"background-color: rgb(255, 170, 0);")

        self.gridLayout.addWidget(self.how_win, 2, 0, 1, 4)

        self.btn_backhand = QPushButton(self.centralwidget)
        self.btn_backhand.setObjectName(u"btn_backhand")
        sizePolicy.setHeightForWidth(self.btn_backhand.sizePolicy().hasHeightForWidth())
        self.btn_backhand.setSizePolicy(sizePolicy)
        self.btn_backhand.setMinimumSize(QSize(112, 112))
        self.btn_backhand.setMaximumSize(QSize(112, 112))
        self.btn_backhand.setFont(font)
        self.btn_backhand.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"backhand.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_backhand.setIcon(icon1)
        self.btn_backhand.setIconSize(QSize(112, 112))

        self.gridLayout.addWidget(self.btn_backhand, 7, 2, 1, 2)

        self.btn_you = QPushButton(self.centralwidget)
        self.btn_you.setObjectName(u"btn_you")
        sizePolicy.setHeightForWidth(self.btn_you.sizePolicy().hasHeightForWidth())
        self.btn_you.setSizePolicy(sizePolicy)
        self.btn_you.setMinimumSize(QSize(112, 112))
        self.btn_you.setMaximumSize(QSize(56, 112))
        self.btn_you.setFont(font)
        self.btn_you.setStyleSheet(u"background-color: rgb(0, 170, 0);")
        self.btn_you.setIconSize(QSize(112, 112))

        self.gridLayout.addWidget(self.btn_you, 4, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 247, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Palam Polum Pilish", None))
        self.btn1_unvisivable.setText("")
        self.btn_computer1.setText("")
        self.scoreboard_2.setText(QCoreApplication.translate("MainWindow", u" Ties: 0    Computer2: 0   ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"  Computer1     Computer2", None))
        self.scoreboard.setText(QCoreApplication.translate("MainWindow", u"  You: 0    Computer1: 0        ", None))
        self.btn_onhand.setText("")
        self.btn_computer2.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"                     player", None))
        self.btn2_unvisivable.setText("")
        self.how_win.setText(QCoreApplication.translate("MainWindow", u"          Who won?", None))
        self.btn_backhand.setText("")
        self.btn_you.setText("")
    # retranslateUi

