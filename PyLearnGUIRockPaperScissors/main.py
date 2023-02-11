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
        self.ui.btn3_unvisivable.setVisible(False)
        self.ui.btn4_unvisivable.setVisible(False)
        self.CScore = 0
        self.UScore = 0
        self.TScore = 0
        
        self.ui.btn_paper.clicked.connect(self.paper)
        self.ui.btn_scissors.clicked.connect(self.scissors)
        self.ui.btn_rock.clicked.connect(self.rock)
        
    def paper(self):
        self.ui.btn_you.setIcon(QIcon('paper2.png'))
        self.computerChoice(0)
        
    def scissors(self):
        self.ui.btn_you.setIcon(QIcon('scissors2.png'))
        self.computerChoice(1)
        
    def rock(self):
        self.ui.btn_you.setIcon(QIcon('rock2.png'))
        self.computerChoice(2)

    def computerChoice(self,user_choice):
        i = random.randint(0,2)
        if i == 0:
            self.ui.btn_computer.setIcon(QIcon('paper2.png'))
        elif i == 1:
            self.ui.btn_computer.setIcon(QIcon('scissors2.png'))
        else:
            self.ui.btn_computer.setIcon(QIcon('rock2.png'))
        
        indwin = user_choice - i
        if indwin < 0:
            indwin += 3
        if indwin == 0:
            self.TScore += 1
            self.ui.how_win.setText('              No one won')
        elif indwin == 1:
            self.UScore += 1
            self.ui.how_win.setText('               You won')
        else:
            self.CScore += 1
            self.ui.how_win.setText('            Computer won')
        
        self.ui.scoreboard.setText(f'     You: {self.UScore}       Ties: {self.TScore}          Computer: {self.CScore}')


    def play(self, i ,j):
        if abs(i-self.empty_i) + abs(j-self.empty_j) == 1:

            self.buttons[self.empty_i][self.empty_j].setText(self.buttons[i][j].text())
            self.buttons[i][j].setText('16')

            self.buttons[self.empty_i][self.empty_j].setVisible(True)
            self.buttons[i][j].setVisible(False)

            self.empty_i = i
            self.empty_j = j

            if self.check_win():
                msg_box = QMessageBox()
                msg_box.setText('YOU ARE WINNNN 🎊🎊🎉')
                msg_box.exec()

    def check_win(self):
        index = 1
        for i in range(4):
            for j in range(4):
                if int(self.buttons[i][j].text()) != index:
                    return False
                index += 1
        return True

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()

app.exec()