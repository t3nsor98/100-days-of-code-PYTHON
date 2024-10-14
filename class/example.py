class myClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
diggy = myClass("digbijaya",25)
print(diggy)