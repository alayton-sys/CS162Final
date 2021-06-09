# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 20:09:07 2021

@author: Arianna
"""

class Account:
    def __init__(self, first_name = 'none', last_name = 'none', account_number = 0, email = 'none', status = 'Active', phone_number = 0, pin = 0, balance = 0.00):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.email = email
        self.status = status
        self.phone_number = phone_number
        self.pin = pin
        self.balance = balance