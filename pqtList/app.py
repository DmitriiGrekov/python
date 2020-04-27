from formaded import Ui_Aded
from PyQt5 import QtWidgets
from lists import Ui_Form 
import sys
 
  
class mywindow(QtWidgets.QMainWindow):
    title=''
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Aded()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.buttonAded.clicked.connect(self.adedList)
        self.ui.listView.addItem(title)

    def adedList(self):
        print('Добавлено')
        self.title = self.ui.titleLine.text()
        text = self.ui.textLine.toPlainText()
        date = self.ui.dateLine.text()

        
        
                                       
                                    
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
                                     
sys.exit(app.exec())
