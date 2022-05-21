# -*- coding: utf-8 -*-
from src.city.exit import back_city, back_change_role
from src.instance_zones.cangqiong.cq_public_method import cq_zones_left_two, cq_left_to_right, cq_zones_right_two
from src.instance_zones.public_method import zones_one, is_boss, is_boss_over, sell_page, loop_map, is_frequency_over, \
    decompose
from util.keyboard_operation import key_press, key_down, key_up
from util.log import log
from util.mouse_operation import left_click
from util.utils import delay
from util.window import findHwnd


def nvwang(hwnd):
    while True:
        if not zones_one(hwnd):
            return False  # 没进一图
        key_press(hwnd, "f2")
        key_press(hwnd, "numpad1")
        delay(2600)
        key_down(hwnd, "W")
        key_down(hwnd, "F")
        delay(600)
        key_up(hwnd, "F")
        key_up(hwnd, "W")
        delay(500)
        key_down(hwnd, "W")
        key_down(hwnd, "F")
        delay(600)
        key_up(hwnd, "F")
        key_up(hwnd, "W")
        if not is_boss(hwnd):
            return False  # 没进BOSS图
        delay(200)
        key_down(hwnd, "A")
        delay(50)
        key_up(hwnd, "A")
        key_down(hwnd, "W")
        delay(300)
        key_up(hwnd, "W")
        key_press(hwnd, "E")
        delay(1300)
        if not is_boss_over(hwnd):
            return False  # boss没打死
        loop_map(hwnd)  # 循环开图
        delay(1500)


if __name__ == '__main__':
    hwnd = findHwnd("JFZR")
    nvwang(hwnd)
