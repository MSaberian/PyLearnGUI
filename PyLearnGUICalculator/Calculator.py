from functools import partial
import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def operation_2part(op):
    global a
    global state
    state = op
    a = float(main_window.textbox.text())
    main_window.textbox.setText('')

def operation(op):
    number = float(main_window.textbox.text())
    if op == 'AC':
        number = 0
    elif op == 'per':
        number = number/100
    elif op == 'PN':
        number = -1*number
    elif op == 'sin':
        number = math.sin(number)
    elif op == 'cos':
        number = math.cos(number)
    elif op == 'tan':
        number = math.tan(number)
    elif op == 'cot':
        number = 1/math.tan(number)
    elif op == 'log':
        number = math.log(number)
    elif op == 'sqrt':
        number = math.sqrt(number)

    main_window.textbox.setText(str(number))
        
def n(x):
    global equal_pressed
    if equal_pressed:
        equal_pressed = False
        main_window.textbox.setText('')
    if main_window.textbox.text() == '0':
        main_window.textbox.setText('')
    main_window.textbox.setText(main_window.textbox.text()+x)
    
def dot():
    global equal_pressed
    if equal_pressed:
        equal_pressed = False
        main_window.textbox.setText('')
    main_window.textbox.setText(main_window.textbox.text()+'.')

def result():
    global b
    global equal_pressed
    equal_pressed = True
    b = float(main_window.textbox.text())
    if state == 'sum':
        c = a + b
    elif state == 'sub':
        c = a - b
    elif state == 'mul':
        c = a * b
    elif state == 'dev':
        c = a / b
    else:
        c = 0
    
    main_window.textbox.setText(str(c))


equal_pressed = False

my_app = QApplication([])

loader = QUiLoader()
main_window = loader.load('main.ui')
main_window.show()

main_window.sum.clicked.connect(partial(operation_2part,'sum'))
main_window.sub.clicked.connect(partial(operation_2part,'sub'))
main_window.mul.clicked.connect(partial(operation_2part,'mul'))
main_window.dev.clicked.connect(partial(operation_2part,'dev'))
main_window.AC.clicked.connect(partial(operation,'AC'))
main_window.percent.clicked.connect(partial(operation,'per'))
main_window.PN.clicked.connect(partial(operation,'PN'))
main_window.sin.clicked.connect(partial(operation,'sin'))
main_window.cos.clicked.connect(partial(operation,'cos'))
main_window.tan.clicked.connect(partial(operation,'tan'))
main_window.cot.clicked.connect(partial(operation,'cot'))
main_window.log.clicked.connect(partial(operation,'log'))
main_window.sqrt.clicked.connect(partial(operation,'sqrt'))
main_window.n1.clicked.connect(partial(n,'1'))
main_window.n2.clicked.connect(partial(n,'2'))
main_window.n3.clicked.connect(partial(n,'3'))
main_window.n4.clicked.connect(partial(n,'4'))
main_window.n5.clicked.connect(partial(n,'5'))
main_window.n6.clicked.connect(partial(n,'6'))
main_window.n7.clicked.connect(partial(n,'7'))
main_window.n8.clicked.connect(partial(n,'8'))
main_window.n9.clicked.connect(partial(n,'9'))
main_window.n0.clicked.connect(partial(n,'0'))
main_window.dot.clicked.connect(dot)
main_window.equal.clicked.connect(result)

my_app.exec()