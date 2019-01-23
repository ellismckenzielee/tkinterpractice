#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:53:17 2019

@author: ellis
"""

from tkinter import *

def doNothing():
    print('ok ok I won\'t')

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='New Project', command=doNothing)
subMenu.add_command(label='New Window', command=doNothing)
subMenu.add_separator()
subMenu.add_command(label='Open File', command=doNothing)
subMenu.add_separator()
subMenu.add_command(label='Exit', command=root.destroy)

editMenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Undo', command=doNothing)
editMenu.add_command(label='Redo', command=doNothing)


root.mainloop()