# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 20:00:20 2021

@author: Arianna
"""

from Account_File import Account


class Savings(Account):
    def __init__(self):
        Account.__init__(self)
        
    def getbalance(self):
        return self.balance

    def makePayment(self, savings_account_dict):
        search_account_num = input('Enter account number: ')
        amt = float(input('Enter the amount to be deposited: '))
        savings_account_dict[search_account_num] += amt
        print('Amount successfully deposited. New balance: {:,.2f}'.format(savings_account_dict[search_account_num]))
    
    def addCharge(self, savings_account_dict):
        search_account_num = input('Enter account number: ')
        amt = float(input('Enter the amount to be withdrawn: '))
        if savings_account_dict[search_account_num] >= amt:
            savings_account_dict[search_account_num] -= amt
            print("\n You Withdrew:", amt)
            print('New balance: {:,.2f}'.format(savings_account_dict[search_account_num]))
        else:
            print("\n Insufficient balance :(")
        
    def printAccountInfo(self):
        print('Account information for {} {}:'.format(self.first_name, self.last_name))
        print('Account Number: {}'.format(self.account_number))
        print('Account Balance: ${:,.2f}'.format(self.balance))
        print('Account status: {}'.format(self.status))
        
savings_account_dict = {}
