import random as r
#print(r.random())
#print(r.randint(10,30))
#print(r.randrange(10,30))

#l1 = [x for x in range(1,11)]
#print(l1)
#r.shuffle(l1)
#print(l1)
#print(r.choice(l1))
#print(r.sample(l1,3))

#Random password generator
'''
ndict = {}
name = input("enter username")

def userCheck(name):
    if name in ndict.keys():
        print("user already exist")
        return 0
    else:
        return 1


def genchars(m):
    chars = ""
    pwd = ""
    l = []
    for i in range(m//2):
        chars = chars + chr(r.randrange(67,90))
        chars = chars + chr(r.randrange(97,122))
    for c in chars:
        l.append(c)
        r.shuffle(l)
        pwd = "".join(l)
    return pwd
#res = genchars(4)
#print(res)

       


def genNums(m):
    empList = []
    nums = ""
    for i in range(m):
        nums = nums + str(r.randrange(0,9))
    return nums
#res = genNums(4)
#print(res)
    

def genPwd(username):
    if userCheck(name) == 0:
        print("user already exist")
    elif userCheck(name) == 1:
        password = genchars(4) + genNums(4) + genchars(4) + genNums(4)
        ndict[name] = password
        print("%s--%s"%(name,password))
        print(ndict)
        return password
    else:
        print("some issue")

genPwd(name)
f = open("opendict.txt","w")
f.write(str(ndict))
f.close() '''

userDict = {}

def genPwd(name ):
	status = userChk(name)
	if(status == 1):
		password = randChars(4)+ randNumbers(8) + randChars(4)
		print "Password of  "+name+" is : "+ password 
		userDict[name] = password
	else :
		print "Error "
def userChk( name ):
	usersList = userDict.keys()
	if(name in usersList):
		print " User " +name+" already exist "
		return 0
	else:
		return 1 
def randChars(length):
	chars = []
	pwdStr = ""
	for i in range(1,length//2 +1):
		a = r.randint(67,90)
		b = r.randint(97,122)
		chars.append(chr(a))
		chars.extend(list(chr(b)))
	r.shuffle(chars)
	for char in chars:
		pwdStr =pwdStr+char
	return pwdStr
def randNumbers(length):
	nums = []
	pwdNum = ""
	for i in range(1,length):
		n = r.randint(0,9)
		nums .append(str(n))
		r.shuffle(nums)
	for num in nums:
		pwdNum =pwdNum+num
	return pwdNum


genPwd("aditya")
genPwd("Shiva")
genPwd("Ravi")

f = open("opendict.txt","w")
f.write(str(userDict))
f.close() 

    




    