#My first GUI

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python GUI')

#The next line prevent the GUI window from being resized.
#win.resizable(False, False)

#Creats a label and uses the .grid method to position it.
#ttk is a module inside tkinter, it stands for "themed tk"
top_label = ttk.Label(win, text='A Label')# creates a module level variable we can later change
top_label.grid(column=0, row=0) 

#The function that executes when the button is clicked
def click_me():
    action.configure(text='Ive been clicked!') #changes the text attribute of the button.
    top_label.configure(foreground='red') #changes the foreground i.e. font color of the label.
    top_label.configure(text='A Red Label') #changes the text attribute of the label. 

action = ttk.Button(win, text='Click me!', command=click_me) 
#creates a button widget with a text and a command attribute then binds the command to the click_me function.
action.grid(column=1, row=0)#positions the button after the label but on the same level.

#creating a second label for a second button
button_label = ttk.Label(win, text='Enter a name:').grid(column=0, row=1)

def click_me2(): #function run by the second button
    action2.configure(text='Hello ' + name.get()) #changes the text attribute by getting the 'name' var
    #we get the value of the Entry widget with the name.get() method

action2 = ttk.Button(win, text='Send!', command=click_me2)# second button created, binds to click_me2 func.
action2.grid(column=2, row=1)

name = tk.StringVar() #Create a var called 'name' of the StringVar() class from the tk module. 
#This var is bound to the Entry widget.
name_entered = ttk.Entry(win, width=12,  textvariable=name) #creates a Entry widget under the var 'name_entered'
#the Entry widget stores the entered text to 'name' var.
name_entered.grid(column=1, row=1) 


win.mainloop()

