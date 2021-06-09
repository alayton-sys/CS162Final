# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 20:52:35 2021

@author: Arianna
@Plotting accounts
"""
names = []
balances = []



import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import csv


def plot_all_accounts():
    with open('data.txt', "w") as my_output_file:
        with open('all_accounts.csv', "r") as my_input_file:
            [ my_output_file.write(",".join(row)+'\n') for row in csv.reader(my_input_file)]
        my_output_file.close()
    
    myfile = open('data.txt')
    lines = myfile.readlines()
    myfile.close()
    
    del lines[0]
    
    new_file = open("data.txt", "w+")
    
    for line in lines:
        new_file.write(line)
    
    new_file.close()
    
    myfile = open('data.txt')
    contents = myfile.read().splitlines() 
    for line in contents:
        first_name, b, c, d, e, f, g, h, balance = line.split(',')
        names.append(first_name)
        balances.append(int(balance))
        savings_account_dict[c] = balance
        checking_account_dicts[c] = balance
    
    plt.bar(names, balances, color='pink')
    plt.title('Total amount (in dollars) in each account')
    plt.xlabel('Account Name')
    plt.ylabel('Amount (in dollars)')
    plt.show()

plot_all_accounts()
