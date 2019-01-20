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
f.close()

    




    