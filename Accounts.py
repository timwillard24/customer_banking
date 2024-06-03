""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance=0.0, interest_rate=0.0):
        self.balance = balance
        self.interest_rate = interest_rate
        self.interest_earned = 0.0

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest_earned = interest
    def get_balance(self):
        return self.balance
    def get_interest(self):
        return self.interest_earned
    # This method adds the given amount to the account balance.
    def deposit(self, amount):
        self.balance += amount