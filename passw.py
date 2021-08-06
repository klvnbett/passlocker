import random
from unittest.main import main
class User:
    '''
    this is a class for adding user 
    '''
    def __init__(self,email, password, confirmPassword):
        
        self.email = email
        self.password = password
        self.confirmPassword = confirmPassword
        
    users = [] # empty list of users

    def createUser(email, password, confirmPassword):
        """
        This method creates a new user
        """
        newUser = User(email, password, confirmPassword)
        return newUser
        
    def saveUser(email, password):
        """
        This method saves user data
        """
        newUser=[email, password]
        User.users.append(newUser)
    
    def loginMessage():
        """
        This method diplays to user upon successful login
        """
        print("Login successful")
        
    @classmethod
        #Decorator for displaying users
    def displayUsers(self):
        for user in self.users:
            print(user)
        
    
    @classmethod
    #decorator for deleting users
    def deleteUsers(self):
        User.users.remove(self) 
        
        

class Credentials:
    def __init__(self, username, password):
        """
        This is a credentials constructor 
        """
        self.username = username
        self.password = password

    credentials = []
    
    def createNewCredentials(self, username, password):
        """
        This method creates new credentials
        """
        newCredentials = Credentials(username, password)
        return newCredentials
    
    def save_credentials(self, username, password):
        """
        This methods saves credentials
        """
        Credentials.credentials.append(self)
        
    def display_credentials(self):
        for credential in Credentials.credentials:
            print(credential)   
    
    def check_Ifexist(self, email):
        """
        This is a method to check if data is already existing
        """
        if Credentials.credentials:
            for credential in Credentials.credentials:
                if credential.email == email:
                    return True
            print("Details provided not available")
        else:
            print("kindly subscribe")
    
    def deleteCredential(accountName):
        """
        This method will delete user credentials
        """
        for credential in Credentials.credentials:
            if credential.username == accountName:
                Credentials.credentials.remove(credential)
            
def main():
   while True:    
        print("*"*50)
        login_options = input(f"Goodday. Kindly select option using the following short codes:\n cc - Create account.\n lg -Login\n ex - Exit\n")
        print("*"*50)
        if login_options == 'cc':
            username = input("Enter username / email address: \n")
            
            passwordoption = input(
                "Choose password option: \n 1. Enter password\n2. Use autogenerated password\n")
            
            if passwordoption == "1":                
                password = input("Enter password: \n")
                
                confirmPassword = input("Confirm password: \n")
                
                if password == confirmPassword:
                    print("Welcome to password and credentials locker. Login")
                    User.createUser(username,password,confirmPassword)
                    User.saveUser(username, password)
                    print(f"You have successfully  Subscribed with {username} as username")
                                                   
                                    
            elif passwordoption == "2":
                password = random.randint(10000, 90000)
                User.saveUser(username, password)
                
            print(f"Account created successfully with user {username}.\n")
            print("Password is ")
            print(password)
                
         
        elif login_options == 'lg':
            print("Welcome to password locker. Login\n")
            print("Enter your username: \n")
            login_username = input()
            print("\n")
            
            print("Enter your password: \n")
            login_password = input()
            for credential in User.users:
                if credential[0] == login_username and credential[1] == int(login_password):
                    prompt_selection = input("Kindly select the option you would like to do using number:\n 1. Store already existing account credentials.\n 2. Create new account credentials.\n 3. View account credentials and passwords. \n 4. Delete account details.\n 5. Exit")
                                
                    if prompt_selection == "1":
                        for user in User.users:
                            Credentials.save_credentials(username, password)
                        print(f"Your credentials {user} have been save successfully.")
                    
                    elif prompt_selection == "2":
                        newAccount = input("Enter your username: \n")
                        
                        newPassword = input("Enter your password: \n")
                        Credentials.createNewCredentials(newAccount, newPassword)
                        Credentials.save_credentials(newAccount, newPassword)
                        break
                    
                    elif prompt_selection == "3":
                        Credentials.display_credentials()
                    
                    elif prompt_selection == "4":
                        accountName = input("Enter username of the credential to delete: \n")
                        Credentials.deleteCredential(accountName)
                        print(f"Credential with username {accountName} deleted successfully")
                        
                    elif prompt_selection == "5":
                        print("Exiting application")
                        break
                    
                    else:
                        print("Invalid selection")
                else:
                    print("Invalid username or password")
                    break
        elif login_options == "ex":
            print("Bye for now. Do have a nice day see you soon")
            break
        
if __name__ == '__main__':
    main()
