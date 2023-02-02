import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

def check():
    if buttons[0][0].text() == 'X' and buttons[1][0].text() == 'X' and buttons[2][0].text() == 'X':
        msg_box = QMessageBox(text= 'player 1 is wined')
        msg_box.exec()

def play(row, col):
    global player
    if player == 1:
        buttons[row][col].setText('X')
        buttons[row][col].setStyleSheet('color: red; background-color: pink')
        player = 2

    elif player == 2:
        buttons[row][col].setText('O')
        buttons[row][col].setStyleSheet('color: blue; background-color: lightblue')
        player = 1
    
    check()


app = QApplication(sys.argv)

player = 1

loader = QUiLoader()
main_window = loader.load('main.ui')
main_window.show()

buttons = [[main_window.btn1, main_window.btn2, main_window.btn3],
           [main_window.btn4, main_window.btn5, main_window.btn6],
           [main_window.btn7, main_window.btn8, main_window.btn9]]

for row in range(3):
    for col in range(3):
        buttons[row][col].clicked.connect(partial(play, row, col))

app.exec()