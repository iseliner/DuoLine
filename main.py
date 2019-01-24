"""
The plan is to make a web game supporting multi-play, where each player puts down two lines (can expand
to more choices for amount of lines) before switching to the next player. Each player have their own
color, and together you can make pieces of art.
"""

from tkinter import *

master = Tk()

canvas_width = 600
canvas_height = 500

w = Canvas(master,
           height = canvas_height,
           width = canvas_width)

w.pack()

w.create_rectangle(3,30,canvas_width,canvas_height, fill="#ffffff")

w.create_text(30,
              15,
              text='DuoLine')

mainloop()