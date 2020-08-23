
# snake water gun game

# Snake Water Gun Game in Python
# The snake drinks the water, the gun shoots the snake, and gun has no effect on water.

import random

lst = ["s", "w", "g"]

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print(" \t \t \t \t Snake,Water,Gun Game\n \n")
print("s for snake \nw for water \ng for gun \n")

# making the game in while
while no_of_chance < chance:
    _input = input("Snake,Water,Gun:")
    _random = random.choice(lst)

    if _input == _random:
        print("Tie Both 0 point to each \n ")

    # if user enter s
    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter w
    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter g

    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point == human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")

#

# import random

# gamelist = ["S", "W", "G"]
# attempt = 5
# noofattempt = 0
# comppoint = 0
# humanpoint = 0

# while noofattempt < attempt:
#     compchoice = random.choice(gamelist)
#     inp = input("Enter Your choice 'S', 'W', 'G'\n")
#     if inp.lower() == compchoice.lower():
#         print(
#             f"Its a Tie. Human point is {humanpoint} and computer point is {comppoint}"
#         )
#         noofattempt += 1
#     elif inp.lower() == "s" and compchoice.lower() == "w":
#         humanpoint += 1
#         print(f"Human win.Human point {humanpoint} and computer point {comppoint}")
#         noofattempt += 1
#     elif inp.lower() == "s" and compchoice.lower() == "g":
#         comppoint += 1
#         print(f"Computer win.Computer point {comppoint} and human point {humanpoint}")
#         noofattempt += 1
#     elif inp.lower() == "w" and compchoice.lower() == "s":
#         comppoint += 1
#         print(f"Computer win.Computer point {comppoint} and human point {humanpoint}")
#         noofattempt += 1
#     elif inp.lower() == "w" and compchoice.lower() == "g":
#         humanpoint += 1
#         print(f"Human win.Human point {humanpoint} and computer point {comppoint}")
#         noofattempt += 1
#     elif inp.lower() == "g" and compchoice.lower() == "s":
#         humanpoint += 1
#         print(f"Human win.Human point {humanpoint} and computer point {comppoint}")
#         noofattempt += 1
#     elif inp.lower() == "g" and compchoice.lower() == "w":
#         comppoint += 1
#         print(f"Computer win.Computer point {comppoint} and human point {humanpoint}")
#         noofattempt += 1

# print("####################")
# print("Game Over")
# if humanpoint > comppoint:
#     print(f"Human wins. Human point {humanpoint} and Computer point {comppoint}")
# elif humanpoint == comppoint:
#     print("Its a Tie. between human and computer")
# else:
#     print(f"Computer win.Computer point {comppoint} and human point {humanpoint}")
