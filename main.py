from PyQt5 import *
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from addsubsgui import Ui_Form
from addsubsgui import *
import sys
import string
import random


class AppWindow(QDialog):
    

    
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()

    def add(self):
        self.ui.operator_lb.setText("+")
        
    def minus(self):
        self.ui.operator_lb.setText("-")

    def generate_numbers(self):
        self._num1 = 0
        self._num2 = 0
        self.correct_answer = 0
        self.ui.user_answer_tb.setText("") 
        self.ui.num1_label.setText("")
        self.ui.num2_label.setText("")
        self.ui.answer_label.setText("?")
        self.ui.answer_tb.setText("")

        if self.ui.minus_rb.isChecked() :
            self._num1 = random.randint(1,10)
            self._num2 = random.randint(1, self._num1)
            self.ui.num1_label.setText(str(self._num1))
            self.ui.num2_label.setText(str(self._num2))
        elif self.ui.add_rb.isChecked() : 
            self._num1 = 0
            self._num2 = 0
            self._num1 = random.randint(1,10)
            self._num2 = random.randint(1,10)
            self.ui.num1_label.setText(str(self._num1))
            self.ui.num2_label.setText(str(self._num2))
        elif (self.ui.add_rb.isChecked() == False and self.ui.minus_rb.isChecked() == False) : 
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Select the Operator to be used")
            msgBox.setWindowTitle("No Operator Found")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msgBox.exec()


    def answer(self):
        
        if self.ui.answer_tb.text() == "" :
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Enter your answer!")
            msgBox.setWindowTitle("No answer Found")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msgBox.exec()
     
        elif self.ui.add_rb.isChecked() :
            self.correct_answer = self._num1  + self._num2
            if self.correct_answer == int(self.ui.answer_tb.text()):
                self.ui.user_answer_tb.setText("Correct!")               
                self.ui.answer_label.setText(str(self.correct_answer))
            else :
                self.ui.user_answer_tb.setText("Wrong!")
        elif self.ui.minus_rb.isChecked() :
            self.correct_answer = self._num1  - self._num2
            if self.correct_answer == int(self.ui.answer_tb.text()):
                self.ui.user_answer_tb.setText("Correct!")               
                self.ui.answer_label.setText(str(self.correct_answer))
            else :
                self.ui.user_answer_tb.setText("Wrong!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())