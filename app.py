import sys
from dbhelper import DBhelper



class Flipkart:
    def __init__(self):
        #connect to database
        self.db = DBhelper()
        self.menu()
        
    def menu(self):
        user_input = input("""
        1. Enter 1 to register
        2. Enter 2 to login
        3. Anything else to leave
        """)
        
        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(1000)
            
    def register(self):
        name = input("Enter a name ")
        email = input("Enter a email ")
        password = input("Enter a password ")
        
        response = self.db.register(name, email, password)
        
        if response:
            print("Registration sucessful")
        else:
            print("Registration Failed ")
        self.menu()
    
    def login(self):
        email = input("Enter email ")
        password = input("Enter password ")
        
        self.db.search(email, password)
        self.menu()
        
obj = Flipkart()