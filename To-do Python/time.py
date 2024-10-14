from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title('clock')
def time():
str = strftime ('%H:%M:%S %p')
Label.config(text = string) 
Label.after(1000, time)
Label = Label(root, font = ('calibri', 40, 'bold'),
background = 'black',
foreground = 'white')
Label.pack(anchor = 'center')
time()
mainloop()
