############## Using With Block To Open Python Files ############

f = open("29. Tutorial.txt", "rt")

f.close()

# Above open close syntax can be replaced by single statement
# open file using with block
# Everything else(means functions like readlines,seek,etc.) on f are same

# first create a text file "29. Tutorial.txt" then run this program.
with open("29. Tutorial.txt") as f:
    a = f.read(4)
    print(a)
# Output : Stud

with open("29. Tutorial.txt") as f:
    a = f.readlines()  # Give List of lines
    print(a)
# Output :
# ['Students should use LinkedIn to get connected with Corporate and Research world.\n',
# 'It will be very helpful for students.']

# Question of the day -
# Question 1:
# Can we do readlines outside with block?
#  Yes or No and why?

# Answer :
# No, because with block closes the files once we get out of with block.

# Question 2:
# f = open("29. Tutorial.txt", "rt")
# Can we do readlines here?
# f.close()

# Answer :
# Yes

# Corey lecture
with open("29. Tutorial.txt") as f:
    file_content = f.read()
    print(file_content)

# Reading the file using for loop.After reading the file using f.read() we cannot use for loop as the content has already been read
with open("29. Tutorial.txt") as f:
    for item in f:
        print(item, end="")

# Reading chunk of data using while loop.
with open("29. Tutorial.txt") as f:
    chunk_size = 10
    file_content = f.read(chunk_size)
    while len(file_content) > 0:
        print(file_content, end="")
        file_content = f.read(chunk_size)

# Reading and writing of file
with open("29. Tutorial.txt", "r") as rf:
    with open("29. Tutorial_copy.txt", "w") as wf:
        for item in rf:
            wf.write(item)
