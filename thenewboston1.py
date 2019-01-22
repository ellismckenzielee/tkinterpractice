#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:53:17 2019

@author: ellis
"""

from tkinter import *

#Creating a blank window, which is equal to root
root = Tk()

#Create Labels and entry widgets
#Use .grid to position widgets and labels with more control

label_1 = Label(root, text='Name:')
label_2 = Label(root, text='Password:')
entry_1 = Entry(root)
entry_2 = Entry(root)


#Add sticky and the direction to align text in frame/window/column
label_1.grid(row=0, sticky=E)
label_2.grid(row=1)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

#Checkbox
c = Checkbutton(root, text='Keep me logged in')
c.grid(row=2, columnspan=2)

#Keeps the program running 
root.mainloop()