#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:53:17 2019

@author: ellis
"""

from tkinter import *
import tkinter.messagebox


root = Tk()

#Canvas needed to draw shapes

canvas = Canvas(root, width=200, height=100)
canvas.pack() 

blackLine = canvas.create_line(0,0,100, 50)
redLine = canvas.create_line(0, 100, 100,50, fill='red')
greenBox = canvas.create_rectangle(25,25, 75,75, fill='green')


canvas.delete(redLine)

root.mainloop()