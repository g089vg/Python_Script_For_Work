# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 23:15:50 2020

@author: mitan
"""


import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

from def_comp_excel_20200131 import compar_excel_file2

if __name__ == '__main__':
    
    win = tk.Tk()
    win.title("Replace Words")
    win.geometry("700x200")
    num = 0
      
    
    def dir_click1():
        fTyp = [("","*")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        file1 = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
        pass_t1.insert(tk.END,str(file1))
        
    row = 10
    pass_l1 = tk.Label(win,text='ファイル1(後)')
    pass_l1.place(x=30,y=row+20*2)
    pass_t1 = tk.Entry(win,width=50)
    pass_t1.place(x=30+100,y=row+20*2)
    okButton1 = tk.Button(win,text='Folder',command=dir_click1)
    okButton1.place(x=30+100+350,y=row+20*2)


    def dir_click2():
        fTyp = [("","*")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        file2 = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
        pass_t2.insert(tk.END,str(file2))
        
    a = 30
    row = 10+a
    pass_l2 = tk.Label(win,text='ファイル2(前)')
    pass_l2.place(x=30,y=row+20*2+a)
    pass_t2 = tk.Entry(win,width=50)
    pass_t2.place(x=30+100,y=row+20*2+a)
    okButton2 = tk.Button(win,text='Folder',command=dir_click2)
    okButton2.place(x=30+100+350,y=row+20*2+a)

    
    row = 40
    cb_l = tk.Label(win,text='2つのファイルを比較します．新規追加・削除された行をピックアップします．')
    cb_l.place(x=30,y=5)
#    v1 = StringVar()
    cb = ttk.Combobox(win,width=10)
    cb.bind('<<ComboboxSelected>>')



    row = 80
    cb_l = tk.Label(win,text='同値が予想されるCell数（変更箇所判定に使用）')
    cb_l.place(x=430,y=5)
    cb = ttk.Combobox(win,width=10)
    cb.bind('<<ComboboxSelected>>')
    
    cb['values']=('1','2', '3', '4', '5','6','7', '8', '9', '10')
    cb.set("0")
    cb.place(x=500+100,y=5+25) 

    

    def ok_click():
        out = None
        def destroy():
            out.destroy()

        compar_excel_file2(int(cb.get()),pass_t1.get(),pass_t2.get())


        out = tk.Tk()
        out.title("")
        out.geometry("200x50")    
        outButton = tk.Button(out,text='Succes Replace Words',command=destroy)
        outButton.pack()

        
    okButton = tk.Button(win,text='Compare Excel Files',command=ok_click)
    okButton.place(x=300,y=170)
    win.mainloop()
