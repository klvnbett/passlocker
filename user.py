
class User:
    """
        Class that generates new instance of User.
    """
   
    def __init__(self,username,password):

        self.username = username
        self.password = password
       
    user_list = [] # Empty user list
   
    def save_user(self):
        '''
        This method saves User objects into userlist
        '''
        User.user_list.append(self)

    @classmethod
    def user_exist(cls,username,password):
        '''
        Method that checks if a user exists from the users list.
           
        '''
        for user in cls.user_list:
            if user.username == username and user.password==password:
                return True

        return False


    @classmethod
    def login(cls,username,password):
        '''
        Method that that if the user exists to log in and access the credentials.
        '''
        for user in cls.user_list:
            if user.username == username and user.password==password:
                return user