# def function_name_print(a, b, c, d):
#     """ Prints name of name """
#     print(a, b, c, d)


# function_name_print("Harry", "Rohan", "Aditya", "Larry")

# Args also known as variable argument. Type of args is tuple.

# Now we can pass any number of arguments in funcargs function.
def funcargs(normal, *args):
    print(type(args))
    print(args)
    print(normal)
    for item in args:
        print(item)


name = ["Harry", "Aditya", "Mukesh", "Shiva", "Ramesh"], "hehehe"

# Passing name without packing it. This will pass as tuple first argument.
# funcargs(name)

# Ex: ((['Harry', 'Aditya', 'Mukesh', 'Shiva', 'Ramesh'], 'hehehe'),)
# output: ((['Harry', 'Aditya', 'Mukesh', 'Shiva', 'Ramesh'], 'hehehe'),)

# This will pack the name and pass it to funcargs as tuple
# funcargs(*name)
# here first argument as ["Harry", "Aditya", "Mukesh", "Shiva", "Ramesh"] and 2nd argument as hehehe
# output:(['Harry', 'Aditya', 'Mukesh', 'Shiva', 'Ramesh'], 'hehehe')

name = ["Harry", "Aditya", "Mukesh", "Shiva", "Ramesh"]
normal = "I am a normal argument and the students are :"
funcargs(normal, *name)
# output :<class 'tuple'>
# output: ('Harry', 'Aditya', 'Mukesh', 'Shiva', 'Ramesh')
# Output :I am a normal argument and the students are :
# Harry
# Aditya
# Mukesh
# Shiva
# Ramesh

# funcargs(*name, normal)
# output: funcargs() missing 1 required keyword-only argument: 'normal'
# NOTE: Rule of thumb. Always pass the normal argument first and then 2nd argument as args and third argument as kwargs


# Kwargs also known as keyworded argument. Type of kwargs is dictionary.
# In kwargs we can pass variable number of keyworded argument


def funckwargs(normal, *args, **kwargs):
    print(type(kwargs))
    print(kwargs)
    print(normal)
    print(kwargs.items())
    for item, value in kwargs.items():
        print(f"{item} is {value}")


dictname = {
    "name": "aditya",
    "age": 23,
    "job": "SDE",
    "languages": ["C++", "Python", "JavaScript"],
}
normal = "I am normal from kwargs"
# This will not through error as args and kwargs are the optional argument
funckwargs(normal)
funckwargs(normal, **dictname)
# output:
# <class 'dict'>
# {'name': 'aditya', 'age': 23, 'job': 'SDE', 'languages': ['C++', 'Python', 'JavaScript']}
# dict_items([('name', 'aditya'), ('age', 23), ('job', 'SDE'), ('languages', ['C++', 'Python', 'JavaScript'])])
# name is aditya
# age is 23
# job is SDE
# languages is ['C++', 'Python', 'JavaScript']

# Note : Args and kwargs are the optional argument

funckwargs("aditya", "Mukherjee", name="aditya", age=67)

# output:
# <class 'dict'>
# {'name': 'aditya', 'age': 67}
# aditya
# dict_items([('name', 'aditya'), ('age', 67)])
# name is aditya
# age is 67
