#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 13:17:23 2019

@author: ellis
"""

from tkinter import *
from tkinter import ttk

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title('Tkinter Button')
        self.minsize(640, 400)
        self.configure(background='white')
        self.label = Label(self, text = 'Hello Tkinter')
        self.label.grid(column=0, row=0)
        self.button = Button(self, text = 'Click Me', command = self.clickMe)
        self.button.grid(column=0, row=1)
    
    def clickMe(self):
        self.label.configure(text='This is the changed label')
        self.label.configure(foreground = 'green')
        
root = Root()
root.mainloop()
