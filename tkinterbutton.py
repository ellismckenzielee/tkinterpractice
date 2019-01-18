#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 13:17:23 2019

@author: ellis
"""

from tkinter import *
from tkinter import ttk


COLOR1 = 'Blue'
COLOR2 = 'Red'
COLOR3 = 'Gold'
 
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title('Tkinter Radio Button')
        self.minsize(640, 400)
        self.configure(background='white')
        self.radioButton()
    
    def radioEvent(self):
        radSelected = self.radValues.get()
        
        if radSelected == 1:
            self.configure(background = COLOR1)
        elif radSelected == 2:
            self.configure(background = COLOR2)
        elif radSelected == 3:
            self.configure(background = COLOR3)
        
    def radioButton(self):
        self.radValues = IntVar()
        self.rad1 = ttk.Radiobutton(self, text=COLOR1, value=1, variable = self.radValues, command = self.radioEvent)
        self.rad1.grid(column=0,row=0, sticky=W, columnspan = 3)
        self.rad2 = ttk.Radiobutton(self, text=COLOR2, value=2, variable = self.radValues, command = self.radioEvent)
        self.rad2.grid(column=0,row=1, sticky=W, columnspan = 3)
        self.rad3 = ttk.Radiobutton(self, text=COLOR3, value=3, variable = self.radValues, command = self.radioEvent)
        self.rad3.grid(column=0,row=2, sticky=W, columnspan = 3)
        
root = Root()
root.mainloop()
