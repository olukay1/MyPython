import random
import string

def pwdGen():
    al = string.ascii_lowercase +  string.ascii_uppercase + string.digits + string.punctuation
    p=5
    s = 8
    for j in range(p):
        passw = "".join(random.choice(al) for i in range (0, s))
        return passw


my_acc = input("Store password for which account?:  ")

#print (my_acc )
#pwsdkey = {my_acc: pwdGen()}
pwsdkey = dict()
pwsdkey[my_acc] = pwdGen()

#userAcc = pwsdkey.keys()
#userPwd = pwsdkey.values()
print ("the password stored for", my_acc)
print ( " is:  ",  pwsdkey.values())

#
 #r = random(for i in range v())
 