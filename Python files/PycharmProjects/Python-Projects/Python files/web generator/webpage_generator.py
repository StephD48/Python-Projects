# Python Ver: 3.10.1
#
#Author: Stephanie Drake
#
#Purpose: Create an HTML file in Pyhton, Create a GUI that allows the User
#to enter text and initiate the web page generation process, and Opens the web page
#with the changes.
#
# import everything from tkinter module
import tkinter as tk
import webbrowser as wb
from tkinter import *

#html template
html = """<html>
        <body>
        <h1>{}</h1>
        </body>
        </html>"""
#defining a Parent Class
class ParentWindow(Frame):
    def __init__ (self, master): # defining an init funtion
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(510,185))
        self.master.title('Check files')
        self.master.config(bg='lightgray')

        self.userText = StringVar()# Declaring a variable self.userText
        # Creating an entry field for the users input
        self.b1_entry = Entry(self.master,text=self.userText, font = ('calibre',10,'normal'), width=50, show ='')
        self.b1_entry.grid(row=2, column=1, padx=(20,0), pady=(35,0))
        
        # Creating a button to Open the Web page
        self.b3 = Button(self.master, text="Open Webpage",width=15,height=2, command=self.openfile)
        self.b3.grid(row=6,column=0, padx=(10,0), pady=(15,0), sticky=SW)
        # Creating a button to Close the Program
        self.b4 = Button(self.master, text="Close Program", width=15,height=2)
        self.b4.grid(row=6, column=1, padx=(10,0),pady=(15,0),sticky=S+E)
        
        
        
        

    def openfile(self): #Defining a function to open file
        text= self.userText.get()# Declaring variable called "text"
        f = open("web.html", "w")# Opening the html file
        f.write(html.format(text))# User inputing text into htlm file
        f.close()# Closing the file


        wb.open('web.html',new=2,autoraise=True)#Calling the web page to be opened in the browser

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop
