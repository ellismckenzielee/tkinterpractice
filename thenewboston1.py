#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:53:17 2019

@author: ellis
"""

from tkinter import *
import tkinter.messagebox


root = Tk()

photo  = PhotoImage(file='giphy.gif')
label = Label(root, image=photo)
label.pack()

root.mainloop()