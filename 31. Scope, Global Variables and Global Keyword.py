#Global variable can be used in the entire program
l = 10 # Global variable have global scope

def function1(n):
    # l = 5
    global l # This gloabal keyword gives permision to change the global variable
    l = l + 45 # This will through error . We cannot change global variable (local variable 'l' referenced before assignment). To resole use gloabal l
    m = 8
    print(l) # output : 10  (Because l is having global scope)
    # l and m is local variable here.First it will check in local scope for l and m.  
    print(l,m) # output : 5,8   
    print(n, "I have printed")

function1("This is me")
print(l)
# output : This is me I have printed
# output : 10
#print(m) 
# output : name 'm' is not defined
#Gives error as it is local variable


def harry():
    x = 20
    def rohan():
        global x
        x = 88
    print("Before calling rohan()",x) # x is in local scope so it will print 20
    rohan()
    print("After calling rohan()",x) # x : 20 (Because x is not global variable so it will remain same as 20)

harry()
# output : Before calling rohan() 20
# output: After calling rohan() 20
print(x)
# This will create a gloabal variable x = 88
# output : 88

x = 89
def harry():
    x = 20
    def rohan():
        global x
        x = 88
    # print("Before calling rohan()",x) # x is in local scope so it will print 20
    rohan()
    print("After calling rohan()",x) # x : 20 (Because x is in local scope of harry function with x = 20)

harry()
print(x) # Global x will change the value of x = 88
# output : After calling rohan() 20
# output : 89