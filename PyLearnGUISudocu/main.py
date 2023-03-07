import sys
import random 
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6 import QtCore
from PySide6.QtGui import *
from main_window import Ui_MainWindow 
from sudoku import Sudoku
import qdarktheme

# customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
# sys.argv += ['-platform', 'windows:darkmode=2']

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionnew.triggered.connect(self.new_game)
        self.ui.actionOpen_File.triggered.connect(self.open_file)
        self.ui.actiongreen.triggered.connect(partial(self.setColor,'green','pink'))
        self.ui.actionpink.triggered.connect(partial(self.setColor,'pink','green'))
        self.ui.actionlight.triggered.connect(partial(self.setColor,'light','black'))
        self.ui.actiondark.triggered.connect(partial(self.setColor,'black'))
        self.line_edits = [[None for i in range(9)]for j in range(9)]
        self.picking_boxes()
        self.new_game()
        self.checkable = True
        qdarktheme.setup_theme("light")

    def setColor(self, color, textColor = 'black'):
        if color == 'black':
            qdarktheme.setup_theme("dark")
        else:
            qdarktheme.setup_theme("light")
            self.setStyleSheet(f'background-color: {color}')
            for i in range(9):
                for j in range(9):
                    self.line_edits[i][j].setStyleSheet(f'color: {textColor}')

    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open file...')[0]
        # print(file_path)
        f = open(file_path, 'r')
        big_text = f.read()
        rows = big_text.split('\n')
        puzzle_board = [[None for i in range(9)] for j in range(9)]
        for i in range(len(rows)):
            cells = rows[i].split(' ')
            for j in range(len(cells)):
                puzzle_board[i][j] = int(cells[j])

        self.checkable = False
        for i in range(9):
            for j in range(9):
                if puzzle_board[i][j] != 0:
                    self.line_edits[i][j].setText(str(puzzle_board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                else:
                    self.line_edits[i][j].setText('')
                    self.line_edits[i][j].setReadOnly(False)
        self.checkable = True

    def check(self):
        for i in range(0, 9):
            for j in range(0, 9):
                number1 = self.line_edits[i][0].text()
                number2 = self.line_edits[i][j].text()
                if number1 == number2:
                    print('❌')
                    return False

    def validation(self, i, j, text):
        if self.checkable:
            if text not in ['1','2','3','4','5','6','7','8','9']:
                self.line_edits[i][j].setText('')
            if self.check():
                msg_box = ...

    def picking_boxes(self, color = 'black'):
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                new_cell.setAlignment(QtCore.Qt.AlignCenter)
                new_cell.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
                new_cell.setMinimumWidth(30)
                new_cell.setFont(QFont('Centaur', pointSize=15))
                new_cell.setStyleSheet(f'color: {color}')
                self.ui.gr_ds.addWidget(new_cell, i, j)
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell

    def new_game(self):
        self.checkable = False
        puzzle = Sudoku(3, seed= random.randint(1, 1000)).difficulty(0.5)
        for i in range(9):
            for j in range(9):
                if puzzle.board[i][j] is not None:
                    self.line_edits[i][j].setText(str(puzzle.board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                else:
                    self.line_edits[i][j].setText('')
                    self.line_edits[i][j].setReadOnly(False)
        self.checkable = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()