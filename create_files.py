# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 20:10:51 2020

@author: mitan
"""

import tkinter as tk
from tkinter import messagebox as mbox
from tkinter import filedialog
import os


win = tk.Tk()
win.title("Create Folder")
win.geometry("800x200")

num = 0


def dir_click():
    dir = 'C:\\pg'
    fld = filedialog.askdirectory(initialdir = dir) 
    pass_t.insert(tk.END,str(fld))

row = 20
pass_l = tk.Label(win,text='フォルダパス')
pass_l.place(x=30,y=row+20*2)
pass_t = tk.Entry(win,width=50)
pass_t.place(x=30+100,y=row+20*2)
okButton = tk.Button(win,text='Folder',command=dir_click)
okButton.place(x=30+100+350,y=row+20*2)


bln = tk.BooleanVar()
row = 85

for i in range(1):
    name_l = tk.Label(win,text='フォルダ名'+str(i+1))
    name_l.place(x=30,y=row+i*25)
    name_t = tk.Entry(win,width=10)
    name_t.place(x=30+100,y=row+i*25)
    name_t.insert(tk.END,"sample")
    
    num_l = tk.Label(win,text='サブフォルダ数')
    num_l.place(x=30,y=row+25+i*25)
    num_t = tk.Entry(win,width=10)
    num_t.place(x=30+100,y=row+25+i*25)
    num_t.insert(tk.END,"0")
    name1_l = tk.Label(win,text='フォルダ名(上部)')
    name1_l.place(x=30+100+100,y=row+25+i*25)
    name1_t = tk.Entry(win,width=20)
    name1_t.place(x=230+100,y=row+25+i*25)
    name2_l = tk.Label(win,text='フォルダ名(下部)')
    name2_l.place(x=330+100,y=row+25+i*25)
    name2_t = tk.Entry(win,width=20)
    name2_t.place(x=430+100,y=row+25+i*25)
    
    chk = tk.Checkbutton(win,variable=bln)
    chk.place(x=0,y=5)
    label = tk.Label(win,text='連番を1から始める')
    label.place(x=30,y=5)




    

def ok_click():
    out = None
    new_dir_path =  pass_t.get()+'/'+name_t.get()
    def destroy():
        out.destroy()
    if not(os.path.exists(new_dir_path)):
        
        os.mkdir(new_dir_path)  
        num = 0
        if bln.get():
            num = 1
        for i in range(int(num_t.get())):
          new_dir_path = pass_t.get()+'/'+name_t.get() +'/'+name1_t.get()+str(num+i)+name2_t.get()
          os.mkdir(new_dir_path)  
          

        out = tk.Tk()
        out.title("")
        out.geometry("200x50")    
    #    out = tk.Label(out,text='Create Folder')
    #    out.pack()
        outButton = tk.Button(out,text='Create Folder',command=destroy)
        outButton.pack()
    else:
        out = tk.Tk()
        out.title("")
        out.geometry("200x100")    
        outButton = tk.Button(out,text='Error\nThis Folder is already exist',command=destroy)
        outButton.pack()  
    
    
okButton = tk.Button(win,text='Create Folder',command=ok_click)
okButton.place(x=350,y=150)

win.mainloop()
