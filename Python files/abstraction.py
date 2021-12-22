# Python Abstraction Assignment
#
#
from abc import ABC, abstractmethod
#Creating a class Library
class Library(ABC):
    def Checkout(self, date):
        print("Your books were checked out on: ",date)
# This function is telling us to pass in an argument, but we won't tell you how or what kind of data it willbe.
    @abstractmethod
    def Books(self, date):
        pass

class Returns(Library):
    # here we've defined how to implement the books functon from its parent Checkout class.
    def Books(self, date):
        print('Your books are due on {}, Thank you!'.format(date))

obj = Returns()
obj.Checkout("08/21/21")
obj.Books("08/31/21")
