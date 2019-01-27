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

def resetPainting():
    pass

master = Tk()
master.title("DuoLine")

frame = Frame()
drawing_frame = (frame)
drawing_frame.place(x=3, y=30)

w = Canvas(master,
           height = canvas_height,
           width = canvas_width)
w.pack(expand = YES, fill = BOTH)
w.bind( "<B1-Motion>", paint )

btn_reset = Button(w, text="Reset", command=resetPainting())
btn_reset.place(x=5, y=2)

#draw_area = w.create_window(3, 30, height=canvas_height, width=canvas_width, anchor="nw")
w.create_text(550, 15, text='DuoLine')
w.create_rectangle(3, 30, canvas_width, canvas_height, fill="#ffffff")

mainloop()

#TODO: Make function for making lines
#TODO: Make a maximum of two lines before changing "player"