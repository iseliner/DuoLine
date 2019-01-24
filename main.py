"""
The plan is to make a web game supporting multi-play, where each player puts down two lines (can expand
to more choices for amount of lines) before switching to the next player. Each player have their own
color, and together you can make pieces of art.
"""

from tkinter import *

canvas_width = 600
canvas_height = 500

def paint(event):
    python_color = "#000"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval(x1, y1, x2, y2, fill=python_color)

master = Tk()
master.title("DuoLine")

w = Canvas(master,
           height = canvas_height,
           width = canvas_width)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )

w.create_text(30,15,text='DuoLine')
w.create_rectangle(3,30,canvas_width,canvas_height, fill="#ffffff")

mainloop()