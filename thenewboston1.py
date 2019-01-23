#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:53:17 2019

@author: ellis
"""

from tkinter import *


#Create a class that has main functionality 
#Master is the main window 
class usingClasses:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.printButton = Button(frame, text='Print Message', command= self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text='Quit', command=master.destroy)
        self.quitButton.pack(side=RIGHT)

    def printMessage(self):
        print('This is the message')

#Keeps the program running 
root = Tk()
main = usingClasses(root)
root.mainloop()
