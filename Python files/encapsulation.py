# Python code showing protected and private encapsulation

# Example of a Protected Variable
# Creating a Student class
class Student:
    def __init__(self):
        #Protected Variable
        self._girls = 0
#object that makes use of protected variable       
obj = Student()
obj._girls = 15
print(obj._girls)




# Example of a Private Encapsulation
#Creating a Person class
class Person:
    def __init__(self):
        #private variable
        self.__Students = 50

    def getNumber(self):
        print(self.__Students)

    def setNumber(self, Number):
        self.__Students = Number
        
# object that makes use of the private variable
obj = Person()
obj.getNumber()
obj.setNumber(55) # will not change the variable because it's private
obj.getNumber()

    


