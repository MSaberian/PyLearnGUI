import sys
from random import randint
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
import PySide6.QtWebEngineCore 

PYSIDE_DESIGNER_PLUGINS = "."

player1_points = []
player2_points = []

def set_scroreboard_color():
    if player == 1:
        main_window.gb_x.setStyleSheet('background-color: yellow')
        main_window.gb_o.setStyleSheet('background-color: gray')
    else:
        main_window.gb_o.setStyleSheet('background-color: blue')
        main_window.gb_x.setStyleSheet('background-color: gray')

def reset_page():
    global player
    player = randint(1, 2)

    for row in range(3):
        for col in range(3):
            buttons[row][col].setText('')
            buttons[row][col].setStyleSheet('')
            player1_points.clear()
            player2_points.clear()
            
    if main_window.rb_cpu.isChecked() and player == 2:
        add_cpu_point()
        player = 1
    set_scroreboard_color()

def check_game(player_points, player_name):
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
            msg_box = QMessageBox(text= f'{player_name} is wined')
            msg_box.exec()
            reset_page()
            return True
    
    return False

def get_point(player_points, player_name):
    while True:
        if player_name == "CPU player":
            row = randint(0, 2)
            col = randint(0, 2)
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

def add_cpu_point():
    while True:
        row = randint(0, 2)
        col = randint(0, 2)
        if not [row,col] in player1_points and not [row,col] in player2_points:
            buttons[row][col].setText('O')
            buttons[row][col].setStyleSheet('color: blue')
            player2_points.append([row,col])
            if check_game(player2_points, 'CPU'):
                main_window.tb_o.setText(str(int(main_window.tb_o.text())+1))
            break

def check_draw():
    if len(player1_points) + len(player2_points) == 9:
        msg_box = QMessageBox(text= 'ِDraw!!')
        main_window.tb_t.setText(str(int(main_window.tb_t.text())+1))
        msg_box.exec()
        reset_page()
        return True

def play(row, col):
    global player
    if not [row,col] in player1_points and not [row,col] in player2_points:
        if player == 1:
            buttons[row][col].setText('X')
            buttons[row][col].setStyleSheet('color: yellow')
            player1_points.append([row,col])
            if check_game(player1_points, 'player 1'):
                main_window.tb_x.setText(str(int(main_window.tb_x.text())+1))
                return
            if main_window.rb_cpu.isChecked():
                if not check_draw():
                    add_cpu_point()
            else:
                player = 2

        elif player == 2:
            buttons[row][col].setText('O')
            buttons[row][col].setStyleSheet('color: blue')
            player2_points.append([row,col])
            player = 1
            if check_game(player2_points, 'player 2'):
                main_window.tb_o.setText(str(int(main_window.tb_o.text())+1))
    else:
        print('fault')
    set_scroreboard_color()
    check_draw()
        
def reset_game():
    main_window.tb_t.setText('0')
    main_window.tb_x.setText('0')
    main_window.tb_o.setText('0')
    if main_window.rb_cpu.isChecked():
        main_window.tb_another.setText('O (CPU)')
    else:
        main_window.tb_another.setText('O (RIVAL)')
    reset_page()

app = QApplication(sys.argv)

loader = QUiLoader()
main_window = loader.load('main.ui')
main_window.show()

loader_about = QUiLoader()
about_window = loader_about.load('about.ui')

def about():
    about_window.show()

def about_close():
    about_window.close()

buttons = [[main_window.btn1, main_window.btn2, main_window.btn3],
           [main_window.btn4, main_window.btn5, main_window.btn6],
           [main_window.btn7, main_window.btn8, main_window.btn9]]

for row in range(3):
    for col in range(3):
        buttons[row][col].clicked.connect(partial(play, row, col))
main_window.btn_newgame.clicked.connect(reset_page)
main_window.rb_cpu.toggled.connect(reset_game)
main_window.rb_player.toggled.connect(reset_game)
main_window.btn_about.clicked.connect(about)
about_window.btn_ok.clicked.connect(about_close)

reset_page()

app.exec()