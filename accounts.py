#Copyright (c) 2023 Nikolaus Luebbert
#All rights reserved. Although I will probably give you permission to use it for whatever you want to do with it if you ask me first.

class Account:
    IS_SAVINGS_ACCOUNT = False
    def __init__(self, name, balance=0) -> None:
        '''
        Initalizes a new bank account.
        :param name: String (Name for the new bank account)
        ;param balance: Float (Starting balance of the account. (defaults to zero))
        '''
        self.__account_name = name
        #self.__account_balance = balance
        self.set_balance(balance)

    def deposit(self, amount) -> bool:
        '''
        Deposits the amount of money specified into the account.
        If amount is less than or equal to zero, False will be returned and the balance will remain unchanged. Otherwise, True will be returned.
        :param amount: Float (Amount of money to deposit into the account.)
        :return: Boolean ('False' if amount <=0. 'True' if amount > 0)
        '''
        if amount <= 0: #changed from < to <= per in-person instructions.
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount) -> bool:
        '''
        Withdraws money from the bank account.
        If the amount is less than zero or more than the account balance, it will return False.
        :param amount: Float (Amount of money to deposit into the account)
        '''
        if amount < 0 or amount > self. __account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> int:
        '''
        Returns the balance of the account.
        :return: Balance (Float)
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Returns the account name.
        :return: __account_name (String)
        '''
        return self.__account_name

    def set_balance(self, value) -> None:
        '''
        Sets the balance for the account. If the balance is negative, the balance will default to 0.
        :param value: floating point number to attempt to set as the balance.
        '''
        if value < 0:
            self.__account_balance = 0
        else:
            self.__account_balance = value

    def set_name(self, value) -> None:
        '''
        Sets the name of the account to a new string.
        :param: Value (String containing the new name)
        '''
        self.__account_name = value

    def __str__(self) -> str:
        '''
        Returns a formatted overview of the current bank account.
        :return: String
        '''
        return f'Account name = {self.get_name()}, Account balance = {self.get_balance():.2f}'

class SavingAccount(Account):
    IS_SAVINGS_ACCOUNT = True
    MINIMUM = 100
    RATE = 0.02
    
    def __init__(self, name) -> None:
        '''
        Initalizes a new savings account. It will have a default amount of SavingAccount.MINIMUM
        :param name: String (Name for the new bank account)
        '''
        super().__init__(name, self.MINIMUM)
        self.__deposit_count = 0
       

    def apply_interest(self) -> None:
        '''
        Adds the amount of interest dictated by SavingAccount.RATE every fifth successful deposit.
        '''
        if self.__deposit_count % 5 == 0 and self.__deposit_count != 0:
            super().deposit((float(self.get_balance()) * SavingAccount.RATE))
        
    def deposit(self, amount) -> bool:
        '''
        Deposits the amount of money specified into the account.
        If amount is less than or equal to zero, False will be returned and the balance will remain unchanged. Otherwise, True will be returned.
        For every fifth successful deposit, apply_interest() will be applied to the balance.
        :param amount: Float (Amount of money to deposit into the account.)
        :return: Boolean ('False' if amount <=0. 'True' if amount > 0)
        '''
        output = super().deposit(amount)
        if output == True:
            self.__deposit_count += 1
        self.apply_interest()
        return output
        
    def withdraw(self, amount) -> bool:
        if (float(self.get_balance()) - amount) >= SavingAccount.MINIMUM:
            return super().withdraw(amount) 
        else:
            return False

    def get_balance(self) -> float:
        return super().get_balance()

    def get_name(self) -> str:
        return super().get_name()

    def set_balance(self, value) -> None:
        super().set_balance(value) #changed from (self, value) during lecture.

    def set_name(self, value) -> None:
        super().set_name(value) #changed from (self, value) during lecture.

    def __str__(self) -> str:
        return "SAVING ACCOUNT: " + super().__str__()
        #return f'SAVING ACCOUNT: Account name = {self.__account_name}, Account balalnce = {self.__account_balance:.2f}'
        
        
    

#for testing purposes:
