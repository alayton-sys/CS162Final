# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 19:56:46 2021

@author: Arianna
"""

from Account_File import Account


class Checking(Account):
    def __init__(self):
        Account.__init__(self)
        
    def getbalance(self):
        return self.balance

    def makePayment(self, checking_account_dict):
        search_account_num = input('Enter account number: ')
        amt = float(input('Enter the amount to be deposited: '))
        checking_account_dict[search_account_num] += amt
        print('Amount successfully deposited. New balance: {:,.2f}'.format(checking_account_dict[search_account_num]))
    
    def addCharge(self, checking_account_dict):
        search_account_num = input('Enter account number: ')
        amt = float(input('Enter the amount to be withdrawn: '))
        if checking_account_dict[search_account_num] >= amt:
            checking_account_dict[search_account_num] -= amt
            print("\n You Withdrew:", amt)
            print('New balance: {:,.2f}'.format(checking_account_dict[search_account_num]))
        else:
            print("\n Insufficient balance :(")
   
    def printAccountInfo(self):
        print('Account information for {} {}:'.format(self.first_name, self.last_name))
        print('Account Number: {}'.format(self.account_number))
        print('Account Balance: ${:,.2f}'.format(self.balance))
        print('Account status: {}'.format(self.status))
        
checking_account_dict = {}
