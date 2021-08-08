class Credentials:
    # Class that generates new instances of credentials.
   
    def __init__(self,account,password):

        self.account = account
        self.password = password
       
    credentials_list = [] # Empty credentials list
   
    def save_credential(self):
        # save_user method saves credentials objects into user_list
        Credentials.credentials_list.append(self)

    @classmethod
    def display_credentials(cls):
        """
        method that displays a list of user credentials.
        """
        return cls.credentials_list

    @classmethod
    def find_credentials(cls, account):
        """
        This Method that takes in a account name and returns a credential that matches that account name.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    def delete_credentials(self):
        #function to delete users saved credentials based on its name
        Credentials.credentials_list.remove(self)