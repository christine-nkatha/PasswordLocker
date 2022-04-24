import unittest
from user import user


class testuser(unittest.TestCase):

    '''

    Test class that defines test cases for the user class behaviour.
    Args:
       unittest.TestCase:TestCase class that helps in creating test cases
    '''
def setup(self):
    '''
    set up method to run before each test case
    '''
    self.new_user=user("tina","mburugu","1234") #create contact object
def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.user_name,"tina")

    self.assertEqual(self.new_user.password,"1234")
def test_save_user(self):
    '''
    test_save_user case to test if the user object is saved into the user list
    
    ''' 
    self.new_user.save_user() #saving the new contact
    self.assertEqual(len(user.user_list),1)
def test_delete_user(self):
    self.new_contact.save_contact()
    test_user=user("Test","user","0743111325","test@user.com") #new contact
    test_user.save_user()

    self.new_user.delete_user() #deleting a contact object
    self.assertEqual(len(user.user_list),1)
if __name__ =="_main_":
  unittest.main()
