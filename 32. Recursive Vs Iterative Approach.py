def print2(str1):
    # print2("Aditya")  #Recursion happens 
    print("This is " + str1)

print2("Harry")
# output: Recursion error [Previous line repeated 996 more times]

#Iterative approach
def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

inp = int(input("Enter the number\n"))
print(factorial_iterative(inp))

#Recursive approach
def factorial_recursive(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        num = num * factorial_recursive(num-1)
    return num

# print(factorial_recursive(5))

#Fibonacci series
0,1,1,2,3,5,8,11

def Fibonacci_series(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return Fibonacci_series(number-1) + Fibonacci_series(number-2)


_inp = int(input("Enter the number\n"))
print(Fibonacci_series(_inp))