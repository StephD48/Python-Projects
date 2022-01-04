# Python Ver: 3.10.1
#
#Author: Stephanie Drake
#
#Purpose: Create a File Transfer Script. This will transfer files that represent
#customer orders and send the new or updated files from the previous 24hrs and
#send them to the home office.
#
#
#import tkinter modules

from tkinter import *
import tkinter as tk
from tkinter import filedialog
import datetime 
from datetime import datetime
from datetime import timedelta
import shutil
import os

#This imports the other modules so we have access to them
import file_transfer_gui
import file_transfer_func

#Defining the class ParentWindow(Frame)
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs): #Defining the init class
        Frame.__init__(self, master, *args, **kwargs)

        #defining the self.master config
        self.master = master
        self.master.minsize(500,300)
        self.master.title("File Transfer within last 24 hours")
        arg = self.master
        
        file_transfer_gui.startGui(self)
        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
