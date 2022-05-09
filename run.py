import string
from random import *
from user import user
from user import credentials

def create_user(firstname, lastname, username, userpassword):
    newuser = user(firstname, lastname, username, userpassword)
    return newuser

def save_user(user):
        user.save_user()
def delete_user(user):
        user.delete_user()

def find_user(number):
        return user.find_by_number(number)

def display_users():
        return user.display_users()

def create_account(accountusername, accountname, accountpassword):
        newaccount = credentials(accountusername, accountname, accountpassword)
        return newaccount
def save_account(user):
        user.save_account()
def delete_account(user):
        user.delete_account()

def find_account(number):
        return credentials.find_by_number(number)

def display_accounts():
        return credentials.display_accounts()
def main():
        while True:
            print("Welcome to password locker write SU or LG to start")
            print("SU -or-LG")
            option = input()
            if option == "SU":
                print("Create Account")
                print("-"*10)
                print("Enter your firstname..")
                firstname = input()
                print("Enter your lastname..")
                lastname = input()
                print("Set your username..")
                username = input()
                print("Set your password..")
                userpassword=input()
                save_user(create_user(firstname,lastname,username,userpassword))
                print("Your account was created successfully.These are your account details")
                print("-"*10)
                print(f"Name:{firstname} {lastname} \nusername:{username} \npassword:{userpassword}")
                print("\nuse login to your account with your details")
                print("\n \n")
                #for user in display_users():
                #    print(f"{user.firstname} {user.lastname}.....{user.username}")
            elif option =="LG":
                print("your username...")
                loginUsername=input()
                print("your password..")
                loginPassword=input()
            if find_user(loginPassword):
                print("\n")
                print("you can create multiple accounts(AC) and also view them(VA)")
                print("-"*60) 
                print("AC -or-VA") 
                choose=input()
                print("\n")
                if choose == "AC":
                    print("Add your credential Account")
                    print('-'*25)
                    accountusername=loginUsername
                    print("\n")
                    print("Generate automatic password(G)or create new password(C)?")
                    decision=input()
                    if decision=="G":
                       characters=string.ascii_letters+string.digits
                       accountpassword="".join(choice(characters)for x in range(randint(6,16)))
                       print(f"password:{accountpassword}")
                    elif decision=="C":
                        print("Enter your password")
                        accountpassword=input()
                    else:
                        print("please put a valid password")
                    save_account(create_account(accountusername,accountname,accountpassword))
                    print("\n")
                    print(f"Username:{accountusername}\nAccount Name:{accountname}\npassword:{accountpassword}")
                elif choose=="VA":
                    if find_account(accountusername):
                        print("Here is the list of your created accounts")
                        print("-"*25)
                        for user in display_accounts():
                           print(f"Account:{user.accountname}\npassword:{user.accountpassword}\n\n")

                    else:
                        print("Invalid credentials!")

                else:
                    print("PLEASE TRY AGAIN")
                    print("\n")
            else:
                print("incorrect info try again!")
                print("\n")
        else:
          print("choose a valid option")
          print("\n")
if __name__=='_main_':
    main()
                        
            
                    
                



                

