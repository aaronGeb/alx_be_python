#!/usr/bin/env python3
"""A class to represent a bank account."""


class BankAccount:
    """A bank account that can be used to store money and withdraw it."""

    def __init__(self, account_balance=0):
        """Initialize the bank account with a starting balance."""
        self.account_balance = account_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient funds are available in the account."""
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance:{self.account_balance}")
