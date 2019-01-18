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
        self.title('Combobox')
        self.minsize(640, 400)
        self.configure(background='white')
        self.initUI()
    
    def clickMe(self):
        self.label.configure(text='you have selected' + self.myfruit.get())
    def initUI(self):
        self.myfruit = StringVar()
        self.combo = ttk.Combobox(self, width = 15, textvariable = self.myfruit)
        self.combo['values'] = ('Apple', 'Pear')
        self.combo.grid(column = 1,row = 1)
        self.label = ttk.Label(self, text='select fruit')
        self.label.grid(column=5, row = 5)
        self.button = ttk.Button(self, text = 'click', command = self.clickMe)
        self.button.grid(column=2, row = 1)
        
root = Root()
root.mainloop()
