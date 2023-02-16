import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import *
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn1_unvisivable.setVisible(False)
        self.ui.btn2_unvisivable.setVisible(False)
        self.C1Score = 0
        self.C2Score = 0
        self.UScore = 0
        self.TScore = 0
        
        self.ui.btn_onhand.clicked.connect(self.onhand)
        self.ui.btn_backhand.clicked.connect(self.backhand)
        
    def onhand(self):
        self.ui.btn_you.setIcon(QIcon('ohhand.png'))
        self.computerChoice(0)
        
    def backhand(self):
        self.ui.btn_you.setIcon(QIcon('backhand.png'))
        self.computerChoice(1)
        

    def computerChoice(self,user_choice):
        i = random.randint(0,1)
        if i == 0:
            self.ui.btn_computer1.setIcon(QIcon('ohhand.png'))
        else:
            self.ui.btn_computer1.setIcon(QIcon('backhand.png'))

            
        j = random.randint(0,1)
        if j == 0:
            self.ui.btn_computer2.setIcon(QIcon('ohhand.png'))
        else:
            self.ui.btn_computer2.setIcon(QIcon('backhand.png'))
        

        indwin = (user_choice + i + j)%3
        if indwin == 0:
            self.ui.how_win.setText('       No one won')
            self.TScore += 1
        elif user_choice - i - j == 1 or user_choice - i - j == -2:
            self.UScore += 1
            self.ui.how_win.setText('   You won')
        elif user_choice == j:
            self.C1Score += 1
            self.ui.how_win.setText('    Computer1 won')
        else:
            self.C2Score += 1
            self.ui.how_win.setText('    Computer2 won')
        
        self.ui.scoreboard.setText(f'  You: {self.UScore}    Computer1: {self.C1Score}')
        self.ui.scoreboard_2.setText(f' Ties: {self.TScore}     Computer2: {self.C2Score}')

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()

app.exec()