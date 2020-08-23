class Employee:
    
    def __init__(self,fname,lname):
        self.fname = fname 
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"
    
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"
    
    @email.setter
    def email(self,emailadd):
        print("Setting now.....")
        name = emailadd.split("@")[0]
        self.fname = name.split(".")[0] 
        self.lname = name.split(".")[1]



emp1 = Employee("aditya","mukherjee")
emp2 = Employee("Harry","bhai")
print(emp1.explain())
print(emp1.email)
emp1.fname = "Sudhir"
print(emp1.email)
emp1.email = "Abhishek.Singh@gmail.com"
print(emp1.fname)
print(emp1.lname)