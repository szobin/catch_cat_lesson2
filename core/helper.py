import os
from PIL import Image, ImageTk

from .conf import MX, MY, PX, PY, N_ROWS, N_COLS, CW, CH, TRANSPARENT_COLOR

CW2 = CW // 2
CH2 = 3 * CH // 5
CW3 = CW // 3
CH3 = CH // 3


def get_x(cx, cy):
    dx = MX + CW // 2 if cy % 2 == 0 else MX + CW + 2
    return dx + (CW + PX) * cx


def get_y(cy):
    dy = MY + CH // 2
    return dy + (CH + PY) * cy


def make_hexagons():
    cells = []
    y = MY + CH // 2
    for i in range(N_ROWS):
        x = MX + CW // 2 if i % 2 == 0 else MX + CW + 2
        for j in range(N_COLS):
            cells.append({'x': j, 'y': i, 'selected': False,
                          'points': (x, y+CH2, x+CW2, y+CH3,
                                     x + CW2, y - CH3, x, y - CH2,
                                     x - CW2, y - CH3, x - CW2, y + CH3)})
            x += CW + PX
        y += CH + PY
    return cells


def load_transparent_image(fn, transparent_color):
    alpha_color = transparent_color + (0,)

    img = Image.open(fn).convert("RGBA")
    new_data = [alpha_color if px[:3] == transparent_color else px for px in img.getdata()]
    img.putdata(new_data)
    return ImageTk.PhotoImage(img)


def get_image(fn):
    if not os.path.isfile(fn):
        return None
    return load_transparent_image(fn, TRANSPARENT_COLOR)


# def move_pos(p, d):
