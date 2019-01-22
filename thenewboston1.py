#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:53:17 2019

@author: ellis
"""

from tkinter import *

#Creating a blank window, which is equal to root
root = Tk()

#AddLabels
theLabel = Label(root, text='This is a label')
theLabel.pack()

#Keeps the program running 
root.mainloop()