import random



class user:

    '''
    class generating new instance of use

    '''
    userslist=[]
    def __init__(self,firstname,lastname,username,password):
        '''
        _init_method that helps us define properties for our objectsself.

        '''
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.password=password
    def save_user(self):
        '''
        save user method saves user info into user userlist
        '''

        user.userslist.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the userslist
        '''
        user.userslist.remove(self)
    @classmethod
    def find_by_number(cls,number):
        '''
        method takes  in a user and returns a user that matches that number
        '''
        for user in cls.userslist:
            if user.password == number:
                return user
    @classmethod
    def user_exist(cls,number):
        for user in cls.userslist:
            if user.username==number:
               return True
               return False


class credentials:
    '''
    class that generates new instances of credentials
    '''
    accounts=[]
    def _init_(self,accountusername,accountname,accountpassword):
        """
        _init_method that helps in defining properties of our project self
        """
        self.accountusername=accountusername
        self.accountname=accountname
        self.accountpassword=accountpassword
    def save_account(self):
        '''
        save account method saves user info into accounts
        '''
        credentials.accounts.append(self)
    def delete_account(self):
        '''
        delete_account method deletes a saved credential from accounts
        '''
        credentials.accounts.remove(self)
    @classmethod
    def find_by_number(cls,number):
        '''
        method that takes in a number and returns a contact that matches that number
        '''
        for account in cls.accounts:
            if account.accountusername == number:
                return account


    
        



