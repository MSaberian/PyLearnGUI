# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(419, 478)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color:rgb(100,100, 100);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sum = QPushButton(self.centralwidget)
        self.sum.setObjectName(u"sum")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sum.sizePolicy().hasHeightForWidth())
        self.sum.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(40)
        self.sum.setFont(font)
        self.sum.setStyleSheet(u"background-color:rgb(150,150, 150);")

        self.gridLayout.addWidget(self.sum, 3, 4, 1, 1)

        self.n9 = QPushButton(self.centralwidget)
        self.n9.setObjectName(u"n9")
        sizePolicy.setHeightForWidth(self.n9.sizePolicy().hasHeightForWidth())
        self.n9.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.n9.setFont(font1)
        self.n9.setStyleSheet(u"background-color:rgb(120,120, 120);")

        self.gridLayout.addWidget(self.n9, 4, 2, 1, 1)

        self.cot = QPushButton(self.centralwidget)
        self.cot.setObjectName(u"cot")
        sizePolicy.setHeightForWidth(self.cot.sizePolicy().hasHeightForWidth())
        self.cot.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(False)
        self.cot.setFont(font2)
        self.cot.setStyleSheet(u"background-color:rgb(150,150, 150);")

        self.gridLayout.addWidget(self.cot, 1, 3, 1, 1)

        self.n0 = QPushButton(self.centralwidget)
        self.n0.setObjectName(u"n0")
        sizePolicy.setHeightForWidth(self.n0.sizePolicy().hasHeightForWidth())
        self.n0.setSizePolicy(sizePolicy)
        self.n0.setFont(font1)
        self.n0.setStyleSheet(u"background-color:rgb(120,120, 120);")

        self.gridLayout.addWidget(self.n0, 5, 1, 1, 1)

        self.n7 = QPushButton(self.centralwidget)
        self.n7.setObjectName(u"n7")
        sizePolicy.setHeightForWidth(self.n7.sizePolicy().hasHeightForWidth())
        self.n7.setSizePolicy(sizePolicy)
        self.n7.setFont(font1)
        self.n7.setStyleSheet(u"background-color:rgb(120,120, 120);")

        self.gridLayout.addWidget(self.n7, 4, 0, 1, 1)

        self.sin = QPushButton(self.centralwidget)
        self.sin.setObjectName(u"sin")
        sizePolicy.setHeightForWidth(self.sin.sizePolicy().hasHeightForWidth())
        self.sin.setSizePolicy(sizePolicy)
        self.sin.setFont(font2)
        self.sin.setStyleSheet(u"background-color:rgb(150,150, 150);")

        self.gridLayout.addWidget(self.sin, 1, 0, 1, 1)

        self.equal = QPushButton(self.centralwidget)
        self.equal.setObjectName(u"equal")
        sizePolicy.setHeightForWidth(self.equal.sizePolicy().hasHeightForWidth())
        self.equal.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(40)
        font3.setBold(False)
        self.equal.setFont(font3)
        self.equal.setStyleSheet(u"background-color:rgb(160,160, 160);")

        self.gridLayout.addWidget(self.equal, 5, 4, 1, 1)

        self.log = QPushButton(self.centralwidget)
        self.log.setObjectName(u"log")
        sizePolicy.setHeightForWidth(self.log.sizePolicy().hasHeightForWidth())
        self.log.setSizePolicy(sizePolicy)
        self.log.setFont(font2)
        self.log.setStyleSheet(u"background-color:rgb(150,150, 150);")

        self.gridLayout.addWidget(self.log, 1, 4, 1, 1)

        self.n5 = QPushButton(self.centralwidget)
        self.n5.setObjectName(u"n5")
        sizePolicy.setHeightForWidth(self.n5.sizePolicy().hasHeightForWidth())
        self.n5.setSizePolicy(sizePolicy)
        self.n5.setFont(font1)
        self.n5.setStyleSheet(u"background-color:rgb(120,120, 120);")

        self.gridLayout.addWidget(self.n5, 3, 1, 1, 1)

        self.textbox = QLineEdit(self.centralwidget)
        self.textbox.setObjectName(u"textbox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textbox.sizePolicy().hasHeightForWidth())
        self.textbox.setSizePolicy(sizePolicy1)
        self.textbox.setFont(font1)
        self.textbox.setStyleSheet(u"background-color:rgb(170,170, 170);")
        self.textbox.setReadOnly(False)

        self.gridLayout.addWidget(self.textbox, 0, 0, 1, 5)

        self.n2 = QPushButton(self.centralwidget)
        self.n2.setObjectName(u"n2")
        sizePolicy.setHeightForWidth(self.n2.sizePolicy().hasHeightForWidth())
        self.n2.setSizePolicy(sizePolicy)
        self.n2.setFont(font1)
        self.n2.setStyleSheet(u"background-color:rgb(120,120, 120);")

        self.gridLayout.addWidget(self.n2, 2, 1, 1, 1)

        self.n6 = QPushButton(self.centralwidget)
        self.n6.setObjectName(u"n6")
        sizePolicy.setHeightForWidth(self.n6.sizePolicy().hasHeightForWidth())
        self.n6.setSizePolicy(sizePolicy)
        self.n6.setFont(font1)
        self.n6.setStyleSheet(u"background-color:rgb(120,120, 120);")

        self.gridLayout.addWidget(self.n6, 3, 2, 1, 1)

        self.dev = QPushButton(self.centralwidget)
        self.dev.setObjectName(u"dev")
        sizePolicy.setHeightForWidth(self.dev.sizePolicy().hasHeightForWidth())
        self.dev.setSizePolicy(sizePolicy)
        self.dev.setFont(font)
        self.dev.setStyleSheet(u"background-color:rgb(150,150, 150);")

        self.gridLayout.addWidget(self.dev, 4, 3, 1, 1)

        self.cos = QPushButton(self.centralwidget)
        self.cos.setObjectName(u"cos")
        sizePolicy.setHeightForWidth(self.cos.sizePolicy().hasHeightForWidth())
        self.cos.setSizePolicy(sizePolicy)
        self.cos.setFont(font2)
        self.cos.setStyleSheet(u"background-color:rgb(150,150, 150);")

        self.gridLayout.addWidget(self.cos, 1, 1, 1, 1)

        self.AC = QPushButton(self.centralwidget)
        self.AC.setObjectName(u"AC")
        sizePolicy.setHeightForWidth(self.AC.sizePolicy().hasHeightForWidth())
        self.AC.setSizePolicy(sizePolicy)
        self.AC.setFont(font2)
        self.AC.setStyleSheet(u"background-color:rgb(150,150, 150);")

        self.gridLayout.addWidget(self.AC, 2, 4, 1, 1)

        self.n8 = QPushButton(self.centralwidget)
        self.n8.setObjectName(u"n8")
        sizePolicy.setHeightForWidth(self.n8.sizePolicy().hasHeightForWidth())
        self.n8.setSizePolicy(sizePolicy)
        self.n8.setFont(font1)
        self.n8.setStyleSheet(u"background-color:rgb(120,120, 120);")

        self.gridLayout.addWidget(self.n8, 4, 1, 1, 1)

        self.n4 = QPushButton(self.centralwidget)
        self.n4.setObjectName(u"n4")
        sizePolicy.setHeightForWidth(self.n4.sizePolicy().hasHeightForWidth())
        self.n4.setSizePolicy(sizePolicy)
        self.n4.setFont(font1)
        self.n4.setStyleSheet(u"background-color:rgb(120,120, 120);")

        self.gridLayout.addWidget(self.n4, 3, 0, 1, 1)

        self.n1 = QPushButton(self.centralwidget)
        self.n1.setObjectName(u"n1")
        sizePolicy.setHeightForWidth(self.n1.sizePolicy().hasHeightForWidth())
        self.n1.setSizePolicy(sizePolicy)
        self.n1.setFont(font1)
        self.n1.setStyleSheet(u"background-color:rgb(120,120, 120);")

        self.gridLayout.addWidget(self.n1, 2, 0, 1, 1)

        self.PN = QPushButton(self.centralwidget)
        self.PN.setObjectName(u"PN")
        sizePolicy.setHeightForWidth(self.PN.sizePolicy().hasHeightForWidth())
        self.PN.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        self.PN.setFont(font4)
        self.PN.setStyleSheet(u"background-color:rgb(150,150, 150);")

        self.gridLayout.addWidget(self.PN, 5, 0, 1, 1)

        self.sqrt = QPushButton(self.centralwidget)
        self.sqrt.setObjectName(u"sqrt")
        sizePolicy.setHeightForWidth(self.sqrt.sizePolicy().hasHeightForWidth())
        self.sqrt.setSizePolicy(sizePolicy)
        self.sqrt.setFont(font2)
        self.sqrt.setStyleSheet(u"background-color:rgb(150,150, 150);")

        self.gridLayout.addWidget(self.sqrt, 2, 3, 1, 1)

        self.sub = QPushButton(self.centralwidget)
        self.sub.setObjectName(u"sub")
        sizePolicy.setHeightForWidth(self.sub.sizePolicy().hasHeightForWidth())
        self.sub.setSizePolicy(sizePolicy)
        self.sub.setFont(font)
        self.sub.setMouseTracking(False)
        self.sub.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.sub.setLayoutDirection(Qt.LeftToRight)
        self.sub.setStyleSheet(u"background-color:rgb(150,150, 150);")

        self.gridLayout.addWidget(self.sub, 4, 4, 1, 1)

        self.percent = QPushButton(self.centralwidget)
        self.percent.setObjectName(u"percent")
        sizePolicy.setHeightForWidth(self.percent.sizePolicy().hasHeightForWidth())
        self.percent.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setPointSize(30)
        font5.setBold(False)
        self.percent.setFont(font5)
        self.percent.setStyleSheet(u"background-color:rgb(150,150, 150);")

        self.gridLayout.addWidget(self.percent, 5, 3, 1, 1)

        self.n3 = QPushButton(self.centralwidget)
        self.n3.setObjectName(u"n3")
        sizePolicy.setHeightForWidth(self.n3.sizePolicy().hasHeightForWidth())
        self.n3.setSizePolicy(sizePolicy)
        self.n3.setFont(font1)
        self.n3.setStyleSheet(u"background-color:rgb(120,120, 120);")

        self.gridLayout.addWidget(self.n3, 2, 2, 1, 1)

        self.dot = QPushButton(self.centralwidget)
        self.dot.setObjectName(u"dot")
        sizePolicy.setHeightForWidth(self.dot.sizePolicy().hasHeightForWidth())
        self.dot.setSizePolicy(sizePolicy)
        self.dot.setFont(font1)
        self.dot.setStyleSheet(u"background-color:rgb(150,150, 150);")

        self.gridLayout.addWidget(self.dot, 5, 2, 1, 1)

        self.tan = QPushButton(self.centralwidget)
        self.tan.setObjectName(u"tan")
        sizePolicy.setHeightForWidth(self.tan.sizePolicy().hasHeightForWidth())
        self.tan.setSizePolicy(sizePolicy)
        self.tan.setFont(font2)
        self.tan.setStyleSheet(u"background-color:rgb(150,150, 150);")

        self.gridLayout.addWidget(self.tan, 1, 2, 1, 1)

        self.mul = QPushButton(self.centralwidget)
        self.mul.setObjectName(u"mul")
        sizePolicy.setHeightForWidth(self.mul.sizePolicy().hasHeightForWidth())
        self.mul.setSizePolicy(sizePolicy)
        self.mul.setFont(font)
        self.mul.setMouseTracking(False)
        self.mul.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.mul.setLayoutDirection(Qt.LeftToRight)
        self.mul.setStyleSheet(u"background-color:rgb(150,150, 150);")

        self.gridLayout.addWidget(self.mul, 3, 3, 1, 1)

        self.gridLayout.setRowStretch(0, 7)
        self.gridLayout.setRowStretch(1, 5)
        self.gridLayout.setRowStretch(2, 7)
        self.gridLayout.setRowStretch(3, 7)
        self.gridLayout.setRowStretch(4, 7)
        self.gridLayout.setRowStretch(5, 7)
        self.gridLayout.setColumnStretch(0, 7)
        self.gridLayout.setColumnStretch(1, 7)
        self.gridLayout.setColumnStretch(2, 7)
        self.gridLayout.setColumnStretch(3, 5)
        self.gridLayout.setColumnStretch(4, 5)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 419, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.sum.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.n9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.cot.setText(QCoreApplication.translate("MainWindow", u"cot", None))
        self.n0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.n7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.sin.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.log.setText(QCoreApplication.translate("MainWindow", u"log", None))
        self.n5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.textbox.setText("")
        self.n2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.n6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.dev.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.cos.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.AC.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.n8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.n4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.n1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.PN.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.sqrt.setText(QCoreApplication.translate("MainWindow", u"sqrt", None))
        self.sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.percent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.n3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.tan.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.mul.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
    # retranslateUi

