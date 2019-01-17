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
        self.initUI()
        
    def clickMe(self):
        self.label.configure(text='Hello' + self.name.get())
        self.label.configure(foreground = 'green')
        
        
        
    def initUI(self):
        self.name = StringVar()
        self.label = Label(self, text = 'Enter your name')
        self.label.grid(column=0, row=0)
        self.textbox = Entry(self, width=20, textvariable = self.name)
        self.textbox.grid(column=0,row=1)
        self.button = Button(self, text='Submit', command = self.clickMe)
        self.button.grid(column=0,row=2)
root = Root()
root.mainloop()
