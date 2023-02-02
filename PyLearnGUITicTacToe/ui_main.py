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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(474, 310)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn2 = QPushButton(self.centralwidget)
        self.btn2.setObjectName(u"btn2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.btn2.setFont(font)

        self.gridLayout.addWidget(self.btn2, 0, 3, 1, 1)

        self.btn3 = QPushButton(self.centralwidget)
        self.btn3.setObjectName(u"btn3")
        sizePolicy1.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy1)
        self.btn3.setFont(font)

        self.gridLayout.addWidget(self.btn3, 0, 5, 1, 1)

        self.btn1 = QPushButton(self.centralwidget)
        self.btn1.setObjectName(u"btn1")
        sizePolicy1.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy1)
        self.btn1.setFont(font)

        self.gridLayout.addWidget(self.btn1, 0, 1, 1, 1)

        self.btn5 = QPushButton(self.centralwidget)
        self.btn5.setObjectName(u"btn5")
        sizePolicy1.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy1)
        self.btn5.setFont(font)

        self.gridLayout.addWidget(self.btn5, 1, 3, 1, 1)

        self.btn4 = QPushButton(self.centralwidget)
        self.btn4.setObjectName(u"btn4")
        sizePolicy1.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy1)
        self.btn4.setFont(font)

        self.gridLayout.addWidget(self.btn4, 1, 1, 1, 1)

        self.btn7 = QPushButton(self.centralwidget)
        self.btn7.setObjectName(u"btn7")
        sizePolicy1.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy1)
        self.btn7.setFont(font)

        self.gridLayout.addWidget(self.btn7, 2, 1, 1, 1)

        self.btn8 = QPushButton(self.centralwidget)
        self.btn8.setObjectName(u"btn8")
        sizePolicy1.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy1)
        self.btn8.setFont(font)

        self.gridLayout.addWidget(self.btn8, 2, 3, 1, 1)

        self.btn9 = QPushButton(self.centralwidget)
        self.btn9.setObjectName(u"btn9")
        sizePolicy1.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy1)
        self.btn9.setFont(font)

        self.gridLayout.addWidget(self.btn9, 2, 5, 1, 1)

        self.btn6 = QPushButton(self.centralwidget)
        self.btn6.setObjectName(u"btn6")
        sizePolicy1.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy1)
        self.btn6.setFont(font)

        self.gridLayout.addWidget(self.btn6, 1, 5, 1, 1)

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
        self.btn2.setText("")
        self.btn3.setText("")
        self.btn1.setText("")
        self.btn5.setText("")
        self.btn4.setText("")
        self.btn7.setText("")
        self.btn8.setText("")
        self.btn9.setText("")
        self.btn6.setText("")
    # retranslateUi

