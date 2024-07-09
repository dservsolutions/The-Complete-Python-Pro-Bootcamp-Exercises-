import tkinter
import tkinter as tk
from functions import load_image, add_watermark
from tkinter import filedialog, StringVar, Message, RAISED
from PIL import Image, ImageTk, ImageDraw, ImageFont

window = tk.Tk()
window.title("Image Watermark App")
window.minsize(width=1024, height=768)
# window.config(padx=400, pady=300)

# Widgets
label_title = tkinter.Label(text="Please Load a Photo Image: ", font=("Verdana", 20, "bold"))
# label.grid(column=2, row=0)
label_title.pack()

load_btn = tkinter.Button(text="LOAD", command=load_image)
add_watermark_btn = tkinter.Button(text="Add Watermark", command=add_watermark)
# load_btn.grid(column=0, row=1)
load_btn.pack()
# add_watermark_btn.grid(column=1, row=1)
add_watermark_btn.pack()
text_box = tkinter.Entry(window)
text_box.pack()
label_info = tkinter.Label(text="")

window.mainloop()
