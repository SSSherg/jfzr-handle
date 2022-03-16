from util.find_picture_color import picture_son_for_parent
from util.mouse_operation import left_click


def login(hwnd, full_name):
    temp = True
    move_count = 0
    while temp:
        x, y = picture_son_for_parent(hwnd, full_name, 0.8, (0, 0, 0, 0))
        if x > 0 & y > 0:
            left_click(hwnd, (x, y))
