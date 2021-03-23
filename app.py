import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import numpy as np
from tkinter import filedialog, Text
import os
from datetime import datetime

root = tk.Tk() 
root.title("Renamer")
style = ttk.Style()

fileNames = []

def addFiles():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilenames(initialdir="/", 
                                            title="Select File",
                                            ) 

    filename = np.asarray(filename)
    
    for fname in filename:
        fileNames.append(fname)
        style.configure("BW.TLabel", foreground="#050505", background="#c0c0c0", padding=8, font='Arial 11 bold')
        label = ttk.Label(frame, text=fname, style="BW.TLabel")
        label.pack()

def renameFiles():
    fileNames.sort(key=os.path.getctime)
    counter = 1
    for fname in fileNames:
        target_extension = os.path.splitext(fname)[1]
        os.rename(fname, str(counter) + target_extension)
        counter += 1
        
canvas = tk.Canvas(root, height=400, width=500, bg="white") 
canvas.pack() 

frame = tk.Frame(root, bg="#C0C0C0") 
frame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.1) 

openFile = tk.Button(root, 
                     text="Select Files", 
                     padx=10, 
                     pady=5, 
                     width= 20,
                     fg="white", 
                     bg="#004E98", 
                     highlightbackground="blue",
                     command=addFiles)
    
openFile.pack()

runApps = tk.Button(root, 
                    text="Rename Files", 
                    padx=10, 
                    pady=5,
                    width=20,
                    fg="white", 
                    bg="#004E98",                     
                    command=renameFiles)
runApps.pack()

root.mainloop() 
