#importing whole module
from tkinter import *
from tkinter.ttk import *
#importing strftime function to
# retrieve system's time
from time import strftime
#creating tkinter window
root = Tk()
root.title('clock')
# This function is used to
# display time on the label
def time()
str = strftime ('%H:%M:%S %p')
Label.config(text = string) 
Label.after(1000, time)
#Styling the label widget so that clock
# will look more attractive
Label = Label(root, font = ('calibri', 40, 'bold'),
background = 'black',
foreground = 'white')
# Placing clock at the centre
# of the tkinter window
Label.pack(anchor = 'center')
time()
mainloop()