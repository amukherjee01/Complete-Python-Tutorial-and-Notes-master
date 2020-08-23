#  F string
import math

me = "Harry"
age = 30
a = "This is me %s" % me
print(a)
print("my name is %s and my age is %d" % (me, age))
print("my name is {1} and my age is {0}".format(me, age))
print(f"my name is {me} and age is {age} and {math.cos(65)}")  # f string
