
import shutil
import os

#set where the source of the files are
source ='/Users/Stephanie/Desktop/Folder A/'

#set the destination path to folder B
destination ='/Users/Stephanie/Desktop/Folder B/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
