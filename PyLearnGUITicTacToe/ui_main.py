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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(474, 406)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn1 = QPushButton(self.centralwidget)
        self.btn1.setObjectName(u"btn1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.btn1.setFont(font)

        self.gridLayout.addWidget(self.btn1, 0, 0, 1, 1)

        self.btn2 = QPushButton(self.centralwidget)
        self.btn2.setObjectName(u"btn2")
        sizePolicy1.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy1)
        self.btn2.setFont(font)

        self.gridLayout.addWidget(self.btn2, 0, 1, 1, 1)

        self.btn3 = QPushButton(self.centralwidget)
        self.btn3.setObjectName(u"btn3")
        sizePolicy1.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy1)
        self.btn3.setFont(font)

        self.gridLayout.addWidget(self.btn3, 0, 2, 1, 1)

        self.btn4 = QPushButton(self.centralwidget)
        self.btn4.setObjectName(u"btn4")
        sizePolicy1.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy1)
        self.btn4.setFont(font)

        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)

        self.btn5 = QPushButton(self.centralwidget)
        self.btn5.setObjectName(u"btn5")
        sizePolicy1.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy1)
        self.btn5.setFont(font)

        self.gridLayout.addWidget(self.btn5, 1, 1, 1, 1)

        self.btn6 = QPushButton(self.centralwidget)
        self.btn6.setObjectName(u"btn6")
        sizePolicy1.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy1)
        self.btn6.setFont(font)

        self.gridLayout.addWidget(self.btn6, 1, 2, 1, 1)

        self.btn7 = QPushButton(self.centralwidget)
        self.btn7.setObjectName(u"btn7")
        sizePolicy1.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy1)
        self.btn7.setFont(font)

        self.gridLayout.addWidget(self.btn7, 2, 0, 1, 1)

        self.btn8 = QPushButton(self.centralwidget)
        self.btn8.setObjectName(u"btn8")
        sizePolicy1.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy1)
        self.btn8.setFont(font)
        self.btn8.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btn8, 2, 1, 1, 1)

        self.btn9 = QPushButton(self.centralwidget)
        self.btn9.setObjectName(u"btn9")
        sizePolicy1.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy1)
        self.btn9.setFont(font)

        self.gridLayout.addWidget(self.btn9, 2, 2, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setMinimumSize(QSize(0, 90))
        self.groupBox_2.setStyleSheet(u"background-color: gray; border: none;")
        self.textbox_5 = QLineEdit(self.groupBox_2)
        self.textbox_5.setObjectName(u"textbox_5")
        self.textbox_5.setGeometry(QRect(40, 30, 61, 55))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textbox_5.sizePolicy().hasHeightForWidth())
        self.textbox_5.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.textbox_5.setFont(font1)
        self.textbox_5.setStyleSheet(u"background-color: gray; border: none;")
        self.textbox_5.setReadOnly(False)
        self.textbox_11 = QLineEdit(self.groupBox_2)
        self.textbox_11.setObjectName(u"textbox_11")
        self.textbox_11.setGeometry(QRect(30, 0, 81, 41))
        sizePolicy2.setHeightForWidth(self.textbox_11.sizePolicy().hasHeightForWidth())
        self.textbox_11.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.textbox_11.setFont(font2)
        self.textbox_11.setStyleSheet(u"background-color: gray; border: none;")
        self.textbox_11.setReadOnly(False)

        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setMinimumSize(QSize(0, 90))
        self.groupBox_3.setStyleSheet(u"background-color: gray; border: none;")
        self.textbox_6 = QLineEdit(self.groupBox_3)
        self.textbox_6.setObjectName(u"textbox_6")
        self.textbox_6.setGeometry(QRect(40, 30, 61, 55))
        sizePolicy2.setHeightForWidth(self.textbox_6.sizePolicy().hasHeightForWidth())
        self.textbox_6.setSizePolicy(sizePolicy2)
        self.textbox_6.setFont(font1)
        self.textbox_6.setStyleSheet(u"background-color: gray; border: none;")
        self.textbox_6.setReadOnly(False)
        self.textbox_12 = QLineEdit(self.groupBox_3)
        self.textbox_12.setObjectName(u"textbox_12")
        self.textbox_12.setGeometry(QRect(30, 0, 81, 41))
        sizePolicy2.setHeightForWidth(self.textbox_12.sizePolicy().hasHeightForWidth())
        self.textbox_12.setSizePolicy(sizePolicy2)
        self.textbox_12.setFont(font2)
        self.textbox_12.setStyleSheet(u"background-color: gray; border: none;")
        self.textbox_12.setReadOnly(False)

        self.gridLayout.addWidget(self.groupBox_3, 3, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.groupBox_4.setMinimumSize(QSize(0, 90))
        self.groupBox_4.setStyleSheet(u"background-color: gray; border: none;")
        self.textbox_7 = QLineEdit(self.groupBox_4)
        self.textbox_7.setObjectName(u"textbox_7")
        self.textbox_7.setGeometry(QRect(40, 30, 61, 55))
        sizePolicy2.setHeightForWidth(self.textbox_7.sizePolicy().hasHeightForWidth())
        self.textbox_7.setSizePolicy(sizePolicy2)
        self.textbox_7.setFont(font1)
        self.textbox_7.setStyleSheet(u"background-color: gray; border: none;")
        self.textbox_7.setReadOnly(False)
        self.textbox_13 = QLineEdit(self.groupBox_4)
        self.textbox_13.setObjectName(u"textbox_13")
        self.textbox_13.setGeometry(QRect(20, 0, 111, 41))
        sizePolicy2.setHeightForWidth(self.textbox_13.sizePolicy().hasHeightForWidth())
        self.textbox_13.setSizePolicy(sizePolicy2)
        self.textbox_13.setFont(font2)
        self.textbox_13.setStyleSheet(u"background-color: gray; border: none;")
        self.textbox_13.setReadOnly(False)

        self.gridLayout.addWidget(self.groupBox_4, 3, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 474, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn1.setText("")
        self.btn2.setText("")
        self.btn3.setText("")
        self.btn4.setText("")
        self.btn5.setText("")
        self.btn6.setText("")
        self.btn7.setText("")
        self.btn8.setText("")
        self.btn9.setText("")
        self.groupBox_2.setTitle("")
        self.textbox_5.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.textbox_11.setText(QCoreApplication.translate("MainWindow", u"X (YOU)", None))
        self.groupBox_3.setTitle("")
        self.textbox_6.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.textbox_12.setText(QCoreApplication.translate("MainWindow", u"TIES", None))
        self.groupBox_4.setTitle("")
        self.textbox_7.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.textbox_13.setText(QCoreApplication.translate("MainWindow", u"O (FRIENS)", None))
    # retranslateUi

