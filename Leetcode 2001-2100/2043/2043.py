# Leetcode 2043: Simple Bank System
# https://leetcode.com/problems/simple-bank-system/
# Solved on 26th of October, 2025
class Bank:

    def __init__(self, balance: list[int]):
        self.accountBalances = balance
        self.numAccounts = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < 1 or account1 > self.numAccounts or \
                account2 < 1 or account2 > self.numAccounts:
            return False

        index1 = account1 - 1
        index2 = account2 - 1

        if self.accountBalances[index1] < money:
            return False

        self.accountBalances[index1] -= money
        self.accountBalances[index2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account < 1 or account > self.numAccounts:
            return False

        index = account - 1
        self.accountBalances[index] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account > self.numAccounts:
            return False

        index = account - 1

        if self.accountBalances[index] < money:
            return False

        self.accountBalances[index] -= money
        return True