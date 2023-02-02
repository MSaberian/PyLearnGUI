import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

player1_points = []
player2_points = []
CPU_number = -1

def reset_page():
    for row in range(3):
        for col in range(3):
            buttons[row][col].setText('')
            buttons[row][col].setStyleSheet('')
            player1_points.clear()
            player2_points.clear()


def check_game(player_points, player):
    sum2 = 0
    sum3 = 0
    for i in range(3):
        sum0 = 0
        sum1 = 0
        for j in range(3):
            if [i,j] in player_points:
                sum0 += 1
            if [j,i] in player_points:
                sum1 += 1

        if [i,i] in player_points:
            sum2 += 1
        if [i,2-i] in player_points:
            sum3 += 1
        
        if sum0 == 3 or sum1 == 3 or sum2 == 3 or sum3 == 3:
            msg_box = QMessageBox(text= f'Player {player} is wined')
            msg_box.exec()
            reset_page()
            return True
    
    return False

def get_point(player_points, player_name):
    while True:
        if player_name == "CPU player":
            row = random.randint(0, 2)
            col = random.randint(0, 2)
        else:
            row = int(input("row: "))
            col = int(input("col: "))

        if 0 <= row <= 2 and 0 <= col <= 2:
            if not [row,col] in player1_points and not [row,col] in player2_points:
                player_points.append([row,col])
                break
            elif player_name != "CPU player":
                print("⚠ Don't enter repation point")
        else:
            print("⚠ you have to enter numbers between 0-2")

def play(row, col):
    global player


    if not [row,col] in player1_points and not [row,col] in player2_points:
        if player == 1:
            buttons[row][col].setText('X')
            buttons[row][col].setStyleSheet('color: red; background-color: pink')
            player1_points.append([row,col])
            player = 2
            check_game(player1_points, 'player 1')

        elif player == 2:
            buttons[row][col].setText('O')
            buttons[row][col].setStyleSheet('color: blue; background-color: lightblue')
            player2_points.append([row,col])
            player = 1
            check_game(player2_points, 'player 2')
    else:
        print('fault')


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