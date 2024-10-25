class Human:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def giveAge(self):
        return self.__age   
    
    
me = Human("Digbijaya", 21)

print(me.giveAge())
