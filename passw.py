import random
from unittest.main import main
class User:
    '''
    this is a class for adding user 
    '''

    users=[] #empty users

    def __init__(self,userName,email,password,confirmPassword):
        self.email=email
        self.password=password
        self.confirmPassword=confirmPassword

    def createUser(email,password,confirmPassword):
        '''
        an instance that will create a new user
        '''
        newUser =User(email,userName,password,confirmPassword)
        return newUser

    def saveUser(email,userName,password):
        """
        this method will save the user details
        """
        newUser =[email,userName,password]
        User.users.append(newUser)

    def loginMessage():
        """
        this method confirms if succesful in login in
        """

    @classmethod
    #this is a class decorator to display users
    def display_users(self):
        for user in self.users:
            print(user)

    @classmethod
    #class decorator to delete users
    def del_users(self):
        User.users.remove(self)
class Credentials:
    '''
    this is a class fo credentials
    '''

    def __init__(self,userName,password):
        """
        this is an instance to create credentials
        """
        self.userName= userName
        self.password=password

    Credentials=[]

    def createNewCredentials(self,userName,password):
        """
        method to create new credentials
        """
        newCredentials=Credentials(userName,password)
        return newCredentials

    def saveCredentials(self,userName,password):
        """
        method to save new credentials
        """
        Credentials.credentials.append(self)

    def displayCredentials(self):
        for credential in Credentials.credentials:
            print(credential)
    def checkExistance(self,userName):
        """
        method that checks the existance of user data
        """
        if Credentials.credentials:
            for credential in Credentials.credentials:
                if credential.userName==userName:
                    return True
                print("details provided already exist")
            else:
                print("info provided notyet saved")

    def delete_credentials(accountName):
        """
        this will delete user credentials
        """
        for credential in Credentials.credentials:
                if credential.userName==accountName:
                    Credentials.credentials.remove(credential)

def main():
    print("Hi there and welcome")
    while True:
        print("*"*40)
        options= input("Enter your user name")
        
