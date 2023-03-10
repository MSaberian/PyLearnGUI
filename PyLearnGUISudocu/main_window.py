# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(364, 415)
        icon = QIcon()
        icon.addFile(u"sudoku.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.actionlight = QAction(MainWindow)
        self.actionlight.setObjectName(u"actionlight")
        self.actiondark = QAction(MainWindow)
        self.actiondark.setObjectName(u"actiondark")
        self.actionpink = QAction(MainWindow)
        self.actionpink.setObjectName(u"actionpink")
        self.actionpink.setEnabled(False)
        self.actiongreen = QAction(MainWindow)
        self.actiongreen.setObjectName(u"actiongreen")
        self.actiongreen.setEnabled(False)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actioneasy = QAction(MainWindow)
        self.actioneasy.setObjectName(u"actioneasy")
        self.actionnormal = QAction(MainWindow)
        self.actionnormal.setObjectName(u"actionnormal")
        self.actionhard = QAction(MainWindow)
        self.actionhard.setObjectName(u"actionhard")
        self.actionsolve_puzzle = QAction(MainWindow)
        self.actionsolve_puzzle.setObjectName(u"actionsolve_puzzle")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gr_ds = QGridLayout()
        self.gr_ds.setObjectName(u"gr_ds")

        self.gridLayout.addLayout(self.gr_ds, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 364, 22))
        self.menuGame = QMenu(self.menubar)
        self.menuGame.setObjectName(u"menuGame")
        self.menuChane_Mode = QMenu(self.menuGame)
        self.menuChane_Mode.setObjectName(u"menuChane_Mode")
        self.menuNew = QMenu(self.menuGame)
        self.menuNew.setObjectName(u"menuNew")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuGame.addAction(self.menuNew.menuAction())
        self.menuGame.addAction(self.actionOpen_File)
        self.menuGame.addAction(self.menuChane_Mode.menuAction())
        self.menuGame.addSeparator()
        self.menuGame.addAction(self.actionsolve_puzzle)
        self.menuChane_Mode.addAction(self.actionlight)
        self.menuChane_Mode.addAction(self.actiondark)
        self.menuChane_Mode.addAction(self.actionpink)
        self.menuChane_Mode.addAction(self.actiongreen)
        self.menuNew.addAction(self.actioneasy)
        self.menuNew.addAction(self.actionnormal)
        self.menuNew.addAction(self.actionhard)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sudoku", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.actionlight.setText(QCoreApplication.translate("MainWindow", u"light", None))
        self.actiondark.setText(QCoreApplication.translate("MainWindow", u"dark", None))
        self.actionpink.setText(QCoreApplication.translate("MainWindow", u"pink", None))
        self.actiongreen.setText(QCoreApplication.translate("MainWindow", u"green", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actioneasy.setText(QCoreApplication.translate("MainWindow", u"Easy", None))
        self.actionnormal.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.actionhard.setText(QCoreApplication.translate("MainWindow", u"Hard", None))
        self.actionsolve_puzzle.setText(QCoreApplication.translate("MainWindow", u"solve puzzle", None))
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
        self.menuChane_Mode.setTitle(QCoreApplication.translate("MainWindow", u"Chane Mode", None))
        self.menuNew.setTitle(QCoreApplication.translate("MainWindow", u"New...", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

