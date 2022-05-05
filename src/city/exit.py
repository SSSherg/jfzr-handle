# -*- coding: utf-8 -*-
import sys
import time

from util.date_utils import getTimeStr
from util.find_picture_color import picture_son_for_parent, capture_the_current_window_screen
from util.ini_file_operation import readIni
from util.keyboard_operation import key_up, key_down, key_press
from util.log import log
from util.mouse_operation import left_click
from util.utils import delay
from util.window import findHwnd


# 返回城镇
def back_city(hwnd):
    delay(200)
    key_press(hwnd, "esc")
    delay(200)
    count = 0
    while True:
        x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/cityAndPage/back_city.bmp", 0.9,
                                      (1083, 321, 1264, 472))
        if x > 0 and y > 0:
            delay(500)
            left_click(hwnd, (x, y))
            delay(500)
            key_press(hwnd, "enter")
            delay(1200)
            return True
        else:
            key_press(hwnd, "esc")
            delay(500)
            count = count + 1
            if count > 30:
                key_down(hwnd, "S")
                delay(1000)
                key_up(hwnd, "S")
            if count > 25:
                log.info("找不到返回城镇")
                capture_the_current_window_screen(hwnd, getTimeStr(time.time()) + readIni("name") + "-back_city.bmp")
                count = 0


# 返回频道
def back_pindao(hwnd):
    delay(200)
    key_press(hwnd, "esc")
    delay(200)
    count = 0
    while True:
        x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/cityAndPage/back_pindao.bmp", 0.9,
                                      (1102, 412, 1252, 451))
        if x > 0 and y > 0:
            left_click(hwnd, (x, y))
            delay(500)
            key_press(hwnd, "enter")
            delay(1200)
            return True
        else:
            key_press(hwnd, "esc")
            delay(500)
            count = count + 1
            if count > 10:
                key_down(hwnd, "S")
                delay(1000)
                key_up(hwnd, "S")
            if count > 15:
                log.info("找不到返回频道")
                capture_the_current_window_screen(hwnd, getTimeStr(time.time()) + readIni("name") + "-back_pindao.bmp")
                count = 0


# 退出到角色页面
def back_change_role(hwnd):
    delay(200)
    key_press(hwnd, "esc")
    delay(200)
    count = 0
    while True:
        x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/cityAndPage/change_role.bmp", 0.9,
                                      (1099, 441, 1255, 483))
        if x > 0 and y > 0:
            left_click(hwnd, (x, y))
            delay(500)
            key_press(hwnd, "enter")
            delay(1200)
            return True
        else:
            key_press(hwnd, "esc")
            delay(500)
            count = count + 1
            if count > 20:
                key_down(hwnd, "S")
                delay(1000)
                key_up(hwnd, "S")
            if count > 25:
                log.info("找不到返回角色页面")
                capture_the_current_window_screen(hwnd, getTimeStr(time.time()) + readIni("name") + "-back_change_role.bmp")
                count = 0


if __name__ == '__main__':
    hwnd = findHwnd("钉钉")
    capture_the_current_window_screen(hwnd, getTimeStr(time.time()) + readIni("name") + "-is_boss_over.bmp")