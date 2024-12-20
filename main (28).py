# class & objects

class Employee:
    def __init__(self,salary,empid,name):
        self.salary=salary
        self.empid=empid
        self.name=name
        
    def getsalary(self):
        print(self.salary)
    def getempid(self):
        print(self.empid)
    def getname(self):
        print(self.name)
        
    def display(self,salary,empid,name):
        self.salary=salary
        self.empid=empid
        self.name=name
        print("updating the attribute values")
        print(self.name)
        print(self.empid)
        print(self.salary)
        
emp1=Employee(20000,1,"Hemanth")
print(emp1.salary)
print(emp1.empid)
print(emp1.name)
#get function
emp1.getname()
emp1.getempid()
emp1.getsalary()
#updating attribute values
emp1.display(500000,1,"Hemaharsh")