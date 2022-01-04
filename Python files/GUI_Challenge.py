import tkinter as tk
from tkinter import *



class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        browserVar1 = StringVar()
        browserVar2 = StringVar()


        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(510,185))
        self.master.title('Check files')
        self.master.config(bg='lightgray')

     
        
        b1 = Button(self.master, text="Browse...", width=15, height=0)
        b1.grid(row=2, column=0, padx=(10,0), pady=(40,0), sticky=NW)

        b2 = Button(self.master, text="Browse...", width=15, height=0)
        b2.grid(row=3,column=0, padx=(10,0), pady=(20,0), sticky=W)

        b3 = Button(self.master, text="Check for files...",width=15,height=2)
        b3.grid(row=6,column=0, padx=(10,0), pady=(15,0), sticky=SW)

        b4 = Button(self.master, text="Close Program", width=15,height=2)
        b4.grid(row=6, column=1, padx=(10,0),pady=(15,0),sticky=S+E)
        
        b1_entry = Entry(self.master, textvariable = browserVar1, font = ('calibre',10,'normal'), width=50, show ='*')
        b1_entry.grid(row=2, column=1, padx=(20,0), pady=(35,0))
        
        b2_entry = Entry(self.master, textvariable = browserVar2, font = ('calibre',10,'normal'), width=50, show ='*')
        b2_entry.grid(row=3, column=1, padx=(20,0), pady=(20,0))
        
    
        
        
            







if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
