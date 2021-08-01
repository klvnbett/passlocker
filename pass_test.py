import unittest
class Test_userInput(unittest.TestCase):
    '''
    test class that defines test cases for user behaviours
    '''
def setUp(self):
    """
    this method provide test input to test
    """
    self.user=User("kbett","klvnbett@gmail.com","7890","7890")
def test_init(self):
    """
    method to perfom if correct initialization is met
    """
    self.assertEqual(self.user.userName,"kbett")
    self.assertEqual(self.user.email,"klvnbett@gmail.com")
    self.assertEqual(self.user.password,"7890")
    self.assertEqual(self.user.confirmPassword,"7890")

def tearDown(self):
    '''
    method to clear list after every test
    '''
    User.users =[]
def test_severalUsers(self):
    """
    this will test the saved users
    """
    self.user=User("kbett","klvnbett@gmail.com","7890","7890")
    self.user.saveUser(self.user.password)
    self.assertEqual(len(User.users),1)

def test_display_users(self):
    self.user=User("kbett","klvnbett@gmail.com","7890","7890")
    self.user.saveUser(self.user.password)
    self.assertEqual(len(User.users),1)

def test_delete_users(self):

if __name__=='__main__':
 unittest.main()