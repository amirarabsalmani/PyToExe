from PyQt4.QtCore import *
from PyQt4.QtGui import *
from main import *
import sys
import os



class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Ui()
        self.Widgets()


    def Ui(self): # To MainWindows Setting
        self.setWindowTitle("Py To Exe")
        self.setFixedSize(706,511)


    def Widgets(self):
        self.toolButton.clicked.connect(self.open_python_file)
        self.toolButton_2.clicked.connect(self.save_exe_file)
        self.toolButton_3.clicked.connect(self.icon_select)
        self.checkBox.toggled.connect(self.Disable)
        self.pushButton_4.clicked.connect(self.console)




    def open_python_file(self):
        # path = "C:\\"
        # newPath = path.replace(os.sep, '/')
        fname = QFileDialog.getOpenFileName(self, 'Python File',"" , "Python Files(*.py)")
        self.lineEdit.setText(fname)



    def save_exe_file(self):
        fsave = QFileDialog.getExistingDirectory(self,"Select ")
        self.lineEdit_2.setText(fsave)


    def icon_select(self):
        fname = QFileDialog.getOpenFileName(self, "Icon File", "", "icon Files(*.ico)")
        self.lineEdit_3.setText(fname)


    def Disable(self):
        if self.checkBox.isChecked() == True:
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_3.clear()
            self.toolButton_3.setEnabled(False)
        else:
            self.lineEdit_3.setEnabled(True)
            self.toolButton_3.setEnabled(True)



    """ Radio Buttons """
    def console(self):
        if self.radioButton_2.isChecked() == True:
            os.system('pyinstaller -i="{}" --name={} --distpath={} -F "{}"'.format(self.lineEdit_3.text(), self.lineEdit_4.text(),self.lineEdit_2.text() ,self.lineEdit.text()))
            QMessageBox.information(self,"Show Window", "Done !!")



        elif self.radioButton_3.isChecked() == True:
            os.system('pyinstaller -i="{}" --windowed --name={} --distpath={} -F "{}"'.format(self.lineEdit_3.text(),self.lineEdit_4.text(),self.lineEdit_2.text() ,self.lineEdit.text()))
            QMessageBox.information(self, "Hiden Windows", "Done !")







def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()