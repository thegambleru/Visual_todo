import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets

qtCreatorFile = "to_do_list.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.AddButton.clicked.connect(self.Add_Item)
        self.RemoveButton.clicked.connect(self.Remove_Item)
    
    def Add_Item(self):
        item_to_be_added = str(self.ItemName.text())
        self.ListItems.addItem(item_to_be_added)

    def Remove_Item(self):
        if str(self.ListItems.currentItem()) != "None":
            item_to_be_removed = str(self.ListItems.currentItem().text())
            if item_to_be_removed != "NoneType":
                self.RemovedItems.addItem(item_to_be_removed)
                removed_item_index = self.ListItems.currentRow()
                self.ListItems.takeItem(removed_item_index)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
