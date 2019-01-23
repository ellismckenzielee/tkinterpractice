#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:53:17 2019

@author: ellis
"""

from tkinter import *

#Creating a blank window, which is equal to root
root = Tk()

def leftClick(event):
    print('LEFT')

def middleClick(event):
    print('MIDDLE')

def rightClick(event):
    print('RIGHT')


#Add a frame
frame = Frame(root, width=300, height=250)
frame.bind('<Button-1>', leftClick)
frame.bind('<Button-2>', middleClick)
frame.bind('<Button-3>', rightClick)
frame.pack()


#Keeps the program running 
root.mainloop()

