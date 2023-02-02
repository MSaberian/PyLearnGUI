
from functools import partial
import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def sum():
    global a
    global state
    state = 'sum'
    a = float(main_window.textbox.text())
    main_window.textbox.setText('')
    
def operation(op):
    global a
    global state
    state = op
    a = float(main_window.textbox.text())
    main_window.textbox.setText('')

def sub():
    global a
    global state
    state = 'sub'
    a = float(main_window.textbox.text())
    main_window.textbox.setText('')
    
def mul():
    global a
    global state
    state = 'mul'
    a = float(main_window.textbox.text())
    main_window.textbox.setText('')
    
def dev():
    global a
    global state
    state = 'dev'
    a = float(main_window.textbox.text())
    main_window.textbox.setText('')
    
def AC():
    main_window.textbox.setText('')
    
def per():
    main_window.textbox.setText(str(float(main_window.textbox.text())/100))
    
def PN():
    main_window.textbox.setText(str(float(main_window.textbox.text())*(-1)))

def sin():
    main_window.textbox.setText(str(math.sin(float(main_window.textbox.text()))))
    
def cos():
    main_window.textbox.setText(str(math.cos(float(main_window.textbox.text()))))
    
def tan():
    main_window.textbox.setText(str(math.tan(float(main_window.textbox.text()))))
    
def cot():
    main_window.textbox.setText(str(1/math.tan(float(main_window.textbox.text()))))
    
def log():
    main_window.textbox.setText(str(math.log(float(main_window.textbox.text()))))
    
def sqrt():
    main_window.textbox.setText(str(math.sqrt(float(main_window.textbox.text()))))
        
def n(x):
    main_window.textbox.setText(main_window.textbox.text()+x)
    
def dot():
    main_window.textbox.setText(main_window.textbox.text()+'.')

def result():
    global b
    b = float(main_window.textbox.text())
    if state in globals():
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


my_app = QApplication([])

loader = QUiLoader()
main_window = loader.load('main.ui')
main_window.show()

main_window.sum.clicked.connect(partial(operation,'sum'))
main_window.sub.clicked.connect(partial(operation,'sub'))
main_window.mul.clicked.connect(partial(operation,'mul'))
main_window.dev.clicked.connect(partial(operation,'dev'))
main_window.AC.clicked.connect(AC)
main_window.percent.clicked.connect(per)
main_window.PN.clicked.connect(PN)
main_window.sin.clicked.connect(sin)
main_window.cos.clicked.connect(cos)
main_window.tan.clicked.connect(tan)
main_window.cot.clicked.connect(cot)
main_window.log.clicked.connect(log)
main_window.sqrt.clicked.connect(sqrt)
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