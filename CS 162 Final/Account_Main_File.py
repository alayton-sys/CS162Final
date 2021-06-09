# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 13:15:38 2021

@author: Arianna
@CS 162 Final Project
"""

from Checking_File import Checking
from Savings_File import Savings

import csv
import random


def createSavingsAccount():
    print('\nCREATE ACCOUNT\n')
    new_account = Savings()
    new_account.first_name = (input('Enter the customer\'s first name: ')).title()
    new_account.last_name = (input('Enter the customer\'s last name: ')).title()
    new_account.account_number = (new_account.first_name[0]+new_account.last_name[0]+str(random.randint(100000,999999)))
    new_account.email = (input('Enter the customer\'s email: '))
    new_account.phone_number = (input('Enter the customer\'s phone number: '))
    new_account.status = 'Active'
    new_account.balance = int(input('Enter the customer\'s starting balance: '))
    new_account.pin = 0000
    verify_pin = 1111
    while new_account.pin != verify_pin: #verifies that the pin is correctly entered twice
    	new_account.pin = input("Create a four didgit pin: ")
    	verify_pin = input("Enter pin again to confirm: ")
    	print("")
    	if new_account.pin != verify_pin:
    		print("Pin does not match. Please try again.")
    new_account_list = [new_account.first_name, new_account.last_name, new_account.account_number, new_account.phone_number, new_account.email, 'Savings', new_account.status, new_account.pin, new_account.balance]          
    
    rows.append(new_account_list)
    savings_account_dict[new_account.account_number] = new_account.balance
    print('\nAccount #{} successfully created!'.format(new_account.account_number))
    return new_account

def createCheckingAccount():
    print('\nCREATE ACCOUNT\n')
    new_account = Checking()
    new_account.first_name = (input('Enter the customer\'s first name: ')).title()
    new_account.last_name = (input('Enter the customer\'s last name: ')).title()
    new_account.account_number = (new_account.first_name[0] + new_account.last_name[0] + str(random.randint(100000,999999)))
    new_account.email = (input('Enter the customer\'s email: '))
    new_account.phone_number = (input('Enter the customer\'s phone number: '))
    new_account.status = 'Active'  
    new_account.balance = int(input('Enter the customer\'s starting balance: '))    
    new_account.pin = 0000
    verify_pin = 1111
    while new_account.pin != verify_pin: #verifies that the pin is correctly entered twice
    	new_account.pin = input("Create a four didgit pin: ")
    	verify_pin = input("Enter pin again to confirm: ")
    	print("")
    	if new_account.pin != verify_pin:
    		print("Pin does not match. Please try again")
    new_account_list = [new_account.first_name, new_account.last_name, new_account.account_number, new_account.phone_number, new_account.email, 'Checking', new_account.status, new_account.pin, new_account.balance]          
    rows.append(new_account_list)
    checking_account_dict[new_account.account_number] = new_account.balance
    print('\nAccount #{} successfully created!'.format(new_account.account_number))
    return new_account

def linear_search(search_list, search_terms):
    terms_list = search_terms.split()
    print("\nSearch results:")
    print("{} {} {} {} {} {} {}".format('_' * 20, '_' * 20, '_' * 20, '_' * 12, '_' * 30, '_' * 10, '_' * 10))
    print("{:<20} {:<20} {:<20} {:<12} {:<30} {:<10} {:<10}".format("First Name", "Last Name", "Account Number", "Phone Number", "Email", "Type", "Status"))
    print("{} {} {} {} {} {} {}".format('_' * 20, '_' * 20, '_' * 20, '_' * 12, '_' * 30, '_' * 10, '_' * 10))
    
    for index, i in enumerate(search_list):
        for ii in terms_list:
            if ii in i:
                print("{:<20} {:<20} {:<20} {:<12} {:<30} {:<10} {:<10}".format(first_name_list[index], last_name_list[index], account_number_list[index], phone_number_list[index], email_list[index], account_type_list[index], status_list[index]))
                
    
        
def print_menu():
    choice = None
    while choice != "n":
        print("\nChoose search option: ")
        print("0 - First Name ")
        print("1 - Last Name ")
        print("2 - Account Number ")
        print("3 - Phone Number ")
        print("4 - Email ")
        print("5 - Account Type")
        print("6 - Status ")
        
        choice = input("---> ")
        
        if choice == "0":
            first_name_search()
        elif choice == "1":
            last_name_search()
        elif choice == "2":
            account_number_search()
        elif choice == "3":
            phone_number_search()
        elif choice == "4":
            email_search()
        elif choice == "5":
            account_type_search()
        elif choice == "6":
            status_search()
        choice = input("Search again? (y) / (n)\n")
        
def first_name_search():  
    search_terms = input("Enter search term(s): ")
    linear_search(first_name_list, search_terms)
def last_name_search():  
    search_terms = input("Enter search term(s): ")
    linear_search(last_name_list, search_terms)
def account_number_search():  
    search_terms = input("Enter search term(s): ")
    linear_search(account_number_list, search_terms)
def phone_number_search():
    search_terms = input("Enter search term(s): ")
    linear_search(phone_number_list, search_terms)
def email_search():
    search_terms = input("Enter search term(s): ")
    linear_search(email_list, search_terms)
def account_type_search():
    search_terms = input("Enter search term(s): ")
    linear_search(account_type_list, search_terms)
def status_search():
    search_terms = input("Enter search term(s): ")
    linear_search(status_list, search_terms)
    

def clearlists():
    first_name_list.clear()
    last_name_list.clear()
    account_number_list.clear()
    phone_number_list.clear()
    email_list.clear()
    account_type_list.clear()
    status_list.clear()
    
    result_list.clear()


    
names = []
balances = []
        
first_name_list = []
last_name_list = []
account_number_list = []
phone_number_list = []
email_list = []
account_type_list = []
status_list = []

result_list = []        

names = []
balances = []

############################################################################################ plotting stuff
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt



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

    
    
    plt.bar(names, balances, color='pink')
    plt.title('Total amount (in dollars) in each account')
    plt.xlabel('Account Name')
    plt.ylabel('Amount (in dollars)')
    plt.show()
    
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
checking_account_dict = {}
savings_account_dict = {}

myfile = open('data.txt')
contents = myfile.read().splitlines() 
for line in contents:
    first_name, b, c, d, e, f, g, h, balance = line.split(',')
    names.append(first_name)
    balances.append(int(balance))
    savings_account_dict[c] = int(balance)
    checking_account_dict[c] = int(balance)
#########################################################################################################

def menu():
    print(' _______   _______         _______                       __')     
    print('|       \ |       \       |       \                     |  \    ')  
    print('| $$$$$$$\| $$$$$$$\      | $$$$$$$\  ______   _______  | $$   __ ')
    print('| $$__/ $$| $$__/ $$      | $$__/ $$ |      \ |       \ | $$  /  \ ')
    print('| $$    $$| $$    $$      | $$    $$  \$$$$$$\| $$$$$$$\| $$_/  $$')
    print('| $$$$$$$ | $$$$$$$       | $$$$$$$\ /      $$| $$  | $$| $$   $$ ')
    print('| $$      | $$            | $$__/ $$|  $$$$$$$| $$  | $$| $$$$$$\ ')
    print('| $$      | $$            | $$    $$ \$$    $$| $$  | $$| $$  \$$\ ')
    print(' \$$       \$$             \$$$$$$$   \$$$$$$$ \$$   \$$ \$$   \$$ ')
    print('\nPP Bank Management System Menu\n')
    print('1 - Create Account')
    print('2 - Delete Account')
    print('3 - Add Funds')
    print('4 - Make a Withdrawal')
    print('5 - Account Search')
    print('6 - Sort all accounts')
    print('7 - Plot all accounts')
    print('8 - Exit')
    
def account_menu():
    print('\nAccount Management Menu\n')
    print('1 - Checking Account')
    print('2 - Savings Account')
    print('3 - Back')

#   ######################################################################################   QUICKSORT
def sort():
    contents = []   
    myfile = open('data.txt')
    contents = myfile.read().splitlines() 
    
    
    def partition(contents, i, k):
        pivot = contents[k]
        index = i - 1
        for j in range(i,k):
            if contents[j] <= pivot:
                index += 1
                contents[index], contents[j] = contents[j], contents[index]
        contents[index + 1], contents[k] = contents[k], contents[index + 1]
        return index + 1
        
    def quicksort(contents, i, k):
        if i < k:
            piv = partition(contents, i, k)
            quicksort(contents, i, piv - 1)
            quicksort(contents, piv + 1, k)
      
    quicksort(contents, 0, len(contents) - 1)
    
    with open('sorted_data.txt', 'w+') as output_file:
        for thingy in contents:
            output_file.write(thingy + '\n')
    output_file.close()

#   ######################################################################################




rows = []  
login = ''
c = Checking()
s = Savings()

    
user_input = ''

try:
    
    while user_input != 8:
        menu()
        user_input = int(input('Choose an option: '))
        if user_input == 1:
            account_menu()
            user_input = int(input('Choose an option: '))
            while user_input != 3:
                if user_input == 1:
                    createCheckingAccount()
                    filename = "all_accounts.csv"
                    with open('all_accounts.csv', 'a', newline='') as csvfile:
                        a = csv.writer(csvfile, delimiter=',')
                        a.writerows(rows)
                        csvfile.close()
                    filename = "checking_accounts.csv"
                    with open('checking_accounts.csv', 'a', newline='') as csvfile:
                        a = csv.writer(csvfile, delimiter=',')
                        a.writerows(rows)
                        csvfile.close()
                    user_input = 3
                                                                                    # OPEN CHECKING ACCOUNT
                elif user_input == 2:
                    createSavingsAccount()
                    filename = "all_accounts.csv"
                    with open('all_accounts.csv', 'a', newline='') as csvfile:
                        a = csv.writer(csvfile, delimiter=',')
                        a.writerows(rows)
                        csvfile.close()
                    filename = "savings_accounts.csv"
                    with open('savings_accounts.csv', 'a', newline='') as csvfile:
                        a = csv.writer(csvfile, delimiter=',')
                        a.writerows(rows)
                        csvfile.close()
                    user_input = 3
                else:
                    raise RuntimeError()
                                                                                  # OPEN SAVINGS ACCOUNT
                
            print('------------------------------------------------------')
            
            
        elif user_input == 2:
            account_menu()
            user_input = int(input('Choose an option: '))
                
            while user_input != 3:
                if user_input == 1:
                    updatedlist=[]
                    account_to_delete = input("Please enter the account number to be deleted: ")                             
                    with open('all_accounts.csv', newline="") as f:
                        reader = csv.reader(f)
     
                        for row in reader:
                            if account_to_delete not in row:
                                updatedlist.append(row)
                        with open('all_accounts.csv', 'w', newline='') as f:
                            a = csv.writer(f, delimiter=',')
                            a.writerows(updatedlist)
                            f.close()
                        f.close() 
                    with open('checking_accounts.csv', newline="") as f:
                        reader = csv.reader(f)
     
                        for row in reader:
                            if account_to_delete not in row:
                                updatedlist.append(row)
                        with open('checking_accounts.csv', 'w', newline='') as f:
                            a = csv.writer(f, delimiter=',')
                            a.writerows(updatedlist)
                            f.close()
                            print("Account has been deleted")                                
                        f.close()            
                    user_input = 3                             
                                                                                    # CLOSE CHECKING ACCOUNT
                elif user_input == 2:
                    updatedlist=[]
                    account_to_delete = input("Please enter the account number to be deleted: ")                             
                    with open('all_accounts.csv', newline="") as f:
                        reader = csv.reader(f)
     
                        for row in reader:
                            if account_to_delete not in row:
                                updatedlist.append(row)
                        with open('all_accounts.csv', 'w', newline='') as f:
                            a = csv.writer(f, delimiter=',')
                            a.writerows(updatedlist)
                            f.close()                                
                        f.close() 
                    with open('savings_accounts.csv', newline="") as f:
                        reader = csv.reader(f)
     
                        for row in reader:
                            if account_to_delete not in row:
                                updatedlist.append(row)
                        with open('savings_accounts.csv', 'w', newline='') as f:
                            a = csv.writer(f, delimiter=',')
                            a.writerows(updatedlist)
                            f.close()
                            print("Account has been deleted")                                
                        f.close()
                    user_input = 3  
                else:
                    raise RuntimeError()
                                                                                    # CLOSE SAVINGS ACCOUNT
                
            print('------------------------------------------------------')
    
            
            
        elif user_input == 3:
            account_menu()
            user_input = int(input('Choose an option: '))
            while user_input != 3:
                if user_input == 1:
                    print('\n----------ADD FUNDS----------\n')
                    c.makePayment(checking_account_dict)
    
                    user_input = 3                
      
                    # PAYMENT CHECKING ACCOUNT
                elif user_input == 2:
                    print('\n----------ADD FUNDS----------\n')
                    s.makePayment(savings_account_dict)
    
                    user_input = 3 
                else:
                    raise RuntimeError()
                    
                    
                    # PAYMENT SAVINGS ACCOUNT
                
            print('------------------------------------------------------')
    
            
        elif user_input == 4:
            account_menu()
            user_input = int(input('Choose an option: '))
            while user_input != 3:
                if user_input == 1:
                    print('\n----------MAKE WITHDRAWAL----------\n')
                    c.addCharge(checking_account_dict)
    
                    user_input = 3                
      
                    # PAYMENT CHECKING ACCOUNT
                elif user_input == 2:
                    print('\n----------MAKE WITHDRAWAL----------\n')
                    s.addCharge(savings_account_dict)
    
                    user_input = 3 
                else:
                    raise RuntimeError()
                
            print('------------------------------------------------------')
    

        elif user_input == 5:                                                   #account search
            clearlists()                                          
            with open("all_accounts.csv", "r") as vg:
                for line in vg.readlines():
                    vg_line_split = line.split(",")
                    
                    first_name_list.append(vg_line_split[0])
                    last_name_list.append(vg_line_split[1])
                    account_number_list.append(vg_line_split[2])
                    phone_number_list.append(vg_line_split[3])
                    email_list.append(vg_line_split[4])
                    account_type_list.append(vg_line_split[5])
                    status_list.append(vg_line_split[6])
            print_menu()
            
            print('------------------------------------------------------')
    
            vg_line_split = []
        elif user_input == 6:
            clearlists()
            sort()                                                               #linear search
            with open("sorted_data.txt", "r") as vg:
                for line in vg.readlines():
                    vg_line_split = line.split(",")
                    
                    first_name_list.append(vg_line_split[0])
                    last_name_list.append(vg_line_split[1])
                    account_number_list.append(vg_line_split[2])
                    phone_number_list.append(vg_line_split[3])
                    email_list.append(vg_line_split[4])
                    account_type_list.append(vg_line_split[5])
                    status_list.append(vg_line_split[6])
            print_menu()            
            print('------------------------------------------------------')

        elif user_input == 7:
            plot_all_accounts()
        
        elif user_input == 8:
            print('------------------------------------------------------')
            print("\nExiting...")
            print()
            
        else:
            print('Unrecognized Command')
            print('------------------------------------------------------')

except ValueError:
    print("**************ERROR**************\n\tPlease enter an integer")
except RuntimeError:
    print("**************ERROR**************\n\tUnrecognized Command")
except KeyError:
    print('**************ERROR**************\n\tAccount Not Found')