import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd

def callback():
    name= fd.askdirectory()
    print(name)

    
    
b1 = Button(text='Ask Directory', command=callback, width=15, height=0)
b1.grid(row=2,column=0, padx=(10,0), pady=(40,0), sticky= NW)
b1_entry = Entry(textvariable = "", font = ('calibre',10,'normal'), width=50, show ='')
b1_entry.grid(row=2, column=1, padx=(20,0), pady=(35,0))
        
    
tk.mainloop()
         
    
        
    
        
    

