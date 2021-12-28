# import tkinter modules

from tkinter import *
import tkinter as tk
from tkinter import filedialog
import datetime 
from datetime import datetime
from datetime import timedelta
import shutil
import os

# Import other modules so we can access them
import file_transfer_main
import file_transfer_func



def startGui(self): # Defining gui widgets function


    # Creating Labels for GUI
    # Class name for labels - self.lbl_source, self.lbl_destination, also grid is the Labels location in the window
    self.lbl_source = tk.Label(self.master, text="Select Files", bg='lightblue')
    self.lbl_source.grid(row = 0, column = 1, padx=(10,0), pady=(10,0))
    self.lbl_destination = tk.Label(self.master, text ="Select Destination", bg='lightblue')
    self.lbl_destination.grid(row = 2, column = 1, padx=(10,0), pady=(10,0))

    #Creating Buttons for GUI
    # Class name for Buttons- self.btn_source, self.btn_destination, self.btn_copy,also grid is the buttons location in the window
    self.bt1_source =  tk.Button(self.master, width = 10, height = 1, text = "Browse",bg='lightblue', command = lambda: file_transfer_func.getSource(self))
    self.bt1_source.grid(row = 1, column = 0, padx = (10,0), pady = (10,0))
    self.bt2_destination = tk.Button(self.master, width = 10, height = 1, text = "Browse",bg='lightblue', command = lambda: file_transfer_func.getDestination(self))
    self.bt2_destination.grid(row = 3, column = 0,  padx=(10,0), pady=(10,0))
    self.bt3_copy = tk.Button(self.master, width = 10, height = 1, text = "Copy",bg='lightblue', command = lambda: file_transfer_func.copy(self))
    self.bt3_copy.grid(row = 4, column = 1, padx=(10,0), pady=(10,0))

    #Creating Text box for GUI
    # Class name for Text Entry - self.txt_source, self.txt_destination, also grid is the text box location in the window
    self.txt_source = tk.Entry(self.master, width= 50, font=('calibre', 10))
    self.txt_source.grid(row = 1, column = 1, padx = (10,0), pady = (10,0))
    self.txt_destination = tk.Entry(self.master, width= 50, font=('calibre', 10))
    self.txt_destination.grid(row = 3, column = 1, padx = (10,0), pady = (10,0))






if __name__ == "__main__":
    pass
