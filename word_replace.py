# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 10:00:59 2020

@author: mitan
"""

import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import filedialog
from tkinter import ttk
import os
import shutil

if __name__ == '__main__':
    
    win = tk.Tk()
    win.title("Replace Words")
    win.geometry("700x350")
    
    num = 0
    
    
    def dir_click():
        dir = 'C:\\pg'
        fld = filedialog.askdirectory(initialdir = dir) 
        pass_t.insert(tk.END,str(fld))
    
    row = 10
    pass_l = tk.Label(win,text='フォルダパス')
    pass_l.place(x=30,y=row+20*2)
    pass_t = tk.Entry(win,width=50)
    pass_t.place(x=30+100,y=row+20*2)
    okButton = tk.Button(win,text='Folder',command=dir_click)
    okButton.place(x=30+100+350,y=row+20*2)
    
    row = 40
    cb_l = tk.Label(win,text='File Version')
    cb_l.place(x=30,y=5)
    v1 = StringVar()
    cb = ttk.Combobox(win, textvariable=v1,width=10)
    cb.bind('<<ComboboxSelected>>')
    
    cb['values']=('.xlsx', '.c', '.py', '.txt')
    cb.set(".c")
    cb.place(x=30+100,y=5) 

#    label = tk.Label(win,text='サブフォルダ')
#    label.place(x=130+100,y=5)
#    bln = tk.BooleanVar()
#    chk = tk.Checkbutton(win,variable=bln)
#    chk.place(x=130+175,y=5)

    
    label_b = ["","","","",""]
    text_b = ["","","","",""]
    label_a = ["","","","",""]
    text_a = ["","","","",""]
        
    for i in range(5):
        label_b[i] = tk.Label(win,text='置換前文字'+str(i))
        label_b[i].place(x=30,y=row+20*2*(i+1))
        text_b[i]  = tk.Entry(win,width=25)
        text_b[i].place(x=30+100,y=row+20*2*(i+1))
        label_a[i] = tk.Label(win,text='置換後文字'+str(i))
        label_a[i].place(x=130+200,y=row+20*2*(i+1))
        text_a[i]  = tk.Entry(win,width=25)
        text_a[i].place(x=130+100+200,y=row+20*2*(i+1))    
       


    def ok_click():
        out = None
        def destroy():
            out.destroy()

        data_dir_path = pass_t.get()
        file_list = os.listdir(pass_t.get()+"/")
        for file_name in file_list:
            root, ext = os.path.splitext(file_name)
            if ext == cb.get():
                abs_name = data_dir_path + '/' + file_name  
                print(abs_name)
                with open(abs_name, encoding='utf-8') as f:
                    data_lines = f.read()
                for i in range(5):      
                    data_lines = data_lines.replace(str(text_b[i].get()),str(text_a[i].get()))
                    with open(abs_name, mode="w", encoding='utf-8') as f:
                        f.write(data_lines)
                   


        out = tk.Tk()
        out.title("")
        out.geometry("200x50")    

        outButton = tk.Button(out,text='Succes Replace Words',command=destroy)
        outButton.pack()

        
    okButton = tk.Button(win,text='Replace Words',command=ok_click)
    okButton.place(x=300,y=300)
    
    win.mainloop()
