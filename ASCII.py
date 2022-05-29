#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 11:29:52 2022

@author: zulkharnain
"""
from tkinter import *
 root = Tk()
 root.title("Ascii")
 
 root.geography("400x400")
 root.configure(background= 'snow')

enter_world =Enter(root)
enter_world.place(relx=0.5 rely=0.4, anchor=CENTER)

Label = Label(root, text = " Name in ASCII :", bg="Light Yellow", fg="black")

def asciiconverer():
    input_world = enter_world.get()
    
    for letter in input_world :
        label("text")+= str(ord(letter)) + "   "
        
btn=Button(root, text-"show name in ASCII", coomand=asciiconverter, bg="gold", fg="black")
btn.place(relax=0.5, rely=0.5, anchor=CENTER)

label.place(relax=0.5, rely=0.6, anchor=CENTER)

root.mainloop()





