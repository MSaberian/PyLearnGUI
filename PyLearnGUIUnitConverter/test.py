from PySide6.QtWidgets import QWidget, QListWidget, QVBoxLayout, QPushButton

class SortPriorityObjectsIndex(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.list = QListWidget()

        self.list.addItem('Item 1')
        self.list.addItem('Item 2')
        self.list.addItem('Item 3')
        self.list.addItem('Item 4')

        sort_btn = QPushButton('Sort', self)
        sort_btn.clicked.connect(self.sortItems)

        vbox = QVBoxLayout()
        vbox.addWidget(self.list) 
        vbox.addWidget(sort_btn) 

        self.setLayout(vbox) 

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Sort Priority Objects Index')    
        self.show()

    def sortItems(self):  # sorting items in list widget by priority index 

         for i in range (0, 4):  # loop through all items in list widget 

            item = self.list .item (i)   # get item from list widget 

            priority_index = int (item .text ()[-1])   # get the priority index from the item text string 

            item .setData (Qt .UserRole , priority_index )   # set the data for the item with the priority index as value  

         # sort items by their data value using Qt's built-in sorting function 

         self .list .sortItems (Qt .AscendingOrder )

app = QApplication(sys.argv)
main_window = SortPriorityObjectsIndex()
main_window.show()

app.exec()