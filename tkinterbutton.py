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
        self.checkButton()

    def checkButton(self):
        self.check1 = ttk.Checkbutton(self, text='Disabled', state='disabled')
        self.check1.grid(column=0,row=0, sticky = W)
        self.check2 = ttk.Checkbutton(self, text = 'unchecked')
        self.check2.grid(row=0, column=1)
        self.check3 = ttk.Checkbutton(self, text = 'enabled', state='enabled')
        self.check3.grid(column = 3 , row = 1)
root = Root()
root.mainloop()
