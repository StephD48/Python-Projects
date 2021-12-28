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



def getSource(self):
    sourcePath = filedialog.askdirectory(initialdir="/",title='Select Folder')
    self.txt_source.insert('0', sourcePath)

    source="C:\\Users\\Stephanie\\Documents\\GitHub\\Python-Projects\\Python files\\File Transfer Project\\Incoming Files" 




def getDestination(self):
    destinationPath = filedialog.askdirectory(initialdir="/",title='Select Destination Folder')
    self.txt_destination.insert('0', destinationPath)

    destination = "C:\\Users\\Stephanie\\Documents\\GitHub\\Python-Projects\\Python files\\File Transfer Project\\Destination Files"


def copy(self):
    source = self.txt_source.get() 
    destination = self.txt_destination.get() 
    fileNames = os.listdir(source)
    print(fileNames)

    for file in fileNames:
        Path = os.path.join(source, file)
        modifySec = os.path.getmtime(Path)
        modifyTime = datetime.fromtimestamp(modifySec)
        
        if modifyTime > (datetime.now() + timedelta(days= -1)):
            shutil.copy(Path, destination)

        
        
        



if __name__ == "__main__":
    pass
