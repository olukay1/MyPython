'''
My simple program that create UserRecord file in the working directory.
Thus save user input which is then checked if user was registered else, append 
user input in the UserRecord file.
'''
#Welcome screen
def welcome():
    
    return "W E L C O M E \n" + "----------------------"

print(welcome())
# Prompt for username and password
user_name = (input("Enter your username:  \n"))
user_pwsd = (input("Enter your password:  \n"))


#Function to check if user exist
def status ():    
    user_record = {}
    myfile = open("User_Records.txt", 'r+')
    content = myfile.read() 
    myfile.close()
        
    if  user_name in content and user_pwsd in content:
        print("Record found. Login successful")
        print( "Welcome back ", user_name)
        
    else:
        #Add user to database
        user_record [user_name] = user_pwsd 
        
        print("Account created successfully! ")
        print("Login with your details next time.")
        
    return user_record

# Create text file to store user record i.e database
def check_me ():
    myfile = open("User_Records.txt", 'a+')
    record = status()
    
    if len(record) > 0:
        record = myfile.write(str(record))
    else:
        record =""
    myfile.close()    
    return record
    

check_me()