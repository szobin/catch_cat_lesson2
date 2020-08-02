import tkinter as tk

from .helper import get_image, get_x, get_y
from .conf import INIT_POS


class Figure:

    def __init__(self, canvas, board):
        self.canvas = canvas
        self.board = board
        self.image = get_image("./images/cat_1.png")
        self.pos = INIT_POS

    def draw(self):
        self.canvas.delete("cat")
        px, py = self.pos
        x, y = get_x(px, py), get_y(py)
        self.canvas.create_image(x, y, image=self.image, anchor=tk.CENTER, tag="cat")

    # def move(self):
