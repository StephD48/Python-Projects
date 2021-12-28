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
import file_transfer_main


# Defining the getSource function
def getSource(self):
    sourcePath = filedialog.askdirectory(initialdir="C:/") # defining source path in directory
    self.txt_source.insert('0', sourcePath)
    # Source path for the incoming files
    source="C:\\Users\\Stephanie\\Documents\\GitHub\\Python-Projects\\Python files\\File Transfer Project\\Incoming Files" 



# Defining the getDestination function
def getDestination(self):
    destinationPath = filedialog.askdirectory(initialdir="C:/")
    self.txt_destination.insert('0', destinationPath)
    # Source path for the Destination files
    destination = "C:\\Users\\Stephanie\\Documents\\GitHub\\Python-Projects\\Python files\\File Transfer Project\\Destination Files"

# Defining the copy function
def copy(self):
    # path where the incoming files are located
    source = "C:\\Users\\Stephanie\\Documents\\GitHub\\Python-Projects\\Python files\\File Transfer Project\\Incoming Files"
    # path where the files will be copied to 
    destination = "C:\\Users\\Stephanie\\Documents\\GitHub\\Python-Projects\\Python files\\File Transfer Project\\Destination Files" 
    fileNames = os.listdir(source) # Creates a list of all the file names in the directory
    print(fileNames)

    for file in fileNames:
        # path for the file
        Path = os.path.join(source, file)
        modifiedSec = os.path.getmtime(Path) #time is given in a float
        modifiedTime = datetime.fromtimestamp(modifiedSec)# converts float into a datetime structure
        
        if modifiedTime > (datetime.now() + timedelta(days= -1)):# If date of file within the last 24hrs it will be copied to destination
            shutil.copy(Path, destination)

        
        
        



if __name__ == "__main__":
    pass
