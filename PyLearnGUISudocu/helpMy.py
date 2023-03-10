# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'helpMy.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 449)
        MainWindow.setMinimumSize(QSize(500, 449))
        MainWindow.setMaximumSize(QSize(500, 449))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u"Help.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: white; border: none;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 10, 441, 401))
        font = QFont()
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"background-color: transparent; border: none;")
        self.textEdit.setReadOnly(True)
        self.btn_ok = QPushButton(self.centralwidget)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(400, 370, 71, 31))
        self.btn_ok.setFont(font)
        self.btn_ok.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ok.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(170, 170, 170, 255))\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 363, 91, 20))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setOpenExternalLinks(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Help </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'sans-serif'; font-siz"
                        "e:14px; font-weight:700; color:#202122;\">Sudoku</span><span style=\" font-family:'sans-serif'; font-size:14px; color:#202122;\">\u00a0is a\u00a0</span><a href=\"https://en.wikipedia.org/wiki/Logic\"><span style=\" font-family:'sans-serif'; font-size:14px; text-decoration: underline; color:#000000;\">logic</span></a><span style=\" font-family:'sans-serif'; font-size:14px; color:#202122;\">-based\u00a0</span><a href=\"https://en.wikipedia.org/wiki/Combinatorics\"><span style=\" font-family:'sans-serif'; font-size:14px; text-decoration: underline; color:#000000;\">combinatorial</span></a><span style=\" font-family:'sans-serif'; font-size:14px; color:#202122;\">\u00a0number-placement\u00a0</span><a href=\"https://en.wikipedia.org/wiki/Puzzle\"><span style=\" font-family:'sans-serif'; font-size:14px; text-decoration: underline; color:#000000;\">puzzle</span></a><span style=\" font-family:'sans-serif'; font-size:14px; color:#202122;\">. In classic Sudoku, the objective is to fill a 9\u00a0\u00d7\u00a09 grid with di"
                        "gits so that each column, each row, and each of the nine 3\u00a0\u00d7\u00a03 subgrids that compose the grid (also called &quot;boxes&quot;, &quot;blocks&quot;, or &quot;regions&quot;) contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.</span></p>\n"
"<p style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:'sans-serif'; font-size:14px; color:#202122; background-color:#ffffff;\">French newspapers featured variations of the Sudoku puzzles in the 19th century, and the puzzle has appeared since 1979 in</span><span style=\" font-family:'sans-serif'; font-size:14px; color:#202122;\">\u00a0</span><a href=\"https://en.wikipedia.org/wiki/Puzzle_book\"><span style=\" font-family:'sans-serif'; font-size:14px; text-decoration: underline; color:#000000;\">puzzle</span></a><a href=\"https://en.wikipedia.org/wiki/Pu"
                        "zzle_book\"><span style=\" font-family:'sans-serif'; font-size:14px; text-decoration: underline; color:#3366cc;\"> </span></a><a href=\"https://en.wikipedia.org/wiki/Puzzle_book\"><span style=\" font-family:'sans-serif'; font-size:14px; text-decoration: underline; color:#000000;\">books</span></a><span style=\" font-family:'sans-serif'; font-size:14px; color:#202122;\">\u00a0under the name Number Place.\u00a0However, the modern Sudoku only began to gain widespread popularity in 1986 when it was published by the Japanese puzzle company\u00a0</span><a href=\"https://en.wikipedia.org/wiki/Nikoli_(publisher)\"><span style=\" font-family:'sans-serif'; font-size:14px; text-decoration: underline; color:#000000;\">Nikoli</span></a><span style=\" font-family:'sans-serif'; font-size:14px; color:#202122;\">\u00a0under the name Sudoku, meaning &quot;single number&quot;.\u00a0It first appeared in a U.S. newspaper, and then\u00a0</span><a href=\"https://en.wikipedia.org/wiki/The_Times\"><span style=\" font-family:'sans-seri"
                        "f'; font-size:14px; text-decoration: underline; color:#000000;\">The</span></a><a href=\"https://en.wikipedia.org/wiki/The_Times\"><span style=\" font-family:'sans-serif'; font-size:14px; text-decoration: underline; color:#3366cc;\"> </span></a><a href=\"https://en.wikipedia.org/wiki/The_Times\"><span style=\" font-family:'sans-serif'; font-size:14px; text-decoration: underline; color:#000000;\">Times</span></a><span style=\" font-family:'sans-serif'; font-size:14px; color:#202122;\">\u00a0(London), in 2004, thanks to the efforts of\u00a0</span><a href=\"https://en.wikipedia.org/wiki/Wayne_Gould\"><span style=\" font-family:'sans-serif'; font-size:14px; text-decoration: underline; color:#000000;\">Wayne</span></a><a href=\"https://en.wikipedia.org/wiki/Wayne_Gould\"><span style=\" font-family:'sans-serif'; font-size:14px; text-decoration: underline; color:#3366cc;\"> </span></a><a href=\"https://en.wikipedia.org/wiki/Wayne_Gould\"><span style=\" font-family:'sans-serif'; font-size:14px; text-decoration: underl"
                        "ine; color:#000000;\">Gould</span></a><span style=\" font-family:'sans-serif'; font-size:14px; color:#202122;\">, who devised a\u00a0</span><a href=\"https://en.wikipedia.org/wiki/Computer_program\"><span style=\" font-family:'sans-serif'; font-size:14px; text-decoration: underline; color:#000000;\">computer</span></a><a href=\"https://en.wikipedia.org/wiki/Computer_program\"><span style=\" font-family:'sans-serif'; font-size:14px; text-decoration: underline; color:#3366cc;\"> </span></a><a href=\"https://en.wikipedia.org/wiki/Computer_program\"><span style=\" font-family:'sans-serif'; font-size:14px; text-decoration: underline; color:#000000;\">program</span></a><span style=\" font-family:'sans-serif'; font-size:14px; color:#202122;\">\u00a0to rapidly produce unique puzzles.</span><span style=\" font-size:12pt;\">     </span></p>\n"
"<p style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-size:12pt;\""
                        ">For more information go to             </span></p></body></html>", None))
        self.btn_ok.setText(QCoreApplication.translate("MainWindow", u"ok", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://en.wikipedia.org/wiki/Sudoku\"><span style=\" text-decoration: underline; color:#0000ff;\">wikipedia.</span></a></p></body></html>", None))
    # retranslateUi

