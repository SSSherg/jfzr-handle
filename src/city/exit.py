# -*- coding: utf-8 -*-
import sys

from util.find_picture_color import picture_son_for_parent
from util.keyboard_operation import key_up, key_down, key_press
from util.log import log
from util.mouse_operation import left_click
from util.utils import delay
from util.window import findHwnd


def back_city(hwnd):
    delay(200)
    key_press(hwnd, "esc")
    delay(200)
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
            # log.info("找不到返回城镇")
            key_press(hwnd, "esc")
            delay(500)


# 返回频道
def back_pindao(hwnd):
    delay(200)
    key_press(hwnd, "esc")
    delay(200)
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
            # log.info("找不到返回频道")
            key_press(hwnd, "esc")
            delay(500)


# 退出到角色页面
def back_change_role(hwnd):
    delay(200)
    key_press(hwnd, "esc")
    delay(200)
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
            # log.info("找不到返回角色页面")
            key_press(hwnd, "esc")
            delay(500)


# 传入1去正常频道，其他为特殊频道
def enter_pindao(hwnd, change):
    x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/cityAndPage/pindao_button.bmp", 0.9,
                                  (1365, 761, 1510, 813))
    if x > 0 and y > 0:
        if change == "1":
            left_click(hwnd, (x, y))
            delay(5000)
        else:
            left_click(hwnd, (x, y - 100))
            delay(500)
            key_press(hwnd, "enter")
    else:
        log.info("没到选择频道页面")


if __name__ == '__main__':
    hwnd = findHwnd("JFZR")
    back_city(hwnd)