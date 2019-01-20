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

'''
def printme():
    print("hello")'''

'''
def printme(name):
#    hello this is new function
#    how are you'''
    
#    print("hello",name)

#printme("aditya")
#print(printme.__doc__)'''


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

'''
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
category()'''


def first():
   print("hello")
   return 100

def second():
   print("bye")
   return first()