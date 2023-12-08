#Copyright (c) 2023 Nikolaus Luebbert
#All rights reserved. Although I will probably give you permission to use it for whatever you want to do with it if you ask me first.
from PyQt5.QtWidgets import * #QMainWindow
from gui import *
from accounts import *
import csv

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.currAccount = Account("Unnamed Account")

        self.accountNameLabel.setText(self.currAccount.get_name())
        self.currentBalanceLabel.setText("${:.2f}".format(self.currAccount.get_balance()))
        self.errorLabel.setText("")
        
        
        self.withdrawButton.clicked.connect(lambda : self.withdraw_handler())
        self.depositButton.clicked.connect(lambda : self.deposit_handler())
        self.setBalanceButton.clicked.connect(lambda : self.set_balance_handler())
        self.saveButton.clicked.connect(lambda : self.save_button_handler())
        self.loadButton.clicked.connect(lambda : self.load_button_handler())
        self.changeNameButton.clicked.connect(lambda : self.set_account_name_handler())

        self.newAccountButton.clicked.connect(lambda : self.new_account_handler())
        self.newSavingsAccountButton.clicked.connect(lambda : self.new_savings_account_handler())
        


    def withdraw_handler(self):
        try:
            self.withdrawAmount = float(self.withdrawAmountEntry.text())
            self.withdrawResult = self.currAccount.withdraw(self.withdrawAmount)
            if self.withdrawResult == False:
                self.errorLabel.setText("You can't withdraw $0.00 or more than is in your account.")
            else:
                self.errorLabel.setText("") #clear error text upon correct execution.
                self.currentBalanceLabel.setText("${:.2f}".format(self.currAccount.get_balance())) #set new balance on the display.
        except:
            self.errorLabel.setText("Make sure the withdraw amount is a floating point number.")
            

    def deposit_handler(self):
        try:
            self.depositAmount = float(self.depositAmountEntry.text())
            self.depositResult = self.currAccount.deposit(self.depositAmount)
            if self.depositResult == False:
                self.errorLabel.setText("The deposit amount needs to be greater than zero.")
            else:
                self.errorLabel.setText("") #clear error text upon correct execution.
                self.currentBalanceLabel.setText("${:.2f}".format(self.currAccount.get_balance())) #set new balance on the display.
                     
        except:
            self.errorLabel.setText("Make sure what you entered for the deposit amount was a float.")
            
    
        
    def set_balance_handler(self):
        try:
            self.balanceAmount = float(self.setBalanceEntry.text())
            self.currAccount.set_balance(self.balanceAmount)
                
            self.errorLabel.setText("") #clear error text upon correct execution.
            self.currentBalanceLabel.setText("${:.2f}".format(self.currAccount.get_balance())) #set new balance on the display.

        except:
           self.errorLabel.setText("Make sure your new balance is a floating point number.")
            
        

    def save_button_handler(self):
        try:
            self.output_file_name = self.saveFileEntry.text()
            self.output_csv = open(self.output_file_name, "w", newline="")
            self.output_csv_interface = csv.writer(self.output_csv) 

            #So I can record whether it is a savings account or not.
            if self.currAccount.IS_SAVINGS_ACCOUNT == False:
                self.isSavingsAccount = False
            else:
                self.isSavingsAccount = True

            self.output_line = [str(self.currAccount.get_name()), str(self.currAccount.get_balance()), str(self.isSavingsAccount)]

            self.output_csv_interface.writerow(self.output_line)
            self.output_csv.close()
            self.errorLabel.setText("") #clear error text upon correct execution.
            
        except:
            self.errorLabel.setText("Make sure the file name is acceptable to your OS and you have perission to write to it.")

    def load_button_handler(self):
        try:
            self.input_file_name = self.loadFileEntry.text()
            self.input_csv = open(self.input_file_name, "r", newline="")
            self.input_csv_interface = csv.reader(self.input_csv)
            
            self.read_line = next(self.input_csv_interface)
            

            #Savings or regular account? Also, loading the name of the account:
            if self.read_line[2] == "True": #if isSavingsAccount == True:
                self.currAccount = SavingAccount(self.read_line[0]) #readLine[0] = account name. Passing it to the new account.
                self.accountTypeLabel.setText("Savings Account")
            else: 
                self.currAccount = Account(self.read_line[0]) #readLine[0] = account name. Passing it to the new account.
                self.accountTypeLabel.setText("Basic Account")

            #Loading the amount for the account:
            self.currAccount.set_balance(float(self.read_line[1]))
                

            self.accountNameLabel.setText(self.currAccount.get_name()) #set the default name of the new savings account
            self.errorLabel.setText("") #clear error text upon correct execution.
            self.currentBalanceLabel.setText("${:.2f}".format(self.currAccount.get_balance())) #set new balance on the display.
            
        except:
            self.errorLabel.setText("Are you sure you typed the file name correctly?\n In addition, is the provided file designed for use with this program?")
        

    def set_account_name_handler(self):
        try:
            self.newAccountName = self.newAccountNameEntry.text()
            self.currAccount.set_name(self.newAccountName)
            self.accountNameLabel.setText(self.currAccount.get_name())
            self.errorLabel.setText("")
        except:
            self.errorLabel.setText("For some reason, we couldn't set your account name to this entry.")
            

    def new_account_handler(self):
        self.currAccount = Account("Unnamed Account")
        self.accountNameLabel.setText(self.currAccount.get_name()) #set the default name of the new savings account
        self.errorLabel.setText("") #clear error text upon correct execution.
        self.currentBalanceLabel.setText("${:.2f}".format(self.currAccount.get_balance())) #set new balance on the display.
        self.accountTypeLabel.setText("Basic Account")

    def new_savings_account_handler(self):
        self.currAccount = SavingAccount("Unnamed Savings Account")
        self.accountNameLabel.setText(self.currAccount.get_name()) #set the default name of the new savings account
        self.errorLabel.setText("") #clear error text upon correct execution.
        self.currentBalanceLabel.setText("${:.2f}".format(self.currAccount.get_balance())) #set new balance on the display.
        self.accountTypeLabel.setText("Savings Account")
