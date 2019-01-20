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

#######################################################################

#(100,400,"python",10.35)
'''
emp = []
num = int(input("Enter number of element"))
for i in range(0,num):
    ele = input("Enter element")
    if ele.isdigit():
        ele = int(ele)
        emp.append(ele)
    elif "." in ele:
        e = ele.split(".")
        for i in e:
            if i.isdigit():
                ele = float(ele)
                emp.append(ele)
                break
            else :
                emp.append(ele)
    else:
        emp.append(ele)
emp = tuple(emp)
print(emp)'''

#########################################################################

##chose a category
##   1. arith
##   2. logical
##1
##
##chose an operation
##   1. add
##   2. sub
##   3. mul
##   4. div
##

"""
def category():
    '''Chose a category
        1.arith
        2.logical '''
    cat = int(input("Enter category :"))
    if cat == 1:
        print(arith.__doc__)
        arith()
    elif cat == 2:
        logical()
    else:
        print("wrong input")
def arith():
    '''choose operation
        1.ADD
        2.SUB
        3.MUL
        4.DIV '''
    ope = int(input("Enter operation :"))
    num1 = int(input("enter element :"))
    num2 = int(input("enter element :"))

    if ope == 1:
        addnums(num1,num2)
    elif ope == 2:
        subnums(num1,num2)
    elif ope == 3 :
        mulnums(num1,num2)
    elif ope == 4:
        if num2 == 0:
            print("cannot divide by zero")
        else:
            divnums(num1,num2)
def addnums(num1,num2):
    res = num1 + num2
    print(res)
def subnums(num1,num2):
    res = num1 - num2
    print(res)
def mulnums(num1,num2):
    res = num1 * num2
    print(res)
def divnums(num1,num2):
    res = num1/num2
    print(res)

print(category.__doc__)
category()"""

#PythonList------------------------------

#Filter integer and string from a list
'''
str1 = [100,200,"aditya",98,"mukherjee","hello",67,"world"]
num =[]
new_str =[]
for i in str1:
    if type(i) is int:
        num.append(i)
    else:
        new_str.append(i)
print(num)
print(new_str) '''

#List of even number up to num
'''
num = int(input("Enter number"))
op = []
for i in range(1,num+1):
    if (i%2 ==0):
        op.append(i)
print(op) '''

#Adding two list of same length

'''
num_1 = [2,4,67,34]
num_2 = [3,7,5,23]
op =[]

for i in range(0,4):
    x =   num_1[i] + num_2[i]
    op.append(x)
print(op) '''

#Adding two list taking input from user 
'''
num = int(input("Enter number of elements in list : "))
num_1 = []
num_2 = []
op = []
op_1 = []
op_2 = []
for i in range(1,num+1):
    str1 = input("Enter Element of first list : ")
    op.append(str1)
    str2 = input("Enter Element of second list : ")
    op_1.append(str2)
for j in range(0,num):
    sum = int(op[j]) + int(op_1[j])
    op_2.append(sum)
print(op_2) '''

#Extending list
'''
list1=[10,20,30,40,50]
list2=[100,200,300,400]
list1.extend(list2)
print(list1) '''

#Creating single list from heterogeneous list
'''
nums = []
li=[100,[230,400,"python"],["hyd",39],200]
for i in li:
	if type(i) is not list:
		nums.append(i)
	else:
		for j in i:
			nums.append(j)
print(nums) '''

#Square of list 
'''
num = int(input("enter number"))
numlist = []
for i in range(1,num+1):
    a = i*i
    numlist.append(a)
print(numlist) '''


#Square of Even number list

'''
num = int(input("Enter number"))
op = []
for i in range(1,num+1):
    if (i%2 ==0):
        a = i*i
        op.append(a)
print(op) '''


#list comprehensions

'''
num = [ i for i in range(10)]
print(num)'''

'''
num = int(input("enter number"))

num_1 = [i for i in range(1,num+1) if (i%2 == 0)]
print(num_1) '''


'''
num = int(input("enter number"))

num_1 = [i**2 for i in range(1,num+1) ]
print(num_1) '''


'''
num = int(input("enter number"))

num_1 = [i**2 for i in range(1,num+1) if (i%2 == 0)]
print(num_1) '''


#List which gives length of each word given by the user
'''
stmt = input("Enter Statement : ")
op = []
a = stmt.split()
for i in a:
    op.append(len(i))
print(op) '''

'''
stmt = input("Enter Statement : ")
num = [len(i)  for i in stmt.split()]
print(num) '''


#Tuples

'''
nums =(12,45,56,100)
print(nums)
print(type(nums))
print(nums[3])
print(nums[0])
print(nums[0:2])
print(nums[2:]) '''


'''
char = "a","b","java","python"
print(char)
print(type(char))    
print(char)
char[0] = "aaaa" #Error tuples are immutable
print(char) '''


#Converting tuple into list and then doing modification and then changing it to tuples

'''
char = "a","b","java","python"
char = list(char)
char[0] = "aaaaa"
char = tuple(char)
print(char)
print(type(char)) '''


#Dictionary

'''
d ={20:40,"tech":"python"}
print(d)
print(type(d)) '''


#accesssing of elements


#emp = {"name":"aditya","tech":"python","age":100,(1,2,3):"c++"}
#print(emp["name"])
#emp["location"] = "hyd"
#print(emp)

#modifying
#emp["tech"] = "java"
#print(emp)

#Deleting 
#del <dictname>[<key>]
#del <dictname>
#del emp["tech"]
#print(emp)

#del emp
#print(emp)

#print(len(emp))
#print(emp.keys())
#print(emp.values())
#print(emp.items())

#for i in emp.keys():
#    print(i)

#newdict = emp.copy()
#print(newdict)
#emp.clear()
#print(emp)

#update -->extend

#org ={"name":"lync","address":"hyd","est":2016}
#print(org)
#print("----using update----")
#emp.update(org)
#print(emp)
#print(org)

#emp.pop("tech")
#print(emp)
#emp.popitem()
#print(emp)


#numsq ={}
#num = int(input("enter number"))
#for i in range(1,num+1):
#    numsq[i] = i**2
#print(numsq)

#wordslen ={}
#stmt = input("Enter statement :")
#words = stmt.split()
#for i in stmt.split():
#    wordslen[i] = len(i) 
#print(wordslen)

#Convert list into dictionary

#l1 = [1,2,3]
#l2 =["one","two","three"]
#newdict  = {}
#d = {l1[n]: l2[n] for n in range(len(l1))}
#print(d)
#d= {}
#if len(l1) == len(l2):
#    for i in range(len(l1)):
#        d[l1[i]] = l2[i]
#else:
#    print("unequal length")
#print(d)


#z = zip(l1,l2)
#print(z)
#d = dict(z)
#print(d)

#d = dict(zip(l1,l2))
#print(d)


#dictionary comprehension
#d = {i:i**2 for i in range(10) if i%2 == 0}
#print(d)


#stmt = "i love python"
#d = { i:len(i) for i in stmt.split()}
#print(d)


#stmt = "i love python"
#d = { i:len(i) for i in stmt.split() if len(i) > 4 }
#print(d)


#sum, max, any, enumerate 

'''
l1 = [1,3,5,43,23,45,21]
Sum = sum(l1)
average = Sum/len(l1)
print(average)
Max = max(l1)
print(Max)
print(any(l1))
print(len(l1))
l2 = enumerate(l1)
print(l2) '''

#Function returns another function

'''
def first():
   print("hello")
   return 100

def second():
   print("bye")
   return first()
print(second()) '''


# Function return
'''
def first():
    print("hello")
    return 100
def second():
    print("bye")
    return first

print(first)
print(second)

print(first())
print(second())

print(type(first)) #100
print(type(second)) #location of first

print(type(first()))
print(type(second())) '''

#Generate email using lambda function
''' 
email = lambda name,org : name + "@" + org + ".com"
print(email("aditya","company")) '''



############################Recursion in python 

'''
def supersum(num):
    ans = 0
    if len(str(num)) == 1:
        return num
    else:
        for i in str(num):
            ans = ans + int(i)
        if len(str(ans)) > 1 :
            return supersum(ans)
        else:
            return ans
print(supersum(1))
print(supersum(21))
print(supersum(35694)) '''


#Factorial using recursion

'''
num = int(input("Enter number to find Factorial :"))

def rec_fact(n):
	if n == 1:
		return 1
	else:
		return n * rec_fact(n-1)


print(rec_fact(5)) '''



l1 = [1,2,3,4]
l2 = [10,20,30,40]
#op = []
#for i in range(len(l1)):
#    sum_1 = l1[i] + l2[i]
#    op.append(sum_1)
#print(op)

'''
def addlist(l1,l2):
    op =[]
    for i in range(len(l1)):
        op.append(l1[i] + l2[i])
    return op
print(addlist(l1,l2))'''


#Map function

'''
def sq(a):
    return a **2
mo  = map(sq,l1)
print(type(mo))
ans = list(mo)
print(ans) '''


'''
def addnum(a,b):
    return a+b
moo = map(addnum,l1,l2)
ans = list(moo)
print(ans) '''


#print(list(map(lambda a : a**2,l1)))
#print(list(map(lambda a, b:a+b,l1,l2)))


#Filter function


'''
fo = filter(lambda a : a%2 == 0 , l1)
print(fo)
ans = list(fo)
print(ans)'''

'''
stmt = "iam in a python session"
print(list(filter(lambda word : len(word) > 5,stmt.split()))) '''



#Reduce


'''
from functools import reduce
val = reduce(lambda a, b: a+b ,l1)
print(val)

val =  reduce(lambda a,b: a+b , l2)
print(val)

val = reduce(lambda a, b: a*b,l1)
print(val)'''

