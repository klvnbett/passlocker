#!/usr/bin/env python3.6
from os import system
import random
import string
from user import User
from credentials import Credentials
from time import sleep


def create_user(username,password):
    '''
    Function to create a new contact
    '''
    new_user = User(username, password)
    return new_user

def save_users(user):
    ''' Function to save User # Init method up here    '''
    user.save_user()

def check_existing_users(username, password):
    '''
    Function that check if a contact exists with that username and password and return a Boolean
    '''
    return User.user_exist(username, password)

def find_user(username, password):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return User.login(username, password)

#............... Accounts credentials..........................
def create_credentials(account,password):
    new_credentials = Credentials(account, password)
    return new_credentials

def save_credentials(credentials):
    credentials.save_credential()

def display_credentials():
    return Credentials.display_credentials()

def find_credential(account):
    """
    Finds a Credentials by an account name and returns the credentials that belong to that account
    """
    return Credentials.find_credentials(account)

def del_credentials(credentials):
    # Deletes credentials by the account name
    credentials.delete_credentials()





# ===================================================================
def main():
    print("WELCOME TO PASSLOCKER")
    options = input("Hey there, what's  your name? and welcome to passlocker\n ")
    account_code = input(f"Use the number codes {options}. to make your choice\n 1. Create a new Account\n2. Login")

    if account_code == "1":
        print('-' * 50)
        print("Create your account")
        print("Username : ")    
        user_name = input()
        print("Password : ")
        password = input() 

        save_users(create_user(user_name,password)) # create and save new user.
        print('\n')
        print(f"New account {user_name} created")
        system('clear')

        # login after registration
        login()

    elif account_code == '2':
        system('clear')
        login()


def login():
    print("KINDLY LOGIN")
    print(" Enter your Username : ") 
    search_username = input()
    print("Passsword : ") 
    search_password = input()
    logged_in(search_username, search_password)
    
def logged_in(search_username, search_password):
    if check_existing_users(search_username, search_password):
            search_user = find_user(search_username, search_password)
            system('clear')
            print(f"Logged in as {search_user.username}")
            print('*' * 50)
            
            print("Choose the service you need")
            print("1. Store already existing account credentials ") 
            print("2. Create a new account credentials ")
            print("3. Display my credentials ")
            print("4. Delete my credential ")
            print("5. Logout ")
            account_name = "" #declaring global function
        
            service_choice = input()
            if service_choice=="1":
                print('.' * 50)
                print("Store already existing account credentials")
                print("Enter your Account name")
                account_name = input()
                print("Enter your Account password")
                account_password = input()

                save_credentials(create_credentials(account_name, account_password))
                print('\n')
                print(f"Credentials for {account_name} created successfully")
                sleep(2)
                system('clear')
                logged_in(search_username, search_password)


            elif service_choice=="2":
                print('.' * 50)
                print("Create a NEW account credentials")
                print("Enter your Account name")
                account_name = input()

                print("Do you want a system generated password?")
                print("1. Yes\n2. No")
                choice = input()

                if choice=="1":
                    password = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
                    save_credentials(create_credentials(account_name, password)) 
                    print(f"Your Generated password is {password}")
                    print(f"Credentials for {account_name} created successfully")
                    print("Loading... please wait")
                    sleep(4)
                    system('clear')
                    logged_in(search_username, search_password) 

                elif choice=="2":
                    print(f"Enter {account_name} 's Account password")
                    account_password = input()
                    save_credentials(create_credentials(account_name, account_password))
                    print(f"Credentials for {account_name} created successfully")
                    sleep(2)
                    system('clear')
                    logged_in(search_username, search_password)

                else:
                    print('.' * 50)
                    print("Wrong choice! Try again")
                    logged_in(search_username, search_password)

            elif service_choice=="3":
                show_credentials()
                print("Press x or any key to exit ")
                exit = input()

                counter = 2
               
                if exit == "X" or exit=='x': 
                    for x in reversed(range(counter)):
                        print(f"Redirecting in {x} seconds")
                        sleep(1)      
                else:
                    for x in reversed(range(counter)):
                        print(f"Redirecting in {x} seconds")
                        sleep(1)

                system("clear")
                logged_in(search_username, search_password)

            elif service_choice=="4":
                print('.' * 50)
                if display_credentials():
                    print("*******Your accounts*******")
                    for credentials in display_credentials():
                        print(f"=> {credentials.account}")
                    print("Enter account name to delete")
                    search_account = input()
                    
                    if find_credential(search_account):
                        search_credential = find_credential(search_account)
                        print("_"*50)
                        search_credential.delete_credentials()
                        print('\n')
                        print(f"Your stored credentials for {search_credential.account} account is successfully deleted!!!")
                        sleep(3)
                        logged_in(search_username, search_password)
                        
                    else:
                        print("_"*50)
                        print("That Credential you want to delete does not exist! Please create some")  
                        print("Redirecting... please wait")
                        sleep(3)
                        logged_in(search_username, search_password)              

                else:
                    print("_"*50)
                    print("You dont seem to have any contacts saved yet")
                    print("Loading... please wait")
                    sleep(4)
                    system("clear")
                    logged_in(search_username, search_password)
            
            elif service_choice=="5":
                print("-"*40)
                print("Logging you out ...")
                sleep(2)
                system('clear')
                main()
            else:
                print("Invalid choice! Try again")
                logged_in(search_username, search_password)

    else:
        system('clear')
        print("Wrong credentials or User does not exist !! Try Again")
        print('-' * 50)
        main()
        


def show_credentials():
    if display_credentials():
            print('-' * 50)
            print("Your credentials")
            for credentials in display_credentials():
                    print(f"Account : {credentials.account}    Password : {credentials.password}")
            print('-' * 50)
    else:
            print('-' * 50)
            print("YOU ARE CURRENTLY NOT REGISTERED")
            


if __name__ == '__main__':
    main()
