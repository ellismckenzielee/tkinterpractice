#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:53:17 2019

@author: ellis
"""

from tkinter import *

#Creating a blank window, which is equal to root
root = Tk()

#create function

def printName():
    print('Hello my name is ellis')
    button_1.configure(text='You said it!')
    
#create button
button_1 = Button(root, text='Say my name', command=printName)
button_1.pack()


#another technique using events
def printName2(event):
    print('Hello my name is Ellis, 2!')
    
#create button
button_2 = Button(root, text='Say my name')
button_2.bind('<Button-1>', printName2)
button_2.pack()
    
#Keeps the program running 
root.mainloop()