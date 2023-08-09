
class Account:

    def __init__(self, name: str) -> None:
        """
        Function to create an account object.
        :param name: Account name.
        """
        
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Function to deposit funds.
        :param amount: amount to deposit
        :return: True if succesful, False if not
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False
        
    def withdraw(self, amount: float) -> bool:
        """
        Function to withdraw funds.
        :param amount: amount to withdraw
        :return: True if succesful, False if not
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
        
    def get_balance(self) -> float:
        """
        Function to get account balance.
        :return: Account balance
        """
        return self.__account_balance
    
    def get_name(self) -> str:
        """
        Function to get account name.
        :return: Account name
        """
        return self.__account_name