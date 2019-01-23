#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 13:53:17 2019

@author: ellis
"""

from tkinter import *
import tkinter.messagebox


root = Tk()

tkinter.messagebox.showinfo('Window Title', 'Random Fact')

answer = tkinter.messagebox.askquestion('Question 1', 'Do you enjoy using Python?')

if answer == 'yes':
    print('User likes Python')
else:
    print('User does not like python')
    
root.mainloop()