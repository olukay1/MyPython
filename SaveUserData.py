#Rcd = {'UserName' : input("Enter your User name: "), 'pwd' : input("Enter your password: "), 'ID': '20'}

#if Rcd['UserName' ] in ('kay', 'Kay', 'KAY'):
#    print ('You have already registered')
#else:
#    print ('No record found, Try and register')



print ("W E L C O M E \n", "----------------------") #Welcome screen


#Create empty dictionary to store data
user_record = {}


# Prompt for username and password
user_name = input("Enter your username:  \n")
user_pwsd = str(input("Enter your password:  \n"))

print(user_record)


#Function to prompt if user existed
def status ():
    
    
    
    if  user_pwsd in user_record.values() and user_name in user_record.keys():
        
        print("Record found. Login successful")
        print("Welcome back ", user_name)
    else:
        #Add user to database
        user_record [user_name] = user_pwsd        
        print("Account created successfully! ")
        print("Login with your details next time.")
    #print('This is urecord INSIDE function', uRecord)
    return user_record

# Create text file to store user record i.e database
#myfile = open("User_Records.txt", "r")
#user_record = myfile.read()
#user_record = user_record.splitline()
#myfile.close()

#print( user_record1  )

def open_file ():
    # Create text file to store user record i.e database
    myfile = open("User_Records.txt", "a+")
    new_dict = myfile.write(str(status()))
    myfile.close()
    print("This is new_dict for status  ", new_dict)
    h = open ("User_Records.txt", "r")
    new_dict = h.read()
    new_dict = eval(str(new_dict))
    myfile.close()
    #print("This is new_dict after EVAL  ", new_dict)
    return new_dict

open_file()


status()



print('This is urecord outside function', user_record) 

#print('This is urecord outside function', user_record1.splitlines()) 


       
