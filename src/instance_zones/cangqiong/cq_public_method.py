# -*- coding: utf-8 -*-
import time

from src.city.exit import back_city, back_change_role
from src.instance_zones.public_method import is_frequency_over
from util.date_utils import getTimeStr
from util.find_picture_color import colors_son_for_parent, capture_the_current_window_screen
from util.ini_file_operation import readIni
from util.keyboard_operation import key_up, key_down, key_press
from util.log import log
from util.mouse_operation import left_click
from util.utils import delay


# 判断苍穹左二图
def cq_zones_left_two(hwnd):
    count = 0
    while True:
        x, y = colors_son_for_parent(hwnd, [(119, 147, 76), (57, 150, 99)], 0.9, (1414, 33, 1512, 122))
        if x > 0 and y > 0:
            key_up(hwnd, "W")
            return True
        else:
            key_down(hwnd, "W")
            delay(300)
            key_up(hwnd, "W")
            delay(100)
            count = count + 1
            if count > 20:
                log.info("没进苍穹左二图重启")
                capture_the_current_window_screen(hwnd,
                                                  getTimeStr(time.time()) + readIni("name") + "-cq_zones_left_two.bmp")
                back_city(hwnd)
                back_change_role(hwnd)
                return False


# 判断苍穹右二图
def cq_zones_right_two(hwnd):
    count = 0
    while True:
        x, y = colors_son_for_parent(hwnd, [(57, 150, 99), (119, 147, 76)], 0.9, (1510, 98, 1550, 148))
        if x > 0 and y > 0:
            key_up(hwnd, "W")
            return True
        else:
            key_down(hwnd, "D")
            delay(300)
            key_up(hwnd, "D")
            delay(100)
            count = count + 1
            if count > 20:
                log.info("没进苍穹右二图重启")
                capture_the_current_window_screen(hwnd,
                                                  getTimeStr(time.time()) + readIni("name") + "-cq_zones_right_two.bmp")
                back_city(hwnd)
                back_change_role(hwnd)
                return False


#      左苍穹图内进右苍穹
def cq_left_to_right(hwnd):
    count = 0
    while True:
        delay(500)
        x, y = colors_son_for_parent(hwnd, [(150, 255, 255)], 0.9, (60, 785, 110, 851))
        if x > 0 and y > 0:
            delay(500)
            left_click(hwnd, (710, 460))  # 点右图
            delay(500)
            key_press(hwnd, "F")
            delay(500)
            key_press(hwnd, "enter")
            delay(500)
            log.info("左苍穹图内进右苍穹")
            if is_frequency_over(hwnd):
                log.info("右图没次数了")
                delay(400)
                key_press(hwnd, "enter")
                back_city(hwnd)
                back_change_role(hwnd)
                return "break"
            return True
        else:
            delay(200)
            count = count + 1
            if count > 30:
                log.info("左苍穹图内进右苍穹，没进选图界面重启")
                capture_the_current_window_screen(hwnd,
                                                  getTimeStr(time.time()) + readIni("name") + "-cq_left_to_right.bmp")
                back_city(hwnd)
                back_change_role(hwnd)
                return "reset"














if __name__ == '__main__':
    print(1)