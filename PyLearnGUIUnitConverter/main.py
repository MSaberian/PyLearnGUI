import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.combo_initialize()

        self.ui.lineEdit_1.textChanged.connect(self.convert)
        self.ui.cmb_par.currentTextChanged.connect(self.combo_initialize)
        self.ui.cmb_unit_1.currentTextChanged.connect(self.convert)
        self.ui.cmb_unit_2.currentTextChanged.connect(self.convert)

    def combo_initialize(self):
        if len(self.ui.cmb_par.currentText()) == 0:
            self.ui.cmb_par.addItem('mass')
            self.ui.cmb_par.addItem('length')
            self.ui.cmb_par.addItem('temperature')
            self.ui.cmb_par.addItem('digital volume')
        
        if self.ui.cmb_par.currentText() == 'mass':
            self.ui.cmb_unit_1.clear()
            self.ui.cmb_unit_1.addItem('gram')
            self.ui.cmb_unit_1.addItem('kilograms')
            self.ui.cmb_unit_1.addItem('ton')
            self.ui.cmb_unit_1.addItem('pound')
            self.ui.cmb_unit_2.clear()
            self.ui.cmb_unit_2.addItem('gram')
            self.ui.cmb_unit_2.addItem('kilograms')
            self.ui.cmb_unit_2.addItem('ton')
            self.ui.cmb_unit_2.addItem('pound')
            self.ui.cmb_unit_2.setCurrentIndex(1)
            
        elif self.ui.cmb_par.currentText() == 'length':
            self.ui.cmb_unit_1.clear()
            self.ui.cmb_unit_1.addItem('millimeter')
            self.ui.cmb_unit_1.addItem('centimeter')
            self.ui.cmb_unit_1.addItem('meter')
            self.ui.cmb_unit_1.addItem('kilometer')
            self.ui.cmb_unit_1.addItem('inch')
            self.ui.cmb_unit_2.clear()
            self.ui.cmb_unit_2.addItem('millimeter')
            self.ui.cmb_unit_2.addItem('centimeter')
            self.ui.cmb_unit_2.addItem('meter')
            self.ui.cmb_unit_2.addItem('kilometer')
            self.ui.cmb_unit_2.addItem('inch')
            self.ui.cmb_unit_2.setCurrentIndex(1)

        elif self.ui.cmb_par.currentText() == 'temperature':
            self.ui.cmb_unit_1.clear()
            self.ui.cmb_unit_1.addItem('centigrade')
            self.ui.cmb_unit_1.addItem('fahrenheit')
            self.ui.cmb_unit_1.addItem('kelvin')
            self.ui.cmb_unit_2.clear()
            self.ui.cmb_unit_2.addItem('centigrade')
            self.ui.cmb_unit_2.addItem('fahrenheit')
            self.ui.cmb_unit_2.addItem('kelvin')
            self.ui.cmb_unit_2.setCurrentIndex(1)
            
        elif self.ui.cmb_par.currentText() == 'digital volume':
            self.ui.cmb_unit_1.clear()
            self.ui.cmb_unit_1.addItem('bit')
            self.ui.cmb_unit_1.addItem('byte')
            self.ui.cmb_unit_1.addItem('kilobyte')
            self.ui.cmb_unit_1.addItem('megabyte')
            self.ui.cmb_unit_1.addItem('gigabyte')
            self.ui.cmb_unit_1.addItem('terabyte')
            self.ui.cmb_unit_2.clear()
            self.ui.cmb_unit_2.addItem('bit')
            self.ui.cmb_unit_2.addItem('byte')
            self.ui.cmb_unit_2.addItem('kilobyte')
            self.ui.cmb_unit_2.addItem('megabyte')
            self.ui.cmb_unit_2.addItem('gigabyte')
            self.ui.cmb_unit_2.addItem('terabyte')
            self.ui.cmb_unit_2.setCurrentIndex(1)

    def convert(self, text):
        text = self.ui.lineEdit_1.text()
        if self.ui.cmb_par.currentText() == 'temperature':
            if text == '':
                text = '0'
            elif not ((text[-1] == '.' or text[-1] == '-' or text[-1].isnumeric()) and text.count('.') < 2):
                text = text[:-1]
                if text == '':
                    text = '0'
            if len(text) > 1:
                if text[0] == '0' and text[1] != '.':
                    text = text[1:]
                if text[1:].count('-'):
                    text = text[:-1]
            self.ui.lineEdit_1.setText(text)
        
        else:
            if text == '':
                text = '0'
            elif not ((text[-1] == '.' or text[-1].isnumeric()) and text.count('.') < 2):
                text = text[:-1]
                if text == '':
                    text = '0'
            if len(text) > 1:
                if text[0] == '0' and text[1] != '.':
                    text = text[1:]
                elif text[0] == '-':
                    text = text[1:]
            if text[0] == '-':
                text = '0'
            self.ui.lineEdit_1.setText(text)

        try:
            if self.ui.cmb_par.currentText() == 'mass':
                if self.ui.cmb_unit_1.currentText() == 'gram':
                    if self.ui.cmb_unit_2.currentText() == 'gram':
                        self.ui.lineEdit_2.setText(text)
                    elif self.ui.cmb_unit_2.currentText() == 'kilograms':
                        self.ui.lineEdit_2.setText(str(float(text)/1000))
                    elif self.ui.cmb_unit_2.currentText() == 'ton':
                        self.ui.lineEdit_2.setText(str(float(text)/1000000))
                    elif self.ui.cmb_unit_2.currentText() == 'pound':
                        self.ui.lineEdit_2.setText(str(float(text)/453.6))
            
                elif self.ui.cmb_unit_1.currentText() == 'kilograms':
                    if self.ui.cmb_unit_2.currentText() == 'gram':
                        self.ui.lineEdit_2.setText(str(float(text)*1000))
                    elif self.ui.cmb_unit_2.currentText() == 'kilograms':
                        self.ui.lineEdit_2.setText(text)
                    elif self.ui.cmb_unit_2.currentText() == 'ton':
                        self.ui.lineEdit_2.setText(str(float(text)/1000))
                    elif self.ui.cmb_unit_2.currentText() == 'pound':
                        self.ui.lineEdit_2.setText(str(float(text)/.4536))
                        
                elif self.ui.cmb_unit_1.currentText() == 'ton':
                    if self.ui.cmb_unit_2.currentText() == 'gram':
                        self.ui.lineEdit_2.setText(str(float(text)*1000000))
                    elif self.ui.cmb_unit_2.currentText() == 'kilograms':
                        self.ui.lineEdit_2.setText(str(float(text)/1000))
                    elif self.ui.cmb_unit_2.currentText() == 'ton':
                        self.ui.lineEdit_2.setText(text)
                    elif self.ui.cmb_unit_2.currentText() == 'pound':
                        self.ui.lineEdit_2.setText(str(float(text)/.0004536))

                elif self.ui.cmb_unit_1.currentText() == 'pound':
                    if self.ui.cmb_unit_2.currentText() == 'gram':
                        self.ui.lineEdit_2.setText(str(float(text)*453.6))
                    elif self.ui.cmb_unit_2.currentText() == 'kilograms':
                        self.ui.lineEdit_2.setText(str(float(text)*.4536))
                    elif self.ui.cmb_unit_2.currentText() == 'ton':
                        self.ui.lineEdit_2.setText(str(float(text)*.0004536))
                    elif self.ui.cmb_unit_2.currentText() == 'pound':
                        self.ui.lineEdit_2.setText(text)
                
            if self.ui.cmb_par.currentText() == 'length':
                if self.ui.cmb_unit_1.currentText() == 'millimeter':
                    if self.ui.cmb_unit_2.currentText() == 'millimeter':
                        self.ui.lineEdit_2.setText(text)
                    elif self.ui.cmb_unit_2.currentText() == 'centimeter':
                        self.ui.lineEdit_2.setText(str(float(text)/10))
                    elif self.ui.cmb_unit_2.currentText() == 'meter':
                        self.ui.lineEdit_2.setText(str(float(text)/1000))
                    elif self.ui.cmb_unit_2.currentText() == 'kilometer':
                        self.ui.lineEdit_2.setText(str(float(text)/1000000))
                    elif self.ui.cmb_unit_2.currentText() == 'inch':
                        self.ui.lineEdit_2.setText(str(float(text)/25.4))
                        
                if self.ui.cmb_unit_1.currentText() == 'centimeter':
                    if self.ui.cmb_unit_2.currentText() == 'millimeter':
                        self.ui.lineEdit_2.setText(str(float(text)*10))
                    elif self.ui.cmb_unit_2.currentText() == 'centimeter':
                        self.ui.lineEdit_2.setText(text)
                    elif self.ui.cmb_unit_2.currentText() == 'meter':
                        self.ui.lineEdit_2.setText(str(float(text)/100))
                    elif self.ui.cmb_unit_2.currentText() == 'kilometer':
                        self.ui.lineEdit_2.setText(str(float(text)/100000))
                    elif self.ui.cmb_unit_2.currentText() == 'inch':
                        self.ui.lineEdit_2.setText(str(float(text)/2.54))
                        
                if self.ui.cmb_unit_1.currentText() == 'meter':
                    if self.ui.cmb_unit_2.currentText() == 'millimeter':
                        self.ui.lineEdit_2.setText(str(float(text)*1000))
                    elif self.ui.cmb_unit_2.currentText() == 'centimeter':
                        self.ui.lineEdit_2.setText(str(float(text)*100))
                    elif self.ui.cmb_unit_2.currentText() == 'meter':
                        self.ui.lineEdit_2.setText(text)
                    elif self.ui.cmb_unit_2.currentText() == 'kilometer':
                        self.ui.lineEdit_2.setText(str(float(text)/1000))
                    elif self.ui.cmb_unit_2.currentText() == 'inch':
                        self.ui.lineEdit_2.setText(str(float(text)/0.0254))
                        
                if self.ui.cmb_unit_1.currentText() == 'kilometer':
                    if self.ui.cmb_unit_2.currentText() == 'millimeter':
                        self.ui.lineEdit_2.setText(str(float(text)*1000000))
                    elif self.ui.cmb_unit_2.currentText() == 'centimeter':
                        self.ui.lineEdit_2.setText(str(float(text)*100000))
                    elif self.ui.cmb_unit_2.currentText() == 'meter':
                        self.ui.lineEdit_2.setText(str(float(text)*1000))
                    elif self.ui.cmb_unit_2.currentText() == 'kilometer':
                        self.ui.lineEdit_2.setText(text)
                    elif self.ui.cmb_unit_2.currentText() == 'inch':
                        self.ui.lineEdit_2.setText(str(float(text)/0.0000254))

                if self.ui.cmb_unit_1.currentText() == 'inch':
                    if self.ui.cmb_unit_2.currentText() == 'millimeter':
                        self.ui.lineEdit_2.setText(str(float(text)/.03937))
                    elif self.ui.cmb_unit_2.currentText() == 'centimeter':
                        self.ui.lineEdit_2.setText(str(float(text)/.3937))
                    elif self.ui.cmb_unit_2.currentText() == 'meter':
                        self.ui.lineEdit_2.setText(str(float(text)/39.37))
                    elif self.ui.cmb_unit_2.currentText() == 'kilometer':
                        self.ui.lineEdit_2.setText(str(float(text)/39370))
                    elif self.ui.cmb_unit_2.currentText() == 'inch':
                        self.ui.lineEdit_2.setText(text)

            if self.ui.cmb_par.currentText() == 'temperature':
                if self.ui.cmb_unit_1.currentText() == 'centigrade':
                    if self.ui.cmb_unit_2.currentText() == 'centigrade':
                        self.ui.lineEdit_2.setText(text)
                    elif self.ui.cmb_unit_2.currentText() == 'fahrenheit':
                        self.ui.lineEdit_2.setText(str(float(text)*1.8+32))
                    elif self.ui.cmb_unit_2.currentText() == 'kelvin':
                        self.ui.lineEdit_2.setText(str(float(text)+273.15))

                if self.ui.cmb_unit_1.currentText() == 'fahrenheit':
                    if self.ui.cmb_unit_2.currentText() == 'centigrade':
                        self.ui.lineEdit_2.setText(str((float(text)-32)/1.8))
                    elif self.ui.cmb_unit_2.currentText() == 'fahrenheit':
                        self.ui.lineEdit_2.setText(text)
                    elif self.ui.cmb_unit_2.currentText() == 'kelvin':
                        self.ui.lineEdit_2.setText(str((float(text)-32)/1.8+273.15)) 

                if self.ui.cmb_unit_1.currentText() == 'kelvin':
                    if self.ui.cmb_unit_2.currentText() == 'centigrade':
                        self.ui.lineEdit_2.setText(str(float(text)-273.15))
                    elif self.ui.cmb_unit_2.currentText() == 'fahrenheit':
                        self.ui.lineEdit_2.setText(str((float(text)-273.15)*1.8+32))
                    elif self.ui.cmb_unit_2.currentText() == 'kelvin':
                        self.ui.lineEdit_2.setText(text)

            if self.ui.cmb_par.currentText() == 'digital volume':
                if self.ui.cmb_unit_1.currentText() == 'bit':
                    if self.ui.cmb_unit_2.currentText() == 'bit':
                        self.ui.lineEdit_2.setText(text)
                    elif self.ui.cmb_unit_2.currentText() == 'byte':
                        self.ui.lineEdit_2.setText(str(float(text)/8.0))
                    elif self.ui.cmb_unit_2.currentText() == 'kilobyte':
                        self.ui.lineEdit_2.setText(str(float(text)/8000))
                    elif self.ui.cmb_unit_2.currentText() == 'megabyte':
                        self.ui.lineEdit_2.setText(str(float(text)/8e6))
                    elif self.ui.cmb_unit_2.currentText() == 'gigabyte':
                        self.ui.lineEdit_2.setText(str(float(text)/8e9))
                    elif self.ui.cmb_unit_2.currentText() == 'terabyte':
                        self.ui.lineEdit_2.setText(str(float(text)/8e12))
                        
                if self.ui.cmb_unit_1.currentText() == 'byte':
                    if self.ui.cmb_unit_2.currentText() == 'bit':
                        self.ui.lineEdit_2.setText(str(float(text)*8.0))
                    elif self.ui.cmb_unit_2.currentText() == 'byte':
                        self.ui.lineEdit_2.setText(text)
                    elif self.ui.cmb_unit_2.currentText() == 'kilobyte':
                        self.ui.lineEdit_2.setText(str(float(text)/1000))
                    elif self.ui.cmb_unit_2.currentText() == 'megabyte':
                        self.ui.lineEdit_2.setText(str(float(text)/1e6))
                    elif self.ui.cmb_unit_2.currentText() == 'gigabyte':
                        self.ui.lineEdit_2.setText(str(float(text)/1e9))
                    elif self.ui.cmb_unit_2.currentText() == 'terabyte':
                        self.ui.lineEdit_2.setText(str(float(text)/1e12))
                        
                if self.ui.cmb_unit_1.currentText() == 'kilobyte':
                    if self.ui.cmb_unit_2.currentText() == 'bit':
                        self.ui.lineEdit_2.setText(str(float(text)*8000))
                    elif self.ui.cmb_unit_2.currentText() == 'byte':
                        self.ui.lineEdit_2.setText(str(float(text)*1000))
                    elif self.ui.cmb_unit_2.currentText() == 'kilobyte':
                        self.ui.lineEdit_2.setText(text)
                    elif self.ui.cmb_unit_2.currentText() == 'megabyte':
                        self.ui.lineEdit_2.setText(str(float(text)/1e3))
                    elif self.ui.cmb_unit_2.currentText() == 'gigabyte':
                        self.ui.lineEdit_2.setText(str(float(text)/1e6))
                    elif self.ui.cmb_unit_2.currentText() == 'terabyte':
                        self.ui.lineEdit_2.setText(str(float(text)/1e9))
                        
                if self.ui.cmb_unit_1.currentText() == 'megabyte':
                    if self.ui.cmb_unit_2.currentText() == 'bit':
                        self.ui.lineEdit_2.setText(str(float(text)*8e6))
                    elif self.ui.cmb_unit_2.currentText() == 'byte':
                        self.ui.lineEdit_2.setText(str(float(text)*1e6))
                    elif self.ui.cmb_unit_2.currentText() == 'kilobyte':
                        self.ui.lineEdit_2.setText(str(float(text)*1e3))
                    elif self.ui.cmb_unit_2.currentText() == 'megabyte':
                        self.ui.lineEdit_2.setText(text)
                    elif self.ui.cmb_unit_2.currentText() == 'gigabyte':
                        self.ui.lineEdit_2.setText(str(float(text)/1e3))
                    elif self.ui.cmb_unit_2.currentText() == 'terabyte':
                        self.ui.lineEdit_2.setText(str(float(text)/1e6))
                        
                if self.ui.cmb_unit_1.currentText() == 'gigabyte':
                    if self.ui.cmb_unit_2.currentText() == 'bit':
                        self.ui.lineEdit_2.setText(str(float(text)*8e9))
                    elif self.ui.cmb_unit_2.currentText() == 'byte':
                        self.ui.lineEdit_2.setText(str(float(text)*1e9))
                    elif self.ui.cmb_unit_2.currentText() == 'kilobyte':
                        self.ui.lineEdit_2.setText(str(float(text)*1e6))
                    elif self.ui.cmb_unit_2.currentText() == 'megabyte':
                        self.ui.lineEdit_2.setText(str(float(text)*1e3))
                    elif self.ui.cmb_unit_2.currentText() == 'gigabyte':
                        self.ui.lineEdit_2.setText(text)
                    elif self.ui.cmb_unit_2.currentText() == 'terabyte':
                        self.ui.lineEdit_2.setText(str(float(text)/1e3))
                        
                if self.ui.cmb_unit_1.currentText() == 'terabyte':
                    if self.ui.cmb_unit_2.currentText() == 'bit':
                        self.ui.lineEdit_2.setText(str(float(text)*8e12))
                    elif self.ui.cmb_unit_2.currentText() == 'byte':
                        self.ui.lineEdit_2.setText(str(float(text)*1e12))
                    elif self.ui.cmb_unit_2.currentText() == 'kilobyte':
                        self.ui.lineEdit_2.setText(str(float(text)*1e9))
                    elif self.ui.cmb_unit_2.currentText() == 'megabyte':
                        self.ui.lineEdit_2.setText(str(float(text)*1e6))
                    elif self.ui.cmb_unit_2.currentText() == 'gigabyte':
                        self.ui.lineEdit_2.setText(str(float(text)*1e3))
                    elif self.ui.cmb_unit_2.currentText() == 'terabyte':
                        self.ui.lineEdit_2.setText(text)

        except ValueError:
            # convert '-' to float, i knew that 😑
            pass

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()

app.exec()