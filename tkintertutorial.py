#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:45:23 2019

@author: ellis
"""

from tkinter import *
def click():
    entered_text=textentry.get()
    output.delete(0.0, END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = 'sorry no definition!'
    output.insert(END, definition)
    
def close_window():
    window.destroy()
    exit()
##main
window = Tk()
window.title('Graphite Segmentation')
window.configure(background='black')

#Photo
photo1 = PhotoImage(file='giphy.gif')
Label (window, image=photo1, bg='black') .grid(row=0, column=0, sticky=E)

#create Label
Label(window, text='Enter the work you would like a definition for:', bg='black',fg='white', font='none 12 bold').grid(row=1, column=0, sticky=W)

#create textentry box
textentry = Entry(window, width=20,bg='white')
textentry.grid(row=2,column=0,sticky=W)

#create submit button
Button(window, text='SUBMIT', width=6, command=click).grid(row=3,column=0,sticky=W)

#create another label
Label(window,text='\nDefinition:', bg='black', fg='white', font='none 12 bold').grid(row=4, column=0, sticky=W)

#create an output text box
output = Text(window, width=75, height=6, wrap=WORD, background='white')
output.grid(row=5, column=0, columnspan=2, sticky=W)

#the dictionary
my_compdictionary = {
        'algorithm': 'Step by step instructions to complete a task', 'bug': 'piece of code that causes a program to fail'
        }

#exit label
Label(window, text='click to exit', bg='black', fg='white',font='none 12 bold').grid(row=6, column=0, sticky=W)
Button(window, text='Exit', width=14, command=close_window).grid(row=7, column=0, sticky=E)

#mainloop
window.mainloop()