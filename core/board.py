from .helper import make_hexagons


class Board:

    def __init__(self, canvas):
        self.canvas = canvas
        self.cells = make_hexagons()

    def draw_cell(self, points, color):
        return self.canvas.create_polygon(points, fill=color,
                                          outline="OliveDrab4", tag="cell")

    def change_by(self, cell_id):
        self.canvas.delete(cell_id)

    def draw(self):
        for cell in self.cells:
            points = cell["points"]
            self.draw_cell(points, "OliveDrab1")
