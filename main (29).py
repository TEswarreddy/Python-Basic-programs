# class & objects

class Employee:
    def __init__(self,salary,empid,name):
        self.salary=salary
        self.empid=empid
        self.name=name
        
    def getsalary(self):
        return self.salary
    def getempid(self):
        return self.empid
    def getname(self):
        return self.name
        
    def updates(self,salary,empid,name):
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
print(emp1.getname())
print(emp1.getempid())
print(emp1.getsalary())
#updating attribute values
emp1.updates(500000,1,"Hemarsh")