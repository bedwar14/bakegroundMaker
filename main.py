import tkinter as tk
from tkinter.ttk import Entry
import requests
from PIL import Image
from PIL import ImageTk
import bakegroundMaker
import os

HEIGHT = 800
WIDTH = 1000

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
gen = bakegroundMaker.GradGen()
bakegrounddata = gen.Generate()
background_image = tk.PhotoImage(data=bakegrounddata)#file='C:\\dev\\python\\landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

root.mainloop()
