# os module is built in python module for dealing with underlying system.
import os

# List all the attributes and methods present in os module
print(dir(os))

# Prints out the current working directory path
print(os.getcwd())
# output :
# C:\Work\complete python\CodeWithHarryPython\Complete-Python-Tutorial-and-Notes-master

# This is to change the directory path and navigate to other path
os.chdir(r"C:\Users\Lenovo\Desktop")
print(os.getcwd())
# output :
# C:\Users\Lenovo\Desktop

# List out all the directories in the current path. We can also pass the path in listdir method explicitly.
print(os.listdir())
# output :
# '1 - Cisco AnyConnect Secure Mobility Client.lnk', '2 - CITRIX Receiver.lnk', 'Daily_Report (30th june).xlsx', 'desktop.ini', 'Doc1.docx', 'New Joining Pack - May2020.rar', 'office', 'pythoncodewithharry', 'Resume.doc', 'ThingsToDo.txt']

# Create directory in the current path with the name os-module
os.mkdir("os-module")
# create chain of directory using makedirs method
os.makedirs("os-module-python/os-module-topic")

# Remove the directory with name os-module
os.rmdir("os-module")
# Remove chain of directory
os.removedirs("os-module-python/os-module-topic")


# Rename the directory name os-module will change to testmodule
os.rename("os-module", "testmodule")
print(os.listdir())

# yeilds a tuple of 3 values as it walks through the directory
# directorypath, directoryname, filename.
# It starts from the current path and deep dive into the directory
# os.walk(os.getcwd('pass the directory here'))
for dirpath, dirname, filename in os.walk(os.getcwd()):
    print(f"Directory Path : {dirpath}")
    print(f"Directory name : {dirname}")
    print(f"File name : {filename}")
    print()
# # output:
# Directory Path : C:\Users\Lenovo\Desktop\office\New Joining Pack - May2020\images
# Directory name : []
# File name : ['Aditya Mukherjee - Appointment Letter chg to 8 June.pdf', 'Capture.PNG', 'date.jpg', 'date_1.jpg', 'Internship offer.jpg', 'Offer Letter.jpg', 'signature.jpg', 'signatur_1.jpg']

# Need to clear this
# print(os.environ.get(r"C:\Users"))

# os.path.join joins the file with the directory
file_path = os.path.join(r"C:\Users\Lenovo\Desktop\testmodule", "test.txt")
print(file_path)
# output:
# C:\Users\Lenovo\Desktop\testmodule\test.txt

# Returns the file name
print(os.path.basename(r"\tmp\test.txt"))
# output:
# test.txt

# Returns the path
print(os.path.dirname(r"\tmp\test.txt"))
# output:
# \tmp

# Returns both path and filename. Returns tuple.
print(os.path.split(r"\tmp\test.txt"))
# output:
# ('\\tmp', 'test.txt')

# Returns False if path not exists otherwise True
print(os.path.exists(r"\tmp\test.txt"))
# output :False

# Return False if test.txt is not file
print(os.path.isfile(r"\tmp\test.txt"))
# output:False

# Returns tuple with path and extension
print(os.path.splitext(r"\tmp\test.txt"))
# output:
# ('\\tmp\\test', '.txt')
