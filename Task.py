# Example of if elif and else (Check if the number is multiple of 3 and 5)
'''
number = input("Enter number :")
if number.isdigit():
    number = int(number)
    if number%3 == 0 and number%5 != 0:
        print("Multiple of 3")
    elif number%5 == 0 and number%3 != 0:
        print("Multiple of 5")
    elif number%5 == 0 and number%3 == 0:
        print("Multiple of 3 and 5")
    else:
        print("Not multiple of 3 and 5")
else:
    print("Enter number only") '''  

# Example if elif and else (convert the time into 24hrs format ) 
'''import sys
time = input("Enter time in hh:mm:ss format :")
if len(time) == 10:
    hh = int(time[0:2])
    mm = int(time[3:5])
    ss = int(time[6:8])
    ff = time[8:10]

    if hh > 12:
        print("Invalid hour input")
        sys.exit()
        
    #if ff.lower() == 'pm':
    if time.endswith('pm'):
        hh = hh + 12
        print("%d:%d:%d"%(hh,mm,ss))
    else:
        hh = hh
        print("%d:%d:%d"%(hh,mm,ss))
else:
    print("Invalid time input from input")    '''

#Class task 1 : Print all even and odd number between 20 and 30 
'''
strt = int(input("Enter start number :"))
end = int(input("Enter end number :"))
for even in range(strt, end):
    if (even%2 == 0):
        print("%d is even number"%(even))
    else:
        print("%d is odd number"%(even)) '''
############################################################

'''num = int(input("Enter number"))
for i in range(1,num):
    print(str(i) * i)'''

###################################################################
# Task 2 (Multiplication of number)
'''
num = int(input("Enter Number :"))
for i in range(1,11):
    print("{} * {} = {}".format(num,i,num*i))'''
#############################################################
'''
a = 1
while a<10:
    print(a,end=" ")
    a += 1 ''' 

'''a = 10
while a > 0:
    print(a)
    a = a-1'''

###############################################   
'''
tech = "python"
for i in tech:
    print(i,end="")'''

############################################

'''alphabet = "abcde"
num = int(input("Enter number : "))
for i in range(1,num+1):
    print(alphabet[i] * i ) '''

##############################################
'''a = [2,4,5,67,9]
print(type(a))'''

############################################

#Nested for loop example
'''
num_list = [1,2,4,5]
alphabet = ['a','b','c','d','r','t']
for i in num_list:
    print(i,end=" ")
    for j in alphabet:
        print(j,end=" ")'''

'''
num = int(input("enter number"))
for i in range(1,num+1):
    print(str(i) * i)'''

#1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

'''
num = int(input("enter number"))
for j in range(1,num+1):
    for i in range(1,j+1):
        print(i,end=" ")
    print("")'''

 #1
# 2 1
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1    

'''
num = int(input("enter number"))
for j in range(1,num+1):
    for i in range(j,0,-1):
        print(i,end=" ")
    print("")'''



#hello
