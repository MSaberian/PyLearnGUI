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
        MainWindow.resize(366, 542)
        MainWindow.setMinimumSize(QSize(366, 542))
        MainWindow.setMaximumSize(QSize(366, 542))
        icon = QIcon()
        icon.addFile(u"hand.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 85, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)

        self.btn1_unvisivable = QPushButton(self.centralwidget)
        self.btn1_unvisivable.setObjectName(u"btn1_unvisivable")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1_unvisivable.sizePolicy().hasHeightForWidth())
        self.btn1_unvisivable.setSizePolicy(sizePolicy)
        self.btn1_unvisivable.setMinimumSize(QSize(112, 112))
        font1 = QFont()
        font1.setPointSize(33)
        self.btn1_unvisivable.setFont(font1)
        self.btn1_unvisivable.setStyleSheet(u"background-color: rgb(0, 170, 0);")

        self.gridLayout.addWidget(self.btn1_unvisivable, 1, 0, 1, 1)

        self.btn_computer = QPushButton(self.centralwidget)
        self.btn_computer.setObjectName(u"btn_computer")
        sizePolicy.setHeightForWidth(self.btn_computer.sizePolicy().hasHeightForWidth())
        self.btn_computer.setSizePolicy(sizePolicy)
        self.btn_computer.setMinimumSize(QSize(112, 112))
        self.btn_computer.setFont(font1)
        self.btn_computer.setStyleSheet(u"background-color: rgb(0, 170, 0);")
        self.btn_computer.setIconSize(QSize(112, 112))

        self.gridLayout.addWidget(self.btn_computer, 1, 1, 1, 1)

        self.btn2_unvisivable = QPushButton(self.centralwidget)
        self.btn2_unvisivable.setObjectName(u"btn2_unvisivable")
        sizePolicy.setHeightForWidth(self.btn2_unvisivable.sizePolicy().hasHeightForWidth())
        self.btn2_unvisivable.setSizePolicy(sizePolicy)
        self.btn2_unvisivable.setMinimumSize(QSize(112, 112))
        self.btn2_unvisivable.setFont(font1)
        self.btn2_unvisivable.setStyleSheet(u"background-color: rgb(0, 170, 0);")

        self.gridLayout.addWidget(self.btn2_unvisivable, 1, 2, 1, 1)

        self.how_win = QLabel(self.centralwidget)
        self.how_win.setObjectName(u"how_win")
        font2 = QFont()
        font2.setFamilies([u"Segoe Print"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.how_win.setFont(font2)
        self.how_win.setStyleSheet(u"background-color: rgb(255, 170, 0);")

        self.gridLayout.addWidget(self.how_win, 2, 0, 1, 3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)

        self.btn3_unvisivable = QPushButton(self.centralwidget)
        self.btn3_unvisivable.setObjectName(u"btn3_unvisivable")
        sizePolicy.setHeightForWidth(self.btn3_unvisivable.sizePolicy().hasHeightForWidth())
        self.btn3_unvisivable.setSizePolicy(sizePolicy)
        self.btn3_unvisivable.setMinimumSize(QSize(112, 112))
        self.btn3_unvisivable.setFont(font1)
        self.btn3_unvisivable.setStyleSheet(u"background-color: rgb(0, 170, 0);")

        self.gridLayout.addWidget(self.btn3_unvisivable, 4, 0, 1, 1)

        self.btn_you = QPushButton(self.centralwidget)
        self.btn_you.setObjectName(u"btn_you")
        sizePolicy.setHeightForWidth(self.btn_you.sizePolicy().hasHeightForWidth())
        self.btn_you.setSizePolicy(sizePolicy)
        self.btn_you.setMinimumSize(QSize(112, 112))
        self.btn_you.setFont(font1)
        self.btn_you.setStyleSheet(u"background-color: rgb(0, 170, 0);")
        self.btn_you.setIconSize(QSize(112, 112))

        self.gridLayout.addWidget(self.btn_you, 4, 1, 1, 1)

        self.btn4_unvisivable = QPushButton(self.centralwidget)
        self.btn4_unvisivable.setObjectName(u"btn4_unvisivable")
        sizePolicy.setHeightForWidth(self.btn4_unvisivable.sizePolicy().hasHeightForWidth())
        self.btn4_unvisivable.setSizePolicy(sizePolicy)
        self.btn4_unvisivable.setMinimumSize(QSize(112, 112))
        self.btn4_unvisivable.setFont(font1)
        self.btn4_unvisivable.setStyleSheet(u"background-color: rgb(0, 170, 0);")

        self.gridLayout.addWidget(self.btn4_unvisivable, 4, 2, 1, 1)

        self.scoreboard = QLabel(self.centralwidget)
        self.scoreboard.setObjectName(u"scoreboard")
        font3 = QFont()
        font3.setFamilies([u"Segoe Print"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.scoreboard.setFont(font3)

        self.gridLayout.addWidget(self.scoreboard, 5, 0, 1, 3)

        self.btn_paper = QPushButton(self.centralwidget)
        self.btn_paper.setObjectName(u"btn_paper")
        sizePolicy.setHeightForWidth(self.btn_paper.sizePolicy().hasHeightForWidth())
        self.btn_paper.setSizePolicy(sizePolicy)
        self.btn_paper.setMinimumSize(QSize(112, 112))
        font4 = QFont()
        font4.setPointSize(13)
        self.btn_paper.setFont(font4)
        self.btn_paper.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"paper.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_paper.setIcon(icon1)
        self.btn_paper.setIconSize(QSize(120, 112))

        self.gridLayout.addWidget(self.btn_paper, 6, 0, 1, 1)

        self.btn_scissors = QPushButton(self.centralwidget)
        self.btn_scissors.setObjectName(u"btn_scissors")
        sizePolicy.setHeightForWidth(self.btn_scissors.sizePolicy().hasHeightForWidth())
        self.btn_scissors.setSizePolicy(sizePolicy)
        self.btn_scissors.setMinimumSize(QSize(112, 112))
        self.btn_scissors.setFont(font1)
        self.btn_scissors.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"scissors.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_scissors.setIcon(icon2)
        self.btn_scissors.setIconSize(QSize(112, 112))

        self.gridLayout.addWidget(self.btn_scissors, 6, 1, 1, 1)

        self.btn_rock = QPushButton(self.centralwidget)
        self.btn_rock.setObjectName(u"btn_rock")
        sizePolicy.setHeightForWidth(self.btn_rock.sizePolicy().hasHeightForWidth())
        self.btn_rock.setSizePolicy(sizePolicy)
        self.btn_rock.setMinimumSize(QSize(112, 112))
        self.btn_rock.setFont(font1)
        self.btn_rock.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"rock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_rock.setIcon(icon3)
        self.btn_rock.setIconSize(QSize(112, 112))

        self.gridLayout.addWidget(self.btn_rock, 6, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 366, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Puuzel 15", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"                           Computer", None))
        self.btn1_unvisivable.setText("")
        self.btn_computer.setText("")
        self.btn2_unvisivable.setText("")
        self.how_win.setText(QCoreApplication.translate("MainWindow", u"               Who won?", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"                              player", None))
        self.btn3_unvisivable.setText("")
        self.btn_you.setText("")
        self.btn4_unvisivable.setText("")
        self.scoreboard.setText(QCoreApplication.translate("MainWindow", u"     You: 0       Ties: 0          Computer: 0", None))
        self.btn_paper.setText("")
        self.btn_scissors.setText("")
        self.btn_rock.setText("")
    # retranslateUi

