# Query user input
myDigit = input('Enter your Phone numbeer here: ')

#Get spatial interval from user (e.g 123-321; 01-32-23 etc)
intv = int(input("Please indicate spatial interval (i.e in 3s, 2s...): "))

myDigit1 = myDigit.replace(' ', '') #To remove whitespace
mee =  (myDigit1[i:i+intv] for  i in range(0, len(myDigit1),intv))
#word = '-'.join(myDigit [i:i+3])

word1 = 'x'.join(mee)
print(word1)
   
    

#print(lem)


















#for i in list[myDigit]:
    #count +=  i
    #if len(i)%3 == 0:
      #  j = '-'.join(i)
    #print(count)
   # print(j)
#print(j)

#print(newNum)