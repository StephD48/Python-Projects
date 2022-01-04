Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import sqlite3
# get personal data from user and insert into a tuple
firstName = input("Enter your first name: ")
Enter your first name: Stephanie
lastName = input("Enter your last name: ")
Enter your last name: Drake
age = int(input("Enter your age: "))
Enter your age: 47
personData = (firstName, lastName, age)

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)

    
<sqlite3.Cursor object at 0x00000249C42B8340>
c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
          (45, 'Luigi', 'Vercotti'))
<sqlite3.Cursor object at 0x00000249C42B8340>

= RESTART: C:/Users/Stephanie/Documents/GitHub/Python-Projects/Python files/sqliteassignment.py
('Ron', 'Obvious')
('Luigi', 'Vercotti')

= RESTART: C:/Users/Stephanie/Documents/GitHub/Python-Projects/Python files/sqliteassignment.py
('Ron', 'Obvious')
('Luigi', 'Vercotti')
