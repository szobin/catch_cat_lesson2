import tkinter as tk
import sched as sd
import time as tm

from .conf import W, H, BG_COLOR
from .board import Board
from .figure import Figure


class App:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Catch the cat")
        self.scheduler = sd.scheduler(tm.time, tm.sleep)
        self.canvas = tk.Canvas(self.window, width=W, height=H, bg=BG_COLOR)
        self.canvas.pack()

        self.board = Board(self.canvas)
        self.figure = Figure(self.canvas, self.board)
        self.canvas.tag_bind("cell", '<ButtonPress-1>', self.on_click)

    def on_click(self, event):
        cell_id = event.widget.find_closest(event.x, event.y)
        if len(cell_id) > 0:
            self.board.change_by(cell_id[0])

    def run(self):
        self.board.draw()
        self.figure.draw()
        self.window.mainloop()
