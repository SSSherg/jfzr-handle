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


def mingzun(hwnd, into_result):
    if into_result == "left":
        while True:
            if not zones_one(hwnd):
                return False    # 没进一图
            key_press(hwnd, "f2")
            key_down(hwnd, "W")
            delay(700)
            key_up(hwnd, "W")
            key_press(hwnd, "numpad1")
            delay(2200)
            key_down(hwnd, "D")
            delay(2500)
            key_up(hwnd, "D")
            delay(200)
            key_down(hwnd, "W")
            delay(1700)
            key_up(hwnd, "W")
            if not cq_zones_left_two(hwnd):
                return False    # 没进二图
            key_down(hwnd, "W")
            delay(700)
            key_up(hwnd, "W")
            key_press(hwnd, "alt")
            delay(3000)
            key_down(hwnd, "W")
            key_down(hwnd, "F")
            delay(500)
            key_up(hwnd, "F")
            key_up(hwnd, "W")
            key_down(hwnd, "D")
            delay(1400)
            key_up(hwnd, "D")
            if not is_boss(hwnd):
                return False    # 没进BOSS图
            delay(200)
            key_down(hwnd, "W")
            delay(500)
            key_up(hwnd, "W")
            delay(200)
            key_press(hwnd, "esc")
            delay(200)
            key_press(hwnd, "4")
            delay(1300)
            if not is_boss_over(hwnd):
                return False    # boss没打死
            key_down(hwnd, "W")
            delay(800)
            key_up(hwnd, "W")
            sell_page(hwnd)  # 卖东西
            loop_map(hwnd)   # 循环开图
            delay(1500)
            if is_frequency_over(hwnd):
                delay(200)
                key_press(hwnd, "enter")
                delay(200)
                key_down(hwnd, "W")   # 换右图
                delay(3000)
                key_up(hwnd, "W")
                key_down(hwnd, "D")  # 换右图
                delay(2000)
                key_up(hwnd, "D")
                key_down(hwnd, "S")  # 换右图
                delay(500)
                key_up(hwnd, "S")
                cq_left_to_right(hwnd)
                return mingzun(hwnd, "right")
    else:  # 右图
        while True:
            if not zones_one(hwnd):
                return False    # 没进一图
            key_press(hwnd, "f2")
            key_down(hwnd, "W")
            delay(2200)
            key_up(hwnd, "W")
            key_press(hwnd, "numpad1")
            delay(3800)
            key_down(hwnd, "D")
            delay(2700)
            key_up(hwnd, "D")
            delay(200)
            if not cq_zones_right_two(hwnd):
                return False    # 没进二图
            key_down(hwnd, "D")
            delay(500)
            key_up(hwnd, "D")
            key_down(hwnd, "W")
            delay(400)
            key_up(hwnd, "W")
            key_press(hwnd, "T")
            delay(4000)
            key_down(hwnd, "W")
            key_down(hwnd, "F")
            delay(1500)
            key_up(hwnd, "W")
            key_up(hwnd, "F")
            key_down(hwnd, "D")
            delay(800)
            key_up(hwnd, "D")
            if not is_boss(hwnd):
                return False    # 没进BOSS图
            delay(200)
            key_down(hwnd, "W")
            delay(500)
            key_up(hwnd, "W")
            delay(200)
            key_press(hwnd, "esc")
            delay(300)
            key_press(hwnd, "4")
            delay(4500)
            if not is_boss_over(hwnd):
                return False    # boss没打死
            key_down(hwnd, "W")
            delay(1100)
            key_up(hwnd, "W")
            sell_page(hwnd)  # 卖东西
            loop_map(hwnd)   # 循环开图
            delay(1200)
            if is_frequency_over(hwnd):
                delay(200)
                key_press(hwnd, "enter")
                delay(200)
                decompose(hwnd)  # 分解
                back_city(hwnd)  # 回城
                back_change_role(hwnd)  # 会选择角色界面
                return True



if __name__ == '__main__':
    hwnd = findHwnd("JFZR")
    key_press(hwnd, "E")
    delay(100)
    left_click(hwnd, (50, 50))
    for i in range(3):
        key_down(hwnd, "A")
        delay(400)
        key_up(hwnd, "A")
        key_down(hwnd, "D")
        delay(400)
        key_up(hwnd, "D")