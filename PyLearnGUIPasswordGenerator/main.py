import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.number = ['0','1','2','3','4','5','6','7','8','9']
        self.alphabet = ['a','b','c','d','e','f','g','h','a','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.ALPHABET = ['A','B','C','D','E','F','G','H','I','G','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.special = [' ','!','"','#','$','%','&','\'',')','(','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','{','}','|','~']
    #     self.buttons = [[self.ui.btn_generate, self.ui.btn2, self.ui.btn3, self.ui.btn4],
    #                     [self.ui.btn5, self.ui.btn6, self.ui.btn7, self.ui.btn8],
    #                     [self.ui.btn9, self.ui.btn10, self.ui.btn11, self.ui.btn12],
    #                     [self.ui.btn13, self.ui.btn14, self.ui.btn15, self.ui.btn16]]
    #     for i in range(4):
    #         for j in range(4):
    #             self.buttons[i][j].setText(str(r[4*i+j]))
    #             self.buttons[i][j].clicked.connect(partial(self.play, i, j))
    #             if r[4*i+j] == 16:
    #                 self.buttons[i][j].setVisible(False)
    #                 self.empty_i = i
    #                 self.empty_j = j
        self.ui.btn_generate.clicked.connect(self.generate)

    def generate(self):
        if self.ui.rbn_1.isChecked():
            passworld = random.choices(self.number, k=1) + random.choices(self.alphabet, k=5) + random.choices(self.ALPHABET, k=1) + random.choices(self.special, k=1)
        elif self.ui.rbn_2.isChecked():
            passworld = random.choices(self.number, k=2) + random.choices(self.alphabet, k=6) + random.choices(self.ALPHABET, k=2) + random.choices(self.special, k=2)
        else:
            passworld = random.choices(self.number, k=3) + random.choices(self.alphabet, k=12) + random.choices(self.ALPHABET, k=3) + random.choices(self.special, k=2)
        
        random.shuffle(passworld)
        self.ui.linePassword.setText(''.join(passworld))



    #     if abs(i-self.empty_i) + abs(j-self.empty_j) == 1:

    #         self.buttons[self.empty_i][self.empty_j].setText(self.buttons[i][j].text())
    #         self.buttons[i][j].setText('16')

    #         self.buttons[self.empty_i][self.empty_j].setVisible(True)
    #         self.buttons[i][j].setVisible(False)

    #         self.empty_i = i
    #         self.empty_j = j

    #         if self.check_win():
    #             msg_box = QMessageBox()
    #             msg_box.setText('YOU ARE WINNNN 🎊🎊🎉')
    #             msg_box.exec()

    # def check_win(self):
    #     index = 1
    #     for i in range(4):
    #         for j in range(4):
    #             if int(self.buttons[i][j].text()) != index:
    #                 return False
    #             index += 1
    #     return True

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()

app.exec()