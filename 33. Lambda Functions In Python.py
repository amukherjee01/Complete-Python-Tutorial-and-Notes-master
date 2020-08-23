#Lamda function or anonymous function


# def add(a,b):
#     return a +b

# print(add(12,23))

#Lambda function is short hand way of writing function
add = lambda a,b: a + b
print(add(12,12)) 
# output: 24

# def a_first(a):
    # return a[1]  #return 1st index from a

a = [[1,14], [5,6], [8,23]]
#a.sort(key= a_first)  # sort based on a_first function
a.sort(key=lambda x: x[1]) #using lambda function return x[1]
print(a)
# output:[[5, 6], [1, 14], [8, 23]]

myemail = lambda fname, lname: f"{fname}.{lname}@gmail.com"
print(myemail('aditya','mukherjee'))