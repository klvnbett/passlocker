import unittest # Importing the unittest module
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user = User("kkbt","7890") 


    def test_init(self):
        self.assertEqual(self.new_user.username,"kkbt")
        self.assertEqual(self.new_user.password,"7890")
    
    def test_save_user(self):
            self.new_user.save_user() # saving the new contact
            self.assertEqual(len(User.user_list),1)

      
    def tearDown(self):
            User.user_list = []

    def test_save_multiple_User(self):
            self.new_user.save_user()
            test_user = User("bettk","king12") 
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
    
    def test_login(self):
        self.new_user.save_user()
        test_user = User("bettk","king12") 
        test_user.save_user()

        auth_user = User.login("bettk","king12")


    # credentials tests
class TestCredentials(unittest.TestCase):

    def setUp(self):
        self.new_credentials = Credentials("TangoEcho","lima12") 


    def test_init(self):
        self.assertEqual(self.new_credentials.account,"TangoEcho")
        self.assertEqual(self.new_credentials.password,"lima12")
    
    def test_save_credentials(self):
            self.new_credentials.save_credential()

    def test_display_all_credentials(self):
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
    
    def test_find_account_by_name(self):
        '''
        test to check if account does exist with the name being used tosearch
        '''
        self.new_credentials.save_credential()
        test_account = Credentials("grego","12345") # new account
        test_account.save_credential()

    def test_delete_credentials(self):
            self.new_credentials.save_credential()
            test_credentials = Credentials("TangoEcho","lima12") 
            test_credentials.save_credential()
            self.new_credentials.delete_credentials()
            self.assertEqual(len(Credentials.credentials_list),1)
 
if __name__ == '__main__':
    unittest.main()