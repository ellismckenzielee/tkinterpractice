#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:53:17 2019

@author: ellis
"""

from tkinter import *

#Creating a blank window, which is equal to root
root = Tk()

#Create labels
one = Label(root, text='One', bg='red', fg='white')
one.pack()

two = Label(root, text='Two', bg='green', fg= 'black')
#Fill X means that it fills the surrounding frame/window
two.pack(fill=X)


three = Label(root, text='Three', bg='blue', fg='white')
#Side = LEFT confines the label to the LHS of frame/window
#Fill Y means that it fills the frame in Y direction
three.pack(side=LEFT, fill=Y)


#Keeps the program running 
root.mainloop()