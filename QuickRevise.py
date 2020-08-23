# numbers
##arithmetic --> numbers
##comparision  --> numbers
##logical  --> numbers
##bitwise --> numbers
##
##membership --> all except numbers 
##identity  --> all except numbers
##
##arithmetic ---> 7 operators --> values 
##adding -> +
##subtr -> -
##mult -> *
##div -> /
##floor div -> //
##remainder -> %
##exponent -> ** 

##comparision --> 6 operators --> True / False
##equals --> ==
##not eqauls --> !=
##gthan --> >
##lthan -> <
##gthan + equals -> >=
##lthan + equals -> <=

##logical --> 3 operators --> True / False / values
##and
##a b res  t --1  f -- 0 
##t t  t   11 1
##t f  f   10 0
##f t  f   01 0 
##f f  f   00 0 
##or
##a b res
##t t  t
##t f  t
##f t  t
##f f  f
##not --> 1's complement 
##input output
##  t      f
##  f      t

##bitwise --> 5 operators --> values
##
##& --> bitwise and
##| --> bitwise or
##~ --> bitwise not
##>> --> right shift
##<< --> left shift

##number --> bits(4) 
##        128     64       32       16       8        4     2     1
##10 -->  0        0        0        0        1        0     1    0
##20 -->  0        0        0        1        0        1     0    0
##10 & 20 0        0         0       0        0        0     0   0 --> 0
##10|20   0         0        0       1         1       1     1   0 --> 30 
##
##~(10) --> 11110101 --> >200
##~ --> 2's complement 
##~(x) --> -(x+1)
##
##10 >> 2 --> 00000010
##10 >> 3 --> 00000001

#strings

##java --> char , string
##char -> single character
##string --> combi of chars
##
##python
##strings --> single character ,combi of chars

##<class str>
##features
##--------
##indexed
##sliced
##concatenated
##IMMUTABLE
##    no change
##    no delete
##    no add
##functions on strings 


##syntax
##-----
##<nameofstring> = " <value> "
##<nameofstring> = ' <value> '

n ="1@HJ&*%BK87%mN*("


tech = "digitallync"

##d   i   g  i  t  a  l  l  y  n  c
##0   1   2  3  4  5  6  7  8  9  10 --> forward indices
##-11-10 -9 -8 -7 -6 -5 -4 -3  -2 -1 ---> reverse indices
##
##indexing --> single char from string 
##
##<strname>[<indexvalue>]
##tech[4] --> t
##tech[10] --> c

##slicing --> substring , string
##startpoint , endpoint
##
##<strname>[<startindex> : <endindex>]
##tech[3:7] --> 3 4 5 6 --> ital
##tech[3:10] --> 3 4 5 6 7 8 9 --> itallyn
##
##<strname>[ : <endindex>] ---> <startindex> = 0 
##<strname>[<startindex> : ] --> <endindex> = end of string 
##
##
##tech[3:10] --> 3 4 5 6 7 8 9
##
##<strname>[<startindex> : <endindex> :<stepvalue>]
##tech[3:10:2] --> 3  5  7  9  --> ialn
##
##string is acccessed reverse 
##<strname>[<startindex> : <endindex> :<stepvalue>]
##stepvalue --> negative
##startindex > endindex
##reverse a string
##<strname>[::-1]
##
##
##IMMUTABLE
##
##modify XXXX
##tech[0] --> d
##tech[0] = "z"
##
##delete XXXX
##del tech[2]
##
##adding XXXX
##tech[11] = "w"
##
##del <strname> --> entire string deletion 
##del tech 
##
##
##
##special  / escape chars
##-----------------------
##special --> \n (newline) \t ( tab space ) 
##escape  --> \ , %
##
##dia = "i'am in a class"
##dia = 'i\'am in a class'
##
##multi line strings --> XXX \n XXX
##<strname> = ''' line1
##line2
##line3
##line4
##'''
##
##
##book = '''hfhrfgh
##fgbkjbgj
##rhjjkrbh
##jgnbjtnbh
##rlegbhljenbhyg '''


##raw strings
##-----------

##syspath = r"c\programs\new\tech\python\code"
##print(syspath)

##concatenation
##-------------
##joining data if allowed

##str1  + str2 ---> "+"

##name = "Mukherjee"
##tech = " python"
##print(name + tech)
##print(name)
##print(tech)

##str int ---> "," ---> print

name = "Mukherjee"  # str ---> %s 
marks = 70 # int  ---> %d

##print(name , marks)

##
##string literals
##---------------
##static storage

##print("Mukherjee has secured 70 marks ")

##print("%s has secured %d %% marks " %(name , marks ))



##type casting
##-------------
##int --> str
##int --> float
##
##
##str --> int (conditional)
##float --> int ( not recomonded )


##number to string              --> str() , repr()
##string to number -            -> int()
##number to decimal number(.) --> float()


##a = 100
##print(a)
##print(type(a)) # number
##print("after changing")
##
####a = str(a)
####print(a)
####print(type(a)) # string
##
##a = repr(a)
##print(a)
##print(type(a))


##name = "Mukherjee"
##marks = 70
##stmt = name + str(marks)
##print(stmt)


##comments
##--------
##non exec line

# --> single line
'''  --> multi line '''

#input vs output
#---------------
#print() --> function --> 3 version
#print --> command --> 2 version

##print(10 , end="")
##print(20)


##input()  --> function in 3 version
##raw_input() , input() ---> functions in 2 version 

##<varname> = input(<statement>)

##a = input("enter any input value ")
##print(a)
##print(type(a))

##string functions
##----------------
##-> case based
##-> checking
##-> operational
##
##-> parameterised --> (<something>)
##-> attribute fetching --> . 

stmt = "Mukherjee is in Python class"
##-> case based
##   lower()  , upper() , capitalize() , title() , swapcase()
##print(stmt.lower())
##print(stmt.upper())
##print(stmt.capitalize())
##print(stmt.title())
##print(stmt.swapcase())

##-> checking
##in , not in  --> true / false 

##print("Mukherjee" in stmt)
##print("Mukherjee" not in stmt)
##print("Mukherjee".lower() in stmt)
##print("z" not in stmt)


##is ,is not --> true / false --> ==
##stmt = stmt.lower()
##print(stmt)
##newstmt = "Mukherjee is in Python class"
##newstmt = newstmt.lower()
##print(newstmt)
##print("Mukherjee is in Python class" is stmt)
##print("Mukherjee is in Python class" is not stmt)

##-> operational (they do not change string)
##
##len(<strname>) --> count of chars in strings
##<strname>.count(<char / substring>) --> frequency of chars
##<strname>.index(<char/ss>) --> index of first occurence of char
##<strname>.find(<char/ss>) --> index of first occurence of char
##<strname>.replace(<old> , <new>) --> replaces old chars with new
##<strname>.split() --> slipts string into words
##<delimiter>.join(<collection>) --> makes a string from words
##<strname>.strip() ---> removes whitespaces from string
##<strname>.lstrip() ---> removes whitespaces from left of string
##<strname>.rstrip() ---> removes whitespaces from right of string
##<strname>.zfill(<number>) ---> fills string with zeros 

dia = "in india i tech python in class"
##print(len(dia))
##print(dia.count("i"))
##print(dia.count("in"))
##print(dia.count("class"))
##print(dia.count("in india i tech python in class"))
##print(dia.count("th"))

##print(dia.index("e"))
##print(dia.index("tech"))
##print(dia.index("i" , 15))
##print(dia.index("java")) # error not available

##print(dia.find("e"))
##print(dia.find("tech"))
##print(dia.find("i" , 15))
##print(dia.find("java")) # -1

##print(dia.replace("in" , "out" , 1))
##print(dia.replace("in" , "out" , 2))
##print(dia.replace("in" , "out" ))

##print(dia.split())
##words = dia.split()
##print(words)
##print(dia.split("tech"))
##print("Mukherjee-30-python-hyd".split("-"))

##print("-".join(words))


##dia = "    in india i tech python in class     "
##print(dia)
##print(dia.strip())
##print(dia.strip(" i"))
##print(dia.strip(" in"))
##print(dia.strip("s "))

##print(dia.lstrip())
##print(dia.rstrip())


##a = "Mukherjee"
##print(a.zfill(5))
##
##b = 125
##print(str(b).zfill(7))


##ASCII ==> numbers
##
##ascii --> character ---> chr()
##character ---> ascii --> ord()

##print(ord("a"))
##print(ord("A"))
##print(ord(","))
##
##print(chr(110))
##print(chr(70))
##print(chr(120))

##conditinoal statements
##----------------------
##-> make descision
##-> on condition
##-> execute statement 
##
##-> condition --> T/F
##-> statement
##
##if  --> 1 statement 
##if else --> 2 statements
##if elif else -> 3 statements
##if elif elif elif . . . . else -> n statements
##
##
##syntax
##------
##
##if <condition> :
##   <statement(s)>
##
##-----------------------------------------
##if <condition> :
##   <statement1(s)>
##else:
##   <statement2(s)>  
##-------------------------------------------
##if <condition1> :
##   <statement1(s)>
##elif <condition2>:
##   <statement2(s)>  
##elif <condition3>:
##   <statement3(s)>  
##elif <condition4>:
##   <statement4(s)>  
##else:
##   <statements5>
##
##-> exits when true 
##
##
##nested conditional stmts
##-------------------------
##if <cond1>:
##   if <cond2>:
##      <statement>
##   else:
##      <statement>
##else:
##   <statement>
##

##a = 100
##if a>5: # condition
##   print("a more than 5 ")
####   pass # empty statements 
##else:
##   print("a less than 5 ")


##a = 3
##if a >5: # false 
##   print("a greater than 5")
##elif a==2: # false 
##   print("a equals 2 ")
##elif a==3: #true 
##   print("a equals 3 ")

##a = 3
##if a <5: # true 
##   print("a less than 5")
##elif a==2:  
##   print("a equals 2 ")
##elif a==3:  
##   print("a equals 3 ")
##else:
##   print("nothing")

##odd even classifier

##isdigit --> t for numbers
##        --> f for all except numbers 

# only nuumber inputs 
##num = int(input("enter a number : "))
##if num%2 == 0 :
##   print(str(num) + " is an even number")
##else:
##   print(str(num) + " is an odd number")
   
##num = input("enter a number : ") # taking input 
##if num.isdigit(): # check number 
##   num = int(num) # type casting to num
##   if num%2 == 0 :
##      print(str(num) + " is an even number")
##   else:
##      print(str(num) + " is an odd number")
##else:# for str 
##   print("enter only numbers")
 

##"08:12:30AM" --> input 
##"08:12:30" --> output
##
##"08:12:30PM" --> input 
##"20:12:30" --> output

##.startswith(<char>)
##.endswith(<char>)

##time = input("enter time in HH:MM:SSFF style")
##if len(time) == 10:
##   hh = int(time[0:2]) # 08
##   mm = int(time[3:5]) # 12 
##   ss = int(time[6:8]) # 30
####   ff = time[8:10]
##
####   if ff == "pm":
##   if time.endswith("pm"):
##      hh = hh + 12
##      print("%d:%d:%d" %(hh,mm,ss))
##   else:
##      hh = hh
##      print("%d:%d:%d" %(hh,mm,ss))
##else:
##   print("time in unrecognised format")
##
##num = input("enter a number")
##if num.isdigit():
##   num = int(num)
##   if num%3 == 0 and num%5 != 0 :
##      print("multiple of 3 ")
##   elif num%5 == 0 and num%3 != 0:
##      print("multiple of 5")
##   elif num%3 == 0 and num%5== 0:
##      print("multiple of 3 and 5")
##   else:
##      print("nothing")
##else:
##   print("enter only numbers")
##
##
##"iam in in a python class"
##python - 12
##
##"python is an easy language"
##python - 0
##
##"python is python"
##python - 0
##occurence 2 times
##
##"java is tough"
##no python in stmt


##stmt = input("enter your dialogue")
##stmt = stmt.lower() # converting to lower 
##if "python" in stmt:
##   index_value = stmt.index("python")
##   count_value = stmt.count("python")
##
##   print("python  - " + str(index_value))
##   print("occurences  - " + str(count_value))
##else:
##   print("no python in stmt")
##   

##looping structures
##-------------------

##syntax:
##-------
##
##for <dummy> in range():
##   <statements using dummy>
##   
##for <dummy> in range():
##   pass
##
##for i in range(10): # i = 0 , i<10 , i + 1 
##   print(i)

##for i in range(3,20): # i = 3 , i<20 , i + 1 
##   print(i)

##for i in range(3,20,4): # i = 3 , i<20 , i + 4 
##   print(i)

##for i in range(30,20,-1): # i = 30 , i>20 , i - 1 
##   print(i)

##for i in range(30,20,-3): # i = 30 , i>20 , i - 3 
##   print(i)

##st = int(input("enter start point"))
##en = int(input("enter end point"))
##step = int(input("enter step point"))
##
##for i in range(st,en,step):
##   print(i)

##for i in range(10):
##   pass


##patterns
##--------
##star , number , string

##*
##**
##***
##****

##print("*" * 1)
##print("*" * 2)
##print("*" * 3)
##print("*" * 4)

##for i in range(1,5):
##   print("*" * i)

##n --> 5 
##1
##22
##333
##4444
##55555
##
##
##n --> 4
##1
##22
##333
##4444

##n = int(input("enter a number"))
##for i in range(1,n+1):
##   print(str(i) * i)
##while True:
##   aplhabets = "abcdefgh"
##   n = int(input("enter a number"))
##   for i in range(0,n):
##      print(aplhabets[i]* (i+1))

##ascii --> ord() chr()

##while
##-----
##init
##condition
##statement
##inc/dec
##--> finite
##--> infinite


##a = 1 # init
##while a<=10: # condition
##   print(a  , end =" ") # statement
##   a = a+1 # a+=1
   
##a = 10 # init
##while a>0:
##   print(a)
##   a = a-1
##
##a =10
##while a>=10:
##   print(a)
##   a +=1


##strings --> for
##---------------
##string --> collections --> iterated

##tech = "python"
##for i in range(0,len(tech)):
##   print(tech[i])

##for char in tech:
##   print(char) # p . . . .  .n
##   

##control statements
##------------------
##pass
##    -> un implemented ( ifelse , for , function)    
##break
##   -> loops --> exit loop at a condition
##continue
##   -> loops --> exit and returns to loop at condition
##   


##composite / prime 
##n --> 12
##12 is composite with 6 factors
##1
##2
##3
##4
##6
##12

##n --> 12
##12%1 == 0
##12%2 == 0
##12%3 == 0
##
##.
##.
##.
##12%12 == 0
##i --> range(1,n)
##n%i
##
##n =  int(input("enter a number"))
##count = 0 
##for i in range(1,n+1):
##   if n%i == 0 :
##      print(str(i) + " is a factor")
##      count +=1
##if count >2:
##   print(str(n) + " is a composite number with " +str(count) +" factors")
##else:
##   print("prime number")

##1
##12
##123
##1234
##12345

##for i in range(1,2):
##   print(i)
##for i in range(1,3):
##   print(i)
##for i in range(1,4):
##   print(i)
##for i in range(1,5):
##   print(i)
##for i in range(1,6):
##   print(i)
##
##
##for j in range(1,n+1):
##   for i in range(1,j+1):
##      print(i , end = "")
##   print()
##
##a
##ab
##abc
##abcd

##collections
##-----------
##heterogeneus 
##stack
##i s c n
##
##
##lists
##-----
##-> mutable collections
##-> <class list>
##
##
##syntax
##-------
##<listname>  = [<ele1> , <ele2> , <ele3>]

##nums = [1,4,56,9,5,2]
##print(nums)
##print(type(nums))


##<listname>[<index>]

##print(nums[4])
##print(nums[-1])

##<listname>[<sindex> : <eindex>]

##print(nums[0:3])

het = [1, "python" , "Mukherjee" , 67 , [10,"hyd" , "bom"]]
##print(het[3])
##print(het[4])
##print(het[4][1])

##modifying / deleting --> index 
##--------------------

##<listname>[<index>] = <newvalue>
##print(het)
##het[3] = 100
##print(het)

##del <listname>[<index>]
##del het[0]
##print(het)

##del <listname>

##del het
##print(het)

##het[0:3] = "java" , "java" , 1000
##print(het)

##del het[3:5]
##print(het)

##functions
##---------

##len() --> no of elements
##<listname>.index(<ele>) --> index of first occurance ele
##<listname>.append(<ele>) --> add element to list at the end
##<listname>.insert(<index> , <ele>) --> add element to list at the index
##<listname>.pop() --> removes element from list from end
##<listname>.remove(<ele>) --> removes given element from list
##<listname>.sort() --> inc sort data (if single data type) --> homogeneous
##<listname>.sort(reverse = "True") --> dec sort data (if single data type) --> homogeneous
##<listname>.count(<ele>) --> frequency of element in list
##<listname>.copy() --> copies elements
##<listname>.clear() --> clear elements

##<list2>
##<list1>
##
##<list3> = <list1> + <list2>
##
##<list1>.extend(<list2>) --> add elemets of list2 to list1 

mixed = [10,40,"python" , "hyd" , 400 , [1,3,"tech" , "lync"] , 600]
##print(mixed)
##mixed.append(1000)
##print(mixed)
##mixed.insert(4,"java")
##print(mixed)
##mixed.pop()
##print(mixed)
##mixed.remove(400)
##print(mixed)
##
##print(mixed.index("python"))
##print(mixed.count("python"))
####mixed.sort() # error
##
##list1 = [10,20,30,40]
##list2 = [100,200,300,400]
##
####print(list1 + list2)
##list1.extend(list2)
##print(list1)
##print(list2)


##for ele in mixed:
##   print(ele)

##l1 = [1,2,3,6,4,3,1,3,345,7,94,4,212,3,5,7,8,3]
##uni = []
##rep = []
##
##for i in l1:
##   if i not in uni :
##      uni.append(i)
##   else:
##      rep.append(i)
##print(uni)
##print(rep)

##l1 = [100 , 300 , "python" , "hyd" , 39]
##nums = [] # 100 300 39
##strs = [] # "python" , "hyd"
##
##for i in l1:
##   if type(i) == int:
##      nums.append(i)
##   else:
##      strs.append(i)
##print(nums)
##print(strs)


##l1 = [100 , [300 , "python" ], ["hyd" , 39] , 190 ]
##op= [] # 100 , 300 , "python" , "hyd" , 39 , 190 
##for i in l1:
##   if type(i) is not list:
##      op.append(i)
##   else:
##      for j in i:
##         op.append(j)
##print(op)

##enter your list size
##n --> 4
##enter your element
##10
##enter your element
##400
##enter your element
##98
##enter your element
##3786
##
##[10,400,98,3786]


##n = int(input("enter your list size"))
##num = []
##for i in range(1,n+1):
##   ele = input("enter element")
##   num.append(ele)
##print(num)


##10
##l1 ---> 0 1 2 3 . . .  10
##
##30
##l2 --> 2 4 6 8 10 .... 30
##
##l1 --> 1 2 3
##l2 --> 7 8 9
##l3 --> 8 10 11
##
##num  = int(input("enter a number"))
##numslist = []
##for i in range(0,num+1):
##   numslist.append(i)
##print(numslist)



##num  = int(input("enter a number"))
##evennumslist = []
##for i in range(0,num+1):
##   if i % 2 == 0 :
##      evennumslist.append(i)
##print(evennumslist)



##num  = int(input("enter a number"))
##sqnumslist = []
##for i in range(0,num+1):
##   sqnumslist.append(i**2)
##print(sqnumslist)

##num  = int(input("enter a number"))
##evensqnumslist = []
##for i in range(0,num+1):
##   if i % 2 == 0 :
##      evensqnumslist.append(i**2)
##print(evensqnumslist)


##list comprehensions
##-------------------
##nums = [i   for i in range(10)]

##stmt = input("enter a stmt")
##words = stmt.split()
##lenwords = []
##for i in words:
##   lenwords.append(len(i))
##print(lenwords)
##
##
##syntaxes
##--------
##<listname> = [<dummyvar> <iteration/loop>]  # nums list
##
##<listname> = [<dummyvar> <iteration/loop>  <condition>] # even nums list
##
##<listname> = [<dummyvar + operation> <iteration/loop>] # squares list
##
##<listname> = [<dummyvar + operation> <iteration/loop> <condition>] # even squares list

##stmt = input("enter a stmt")
##lenwords = [  len(i)   for i in stmt.split()]
##print(lenwords)

##tuples
##------
##-> IMMUTABLE
##-> order 1XN
##-> infinite length
##-> default collection datatype
##-> <class tuple>
##-> stack arch

##syntax
##------

##<tuplename> = (<ele1> , <ele2> , <ele3>)
##nums =(91,2,3,4,5,56)
##print(nums)
##print(type(nums))

##<tuplename>[<index>]
##print(nums[3])
##print(nums[0])
##print(nums[5])

##<tuplename>[<sindex> : <eindex>]
##print(nums[3:5])
##print(nums[0:3])
##print(nums[:4])

##char = "a" , "b" , "python" , "java"
##print(char)
##print(type(char))

##print(char[0])
##char[0] = "aaaa"
##print(char)

##del char[0]

##del char
##print(char)


##tuple --> list
##modify
##list --> tuple 

##char = list(char) 
##char[0] = "aaAA"
##char = tuple(char)
##print(char)
##print(type(char))

##enter length
##4
##enter a element
##100
##enter a element
##400
##enter a element
##python
##enter a element
##10.34
##
##(100 , 400 , "python" , 10.34)

##emp = []
##l = int(input("enter length"))
##for i in range(0,l):
##   ele = input("enter an element")
##   if ele.isdigit():
##      ele = int(ele)
##      emp.append(ele)
##   elif "." in ele:
##      e = ele.split(".")
##      for i in e:
##         if i.isdigit():
##            ele = float(ele)
##            emp.append(ele)
##            break
##         else:
##            emp.append(ele)
##            
##   else:
##      emp.append(ele)
##emp = tuple(emp)
##print(emp)


##dictionaries
##------------
##
##emp form --> fname lname peradd preadd mob1 mob2
##
##e1 --> Mukherjee mj hyd hyd 9 8
##e2 --> ravi v     bom  8 9
##e3 --> hari k     vjy  7 
##
##e1[2] --> hyd
##e2[2] --> bom
##e3[2] --> vjy
##
##
##indices are predefined --> 0 1 2 3 . . . .
##
##custom indices --> dictionaries 
##
##
##syntax
##------
##
##<dictname> = {<k1>:<v1> , <k2>:<v2>}


##d = {20:40 , "tech":"python"}
##print(d)
##print(type(d))
                 
##accessing of elements
##---------------------
emp = {"name" :"Mukherjee" , "tech" : "python" , "age" : 100 }
print(emp)
##<dictname>[<key>]
##print(emp["name"])
##print(emp["tech"])

##modifyng
##--------
##<dictname>[<key>] = <newvalue>
c = "java","c++","hello"
emp["tech"] = list(c)
print(emp)
##emp["location"] = "hyd"
##print(emp)       


##emp = {"name" :"Mukherjee" , (1,2,3) : "python" , "age" : 100 }  # valid
##emp = {"name" :"Mukherjee" , [1,2,3] : "python" , "age" : 100 }  # invalid

##deleting
##--------
##del <dictname>[<key>]
##del <dictname>
##[] -->accessors

##del emp["tech"]
##print(emp)
##del emp
##print(emp)


##functions
##---------
##len()
##.keys() --> list of keys
##.values() --> list of values
##.items() --> list of tuples of items
##copy() --> copying all elements
##clear() --> making empty dict
##update()  --> concat of two dicts
##pop(<key>) --> removes the item
##popitem() --> removes arbitary item


print(len(emp))
print(emp.keys())
print(emp.values())
print(emp.items())
for i in emp.keys(): # iterkeys()
   print(i)

##newdict = emp.copy()
##print(newdict)
##emp.clear()
##print(emp)

##update --> extend 
org = {"nameoforg" :"lync" , "address" : "hyd" , "estd" :2016}
print(org)
##print("-------using update------")

#<dictname1>.update(<dictname2>)
emp.update(org)
print(emp) # 6
print(org) # 3

##emp.pop("tech")
##print(emp)
##emp.popitem()
##print(emp)
##emp.popitem()
##print(emp)

##numsq = {}
##n --> 10 
##{1:1 , 2:4 ,3:9 . .. . 10:100}
##n = int(input("eneter a number"))
##for i in range(1,n+1):
##   numsq[i] = i**2
##print(numsq)


##enter a stmt
##i love python
##
##{"i" : 1 , "love":4 , "python":6 }
##
##stmt = input("enter a statement")
##wordslen ={}
##for i in stmt.split():
##   wordslen[i] = len(i)
##print(wordslen)
##
##l1 = [1,2,3]
##l2 = ["one" , "two" , "three"]
##{1:"one" , 2:"two" , 3:"three"}
##d = {}
##if len(l1) == len(l2):
##   for i in range(len(l1)):
##      d[l1[i]] = l2[i]
##else:
##   print("unequal lengths of lists")
##print(d)

##zip() --> lists , tuples --> zip object

##
##l1 = [1,2,3,4]
##l2 = ["one" , "two" , "three" , "four" , "five"]

##z = zip(l1,l2)
##print(z)
##d = dict(z)
##print(d)

##d = dict(zip(l1,l2))
##print(d)


##spoint --> 10
##epoint --> 20
##10 , 12 , 14 , 15 , 16 , 18 , 20
##{10:[1,2,5,10] , 12:[1,2,3,4,6,12] . .. . 20:[1,2,4,5,10,20]}
n = int(input("enter number"))
n2 = int(input("enter number"))
d1= {}
l1 =[]
for i in range(n,n2+1):
   if i%2 == 0:
            
print(d1)

##d = {i:i**2 for i in range(10)}
##print(d)
##
##d = {i:i**2 for i in range(30) if i %2 ==0}
##print(d)


stmt = "i love python"
##{"i" :1 , "love" : 4 , "python" :6}

##d = { word:len(word) for word in stmt.split() }
##print(d)
##
##stmt = "i love python"
##{ "python" :6}
##d = { word:len(word) for word in stmt.split() if len(word)>4}
##print(d)


##sets
##----
##<setname> = {<ele1> , <ele2> , <ele3>}
##nums = {1,3,4,5,6,7}
##print(nums)
##print(type(nums))

##empset = {} # dict not a set XXXX
##print(empset)
##print(type(empset))

##empset = set(())
##print(empset)
##print(type(empset))
##
##nums = set((1,3,4,5,6,7))
##print(nums)
##print(type(nums))


##rep = {1,2,3,4,2,5,7,6,4,121,1,6}
##print(rep)
##print(rep[3])

##for i in rep:
##   print(i)
##
##add()
##remove()
##discard()
##copy()
##clear()
##rep.add(300)
##rep.add(330)
##rep.add(230)
##print(rep)

##rep.remove(1)
##rep.remove(230)
##rep.remove(6)
##rep.remove(110)
##print(rep)

##rep.discard(1)
##rep.discard(230)
##rep.discard(6)
##rep.discard(110)
##print(rep)

s1 = {10,20,30,40}
s2 = {20,50,60,70}
s3 = {10}
s4 = {100}


##print(s1.union(s2))
##print(s1.intersection(s2))
##print(s1.difference(s2))
##print(s2.difference(s1))
##print(s2.isdisjoint(s1))
##print(s1.isdisjoint(s4))

##print(s2.issuperset(s1))
##print(s1.issuperset(s3))
##print(s2.issubset(s1))
##print(s1.issubset(s3))

##print(s1 | s2)
##print(s1 & s2)
##print(s1 - s2)
##print(s2 - s1)
##print(s1 > s2)
##print(s1 < s3)
##print(s1 > s3)

##frozenset --> r&d


##Functions
##---------
##snippet --> single task
##
##pre - defined
##user - defined
##
##--> return type and parameters
##
##rt    paramters
##1        1
##0        0
##1        0
##0        1
##
##type / class --> function
##
##3 components
##      --> definition
##      --> implementation
##      --> call
##      

##syntax
##------
##
##def <functionname>(): ---> definition
##   <logics>   --> implementation
##
##<functionname>() --> call


##def printme(): # printme
##   print("hello") 
##printme()
##printme()
##printme()
##printme()
##printme()


##def printme(): # printme
##   print("hello")
##
##def printme(): # printme
##   print("bye") 
##
##printme()

##types of parameters / arguements
##-------------------
##formal --> variables --> def
##actual --> values  --> call
##
##4 kinds
##-------
##-> positional
##-> variable 
##-> default
##-> keyworded
##
##parameters  --> inputs

# name as input

##def printme(name): # name --> formal
##   print("hello " + name)
##   
##printme("Mukherjee") # "Mukherjee" --> actual 

##def addnums(a,b):
##   print(a+b)
##addnums(10,20)

##avg --> 5 nums 


# return value
##def avg(a,b):
##   res = (a+b)/5
##   print(res)
##   return "python" 
##   
##print(avg(10,20))

#return variable
##def avg(a,b):
##   res = (a+b)/5
##   print(res)
##   return res
##
##ans = avg(10,20)
##print(ans)

##docstring of a function
##-----------------------


##def avg(a,b):
##   ''' this finds average of 2 nums '''
##   ''' second line'''
##   res = (a+b)/2
##   print(res)

##print(<functionname>.__doc__)
##
##print(avg.__doc__)
##print(len.__doc__)
##print(print.__doc__)

##num1 --> user   30
##num2 --> user inputs 10 
##
##addnums --> 30 10 --> 40
##subnums --> 40 10 --> 30 
##mulnums --> 30 10 --> 300
##divnums --> 300 10 --> 30 

##num1 = int(input("enter a number"))
##num2 = int(input("enter a number"))
##def addnums(num1 , num2):
##   res = num1 + num2
##   print(res)
##   return res 
##def subnums(num1 , num2):
##   res = num1 - num2
##   print(res)
##   return res
##def mulnums(num1 , num2):
##   res = num1 * num2
##   print(res)
##   return res 
##def divnums(num1 , num2):
##   res = num1 / num2
##   print(res)
##   return res 

##addres = addnums(num1 , num2)
##subres = subnums(addres , num2)
##mulres = mulnums(subres , num2)
##divnums(mulres , num2)

##divnums(mulnums(subnums(addnums(num1 , num2) , num2) , num2) , num2)
##
##
##
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
##3
##enter a number
##30
##enter a number
##10
##
##300



##def category():
##   ''' select a category
##    1. Arith
##    2. Logical '''
##   cat = int(input("enter the category"))
##   if cat == 1:
##      print(arith.__doc__)
##      arith()
##   elif cat == 2:
##      logical()
##   else:
##      print("wrong input")
##def arith():
##   ''' select an operation
##          1. Add
##          2. sub
##          3. mul
##          4. div '''
##   
##   ope = int(input("enter an operation"))
##   num1 = int(input("enter a number"))
##   num2 = int(input("enter a number"))
##   
##   if ope == 1:
##      addnums(num1 , num2)
##   elif ope == 2:
##      subnums(num1 , num2)
##   elif ope == 3:
##      mulnums(num1 , num2)
##   elif ope == 4:
##      if num2 == 0 :
##         print("cannot divide with 0")
##      else:
##         divnums(num1 , num2)
##def addnums(a , b):
##   res = a + b
##   print(res)
##def subnums(a , b):
##   res = a - b
##   print(res)
##def mulnums(a , b):
##   res = a * b
##   print(res)
##def divnums(a , b):
##   res = a/ b
##   print(res)
## 
##
##print(category.__doc__)
##category()


##
##def avg(a,b,c):
##   res = (a+b+c) /3
##   print(res)
##avg(10,20,30)
##
##
##variable params

def avg(*abc):
   print(abc)
   print(type(abc))
##
avg(10,20)
avg(10,20,30,40)
avg()
##


##def avg(a , b ,*args):
##   print(a)
##   print(b)
##   print(args)
##   print(type(args))
##
##avg(10,20)
##avg(10,20,30,40)


##def avg(*vars):
##   s = 0
##   for i in vars:
##      s = s+i
##   res = s/len(vars)
##   print(res)
##
##avg(10)
##avg(10,20)
##avg(12,3,4,5,6,7)
##
##stmt --> input enter a stmt
##iam in a python session
##num ----> input enter a number
##2
##
##["iam in " , "in a" , "a python" , "python session"]
##
##anagram(stmt , num)

####return <functionname>
##
##def first():
##   print("hello")
##   return 100
##
##def second():
##   return first


##print(first() ) # 100
##print(second() ) # location of first 
##
##print(type(first() )) # int
##print(type(second() )) # function

##a = second()
##a()
##print(type(a))


##return <functioncall>

##def first():
##   print("hello")
##   return 100
##
##def second():
##   print("bye")
##   return first()

##print(first)
##print(second)
##
##print(first() )
##print(second() )

##print(type(first()))
##print(type(second()))

##default args
##------------

##def emp(name ="employee" , role = "associate"):
##   print("emp name is " + name)
##   print("emp role is " + role)
##   
##emp(role = "pd" , name = "Mukherjee" )
##emp("ravi")
##emp(role = "d")


##cake --> flav , wei , shape

##def makecake(flav = "pine" , wei = 1,shape="square",**kwargs):
##   print("flavour is " + flav)
##   print("weight is " + str(wei))
##   print("shape is " + shape)
##   print(kwargs)
##   print("---------")
##
####makecake("vanilla" , 3 , "round")
####makecake("choco" , 2 )
####makecake(flav = "strw" , shape = "rect")
##
##makecake("vanilla" , 3 , "round" , toppings = "almonds")

##lambda functions
##----------------
##syntax
##------
##
##<functionname> = lambda <params> : <logic>

##addnums = lambda a,b :a+b
##print(addnums(10,20))

##-> anagram
##-> name , org --> email --> lambda
##-> median , mode --> list as param
##
##Files and directories


























