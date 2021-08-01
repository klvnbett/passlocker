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
    '''