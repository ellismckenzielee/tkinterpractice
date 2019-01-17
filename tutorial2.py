#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 11:46:05 2019

@author: ellis
"""

from tkinter import *

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title('NGRG Graphite Segmentation')
        self.minsize(640, 400)
        self.configure(background='white')
        self.createWidget()
        
    def createWidget(self):
        label = Label(self, text='Pack Geometry')
        label.grid(column=0,row=0)
        label2 = Label(self, text='Pack Geometry2')
        label2.grid(column=0,row=1)
        label3 = Label(self, text='Pack 3')
        label3.grid(column=0,row=2)

root = Root()
root.mainloop()
