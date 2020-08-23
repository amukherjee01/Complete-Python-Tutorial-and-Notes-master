import random, math

random_number = random.randint(0, 5)  # Includes both 0 and 5
# print(random_number)
# Output : 0,1,2,...any random number between 0 to 5
rand = random.random()
print(rand)  # Random number between 0 to 1
# outout : 0.4620905986499929

rand = math.floor(random.random() * 100)
print(rand)
# outout : 98

lst = ["Star Plus", "DD1", "Aaj Tak", "CodeWithHarry"]
choice = random.choice(lst)
# This return multiple list. Based on weights. The below will return list with 5 members as k=5
choices = random.choices(lst, weights=[4, 1, 1, 1], k=5)
print(choice)
# outout: CodeWithHarry
print(choices)
# outout: ["Star Plus", "CodeWithHarry", "DD1", "Star Plus", "DD1"]

# External module
# pip install sklearn
# pip insatall flask
# pip install django
