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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionnew.triggered.connect(self.new_game)
        self.ui.actionOpen_File.triggered.connect(self.open_file)
        # self.ui.actiongreen.triggered.connect(partial(self.setColor,'green','pink'))
        # self.ui.actionpink.triggered.connect(partial(self.setColor,'pink','green'))
        self.ui.actionlight.triggered.connect(partial(self.setColor,'light','black'))
        self.ui.actiondark.triggered.connect(partial(self.setColor,'black'))
        self.line_edits = [[None for i in range(9)]for j in range(9)]
        self.editableCells = []
        self.picking_boxes()
        self.new_game()
        self.them = 'light'
        self.checkable = True
        qdarktheme.setup_theme("light")

    def setColor(self, color, textColor = 'black'):
        self.them = color
        if color == 'black':
            qdarktheme.setup_theme("dark")
        else:
            qdarktheme.setup_theme("light")
            # self.setStyleSheet(f'background-color: {color}')
            # for i in range(9):
            #     for j in range(9):
            #         self.line_edits[i][j].setStyleSheet(f'color: {textColor}')
        self.check()
    
    def resetColor(self):
        self.setStyleSheet('')
        for i in range(9):
            for j in range(9):
                self.line_edits[i][j].setStyleSheet('')

    def open_file(self):
        try:
            file_path = QFileDialog.getOpenFileName(self, 'Open file...')[0]
            # print(file_path)
            self.editableCells.clear()
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
                        self.editableCells.append([i,j])
                        self.line_edits[i][j].setText(str(puzzle_board[i][j]))
                        self.line_edits[i][j].setReadOnly(True)
                    else:
                        self.line_edits[i][j].setText('')
                        self.line_edits[i][j].setReadOnly(False)
            self.checkable = True
        except:
            print("An exception occurred to load the file")

    def setCellFalse(self,row,col):
        if [row,col] in self.editableCells:
            self.line_edits[row][col].setStyleSheet('background-color: pink')
        else:
            self.line_edits[row][col].setStyleSheet('background-color: red')

    def check(self,i=-1,j=-1):
        output = True
        self.resetColor()
        for row in range(9):
            for col in range(9):
                number1 = self.line_edits[row][col].text()
                if number1 == '':
                    output = False
                for row9 in range(row+1,9):
                    number2 = self.line_edits[row9][col].text()
                    if number1 == number2 and number2 != '':
                        self.setCellFalse(row,col)
                        self.setCellFalse(row9,col)
                        # print(f'❌ row: {row}, col: {col}, row9: {row9}, number1: {number1}, number2: {number2}')
                        output = False

                for col9 in range(col+1,9):
                    number2 = self.line_edits[row][col9].text()
                    if number1 == number2 and number2 != '':
                        self.setCellFalse(row,col)
                        self.setCellFalse(row,col9)
                        # print(f'❌ row: {row}, col: {col}, row9: {row9}, number1: {number1}, number2: {number2}')
                        output = False

        for n in range(0, 9, 3):
            for m in range(0, 9, 3):
                for row in range(n, n + 3):
                    for col in range(m, m + 3):
                        number1 = self.line_edits[row][col].text()
                        for row3 in range(n, n + 3):
                            for col3 in range(m, m +3):
                                number2 = self.line_edits[row3][col3].text()
                                if number1 == number2 and number2 != '' and not (row == row3 and col == col3):
                                    self.setCellFalse(row,col)
                                    self.setCellFalse(row3,col3)
                                    # print(f'❌ row: {row}, col: {col}, row3: {row3}, col3: {col3},number1: {number1}, number2: {number2}')
                                    output = False
        print(output)
        return output

    def validation(self, i, j, text):
        if self.checkable:
            if text not in ['1','2','3','4','5','6','7','8','9']:
                self.line_edits[i][j].setText('')
            if self.check(i,j):
                msg_box = QMessageBox()
                msg_box.setText('YOU ARE WINNNN 🎊🎊🎉')
                msg_box.exec()

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
        self.editableCells.clear()
        puzzle = Sudoku(3, seed= random.randint(1, 1000)).difficulty(0.5)
        for i in range(9):
            for j in range(9):
                if puzzle.board[i][j] is not None:
                    self.editableCells.append([i,j])
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