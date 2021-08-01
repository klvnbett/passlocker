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
    '''.git/method to clear list after every test
    '''

if __name__=='__main__':
 unittest.main()