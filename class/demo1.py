class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname,self.lastname)



diggy = Person("digbijaya","lenka")

diggy.printname();

class Employee(Person):
    def __init__(self,fname,lname,salary):
        super().__init__(fname,lname)
        self.salary = salary

    def printname(self):
        print(self.firstname,self.lastname,self.salary)
        
        
tony = Employee("tony","stark",50000)

tony.printname()