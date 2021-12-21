# Python 3.10.1
#
#Author: Stephanie L Drake
#
# This is an Assignment from The Tech Academy Python Course. It shows and example of polymorphism where you have a child class
# perform the same function in different ways.
#
# Parent Class Person
class Person:
    fname = "John"
    lname = "Jones"
    id = "38695"


# Defining method for the "Person" class
    def getInfo(self):
        enter_fname = input("Enter First name: ")
        enter_lname = input("Enter Last name: ")
        enter_id = input("Enter id number: ")
        if (enter_lname == self.lname and enter_id == self.id):
            print("Hello, {}! You are the correct person!".format(enter_fname))
        else:
            print("You are not the correct person.")

# Child Class Student
class Student(Person):
    fname = "Sally"
    lname = "Harris"
    student_id = "56783"
    grade = "9th"
    gpa = "3.6"
    

# This is the same method in the parent class "Person"
# The difference is that, instead of using enter_id, we're using enter_student_id.

    def getInfo(self):
        enter_fname = input("Enter First name: ")
        enter_lname = input("Enter Last name: ")
        enter_student_id = input("Enter student id: ")
        if (enter_lname == self.lname and enter_student_id == self.student_id):
            print("Hello,  {}! You are a student at this school!".format(enter_fname))
        else:
            print("You are not a student at this school.")
            
      

# Class Child Staff
class Staff(Person):
    fname = "Polly"
    lname = "Fields"
    staff_id = "F19047"
    position = "Administration"
    hire_date = "09/01/99"
    

# This is the same method in the parent class "Person"
# The difference is that, instead of using enter_id, we're using staff_id.

    def getInfo(self):
        enter_fname = input("Enter First name: ")
        enter_lname = input("Enter Last name: ")
        enter_staff_id = input("Enter Staff id: ")
        if (enter_lname == self.lname and enter_staff_id == self.staff_id):
            print("Hello, {}! You are a staff member at this school!".format(enter_fname))
        else:
            print("You are not a staff member at this school.")
            

    

    
if __name__ == "__main__":
   faculty = Person()
   faculty.getInfo()

   pupils = Student()
   pupils.getInfo()

   administration = Staff()
   administration.getInfo()
   


    


































