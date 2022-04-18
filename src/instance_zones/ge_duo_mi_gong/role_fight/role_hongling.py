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


def hongling(hwnd):
    while True:
        if not zones_one(hwnd):
            return False  # 没进一图
        discount = 0
        count = 0
        temp = True
        while temp:
            if discount == 0:
                key_down(hwnd, "W")
                delay(100)
                for i in range(4):
                    left_click(hwnd, (50, 50))
                    delay(500)
            else:
                key_down(hwnd, "S")
                delay(100)
                for i in range(2):
                    left_click(hwnd, (50, 50))
                    delay(500)
            if discount == 0:
                key_up(hwnd, "W")
                discount = 1
            else:
                key_up(hwnd, "S")
                discount = 0
            count = count + 1
            if count > 16:
                if is_boss_over(hwnd):
                    count = 0
                    temp = False
                    key_up(hwnd, "W")
                    key_up(hwnd, "S")
        loop_map(hwnd)
        delay(1000)
        if is_frequency_over(hwnd):
            delay(200)
            key_press(hwnd, "enter")
            delay(200)
            back_city(hwnd)  # 回城
            back_change_role(hwnd)  # 会选择角色界面
            return True


if __name__ == '__main__':
    hwnd = findHwnd("JFZR")
    hongling(hwnd)
