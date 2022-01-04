# Python code showing protected and private encapsulation


# Example of a Private Encapsulation
#Creating a Person class
class Person:
    
    def __init__(self):
        #Protected Variable
        self._Faculty = 0
        #Private Variable
        self.__Students = 50

    def getNumber(self):
        print(self.__Students)

    def setNumber(self, Number):
        self.__Students = Number

        
# object that makes use of the protected  and  Private variable
obj = Person()
print(obj._Faculty)
obj._Faculty = 100
print(obj._Faculty)
obj.getNumber()
obj.setNumber(55)
obj.getNumber()



    


