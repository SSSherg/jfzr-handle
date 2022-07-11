# -*- coding: utf-8 -*-
from src.city.exit import back_city, back_change_role
from src.instance_zones.cangqiong.cq_public_method import cq_zones_left_two, cq_left_to_right, cq_zones_right_two
from src.instance_zones.public_method import zones_one, is_boss, is_boss_over, sell_page, loop_map, is_frequency_over, \
    decompose, is_no_pilao
from util.keyboard_operation import key_press, key_down, key_up
from util.log import log
from util.mouse_operation import left_click
from util.utils import delay
from util.window import findHwnd


def nvwang(hwnd):
    while True:
        if not zones_one(hwnd):
            return False  # 没进一图
        key_press(hwnd, "f2")  # 开鞋子加速
        key_down(hwnd, "A")  # 往前走一点
        delay(250)
        key_up(hwnd, "A")
        key_down(hwnd, "W")  # 往前走一点
        delay(300)
        key_up(hwnd, "W")
        key_press(hwnd, "E")    # 位移到怪堆
        delay(500)
        key_press(hwnd, "6")    # 宠物技能吸怪打怪
        delay(5000)
        key_down(hwnd, "W")     # 往前走顺便按F
        key_down(hwnd, "F")
        delay(600)
        key_up(hwnd, "F")
        key_up(hwnd, "W")
        if not is_boss(hwnd):
            return False  # 没进BOSS图
        delay(200)
        key_press(hwnd, "numpad1")   # 小键盘1号键，天界头
        delay(1300)
        if not is_boss_over(hwnd):
            return False  # boss没打死
        key_down(hwnd, "W")  # 往前走捡东西
        delay(1000)
        key_up(hwnd, "W")
        loop_map(hwnd)  # 循环开图
        delay(1200)
        if is_no_pilao(hwnd):
            delay(200)
            key_press(hwnd, "enter")
            delay(200)
            back_city(hwnd)  # 回城
            back_change_role(hwnd)  # 回选择角色界面
            return True


if __name__ == '__main__':
    hwnd = findHwnd("JFZR")
    nvwang(hwnd)
