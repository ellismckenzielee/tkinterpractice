#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:53:17 2019

@author: ellis
"""

from tkinter import *

#Creating a blank window, which is equal to root
root = Tk()


#Split the window into two smaller frames (top and bottom)
topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#Widgets
button1 = Button(topFrame, text="Button 1", fg='red')
button2 = Button(topFrame, text="Button 2", fg='blue')
button3 = Button(topFrame, text="Button 3", fg='green')
button4 = Button(bottomFrame, text="Button 4", fg='purple')

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()

#Keeps the program running 
root.mainloop()