# Pattern printing

inp = int(input("Enter Interger number\n"))
boolvalue = int(input("Enter bool value\n"))
if boolvalue:
    for i in range(1, inp + 1):
        print("*" * i)
else:
    for k in range(inp, 0, -1):
        print("*" * k)
