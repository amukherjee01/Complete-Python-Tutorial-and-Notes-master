# Enumerate function returns both index as well as items from list.

l1 = ["Bhindi", "Aloo", "Chopsticks", "Chowmein"]

# i = 0
# for item in l1:
#     if i % 2 == 0:
#         print(f"Jarvis buy {item}")
#     i += 1

for index, item in enumerate(l1):
    if index % 2 == 0:
        print(f"Jarvis buy {item}")

# # output
# Jarvis buy Bhindi
# Jarvis buy Chopsticks
