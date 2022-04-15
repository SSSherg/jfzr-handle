# -*- coding: utf-8 -*-
import sys

from src.city.exit import back_city, back_change_role
from util.find_picture_color import picture_son_for_parent, colors_son_for_parent

# 判断是否次数用尽，true为没次数了，
from util.keyboard_operation import key_down, key_up, key_press
from util.log import log
from util.mouse_operation import scroll, left_click, move_to, left_double_click
from util.utils import delay
from util.window import findHwnd


def is_frequency_over(hwnd):
    x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/instance_zones/frequency_over.bmp", 0.9,
                                  (552, 343, 1058, 516))
    if x > 0 and y > 0:
        return True
    else:
        return False


# 判断boss结束,true为结束
def is_boss_over(hwnd):
    count = 0
    while True:
        x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/instance_zones/boss_over.bmp", 0.9,
                                      (1432, 0, 1560, 135))
        if x > 0 and y > 0:
            key_press(hwnd, "esc")
            delay(200)
            return True
        else:
            delay(500)
            count = count + 1
            if count > 30:
                log.info("没打死boss重启")
                back_city(hwnd)
                back_change_role(hwnd)
                return False


# 循环开图
def loop_map(hwnd):
    count = 0
    while True:
        x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/instance_zones/F4.bmp", 0.9,
                                      (757, 10, 1108, 135))
        if x > 0 and y > 0:
            key_down(hwnd, "f1")
            delay(200)
            key_down(hwnd, "f4")
            return True
        else:
            key_down(hwnd, "esc")
            delay(500)
            count = count + 1
            if count > 20:
                log.info("循环开图错误重启")
                back_city(hwnd)
                back_change_role(hwnd)
                return False


# 判断一图 根据左下方血量找色
def zones_one(hwnd):
    count = 0
    while True:
        x, y = colors_son_for_parent(hwnd, [(255, 0, 0)], 0.9, (398, 781, 452, 840))
        if x > 0 and y > 0:
            for i in range(5):
                scroll(hwnd, -120, (50, 50))
                delay(200)
            return True
        else:
            delay(200)
            count = count + 1
            if count > 50:
                log.info("没进一图重启")
                back_change_role(hwnd)
                return False


# 判断boss图
def is_boss(hwnd):
    count = 0
    while True:
        x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/instance_zones/boss.bmp", 0.9,
                                      (430, 40, 1130, 100))
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
                log.info("没进boss图重启")
                back_city(hwnd)
                back_change_role(hwnd)
                return False


# 卖装备页面
def sell_page(hwnd):
    is_sale = False  # false为不需要卖
    count = 0
    while True:
        delay(200)
        key_press(hwnd, "6")
        delay(200)
        key_press(hwnd, "F")
        delay(600)
        left_double_click(hwnd, (1285, 864))  # 商店按钮
        delay(400)
        left_double_click(hwnd, (1251, 161))  # 角色栏
        delay(400)
        left_double_click(hwnd, (1239, 423))  # 装备栏
        delay(400)
        left_double_click(hwnd, (593, 313))  # 出售栏 点一下会有bug(失效)
        delay(400)
        # 判断装备栏
        x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/instance_zones/is_zb_lan.bmp", 0.9,
                                      (1200, 389, 1269, 460))
        if x > 0 and y > 0:
            is_sale = True
            break
        else:
            delay(400)
            count = count + 1
            if count > 1:  # 重复2次就是没装备
                log.info("没装备卖")
                break
    if is_sale:
        # 先判断初级装备
        x, y = colors_son_for_parent(hwnd, [(84, 90, 169)], 0.9, (695, 619, 722, 647))
        if x > 0 and y > 0:
            delay(400)
            left_click(hwnd, (710, 633))  # 初级装备勾选栏
            delay(400)
            if not sell(hwnd):     # 会出现失效问题
                left_click(hwnd, (710, 633))  # 初级装备勾选栏
                delay(400)
                sell(hwnd)
            delay(1000)
        # 先判断中级装备
        x, y = colors_son_for_parent(hwnd, [(84, 90, 169)], 0.9, (790, 619, 822, 647))
        if x > 0 and y > 0:
            delay(400)
            left_click(hwnd, (809, 633))  # 中级装备勾选栏
            delay(400)
            if not sell(hwnd):
                left_click(hwnd, (809, 633))  # 中级装备勾选栏
                delay(400)
            delay(1500)
        # 先判断高级装备
        x, y = colors_son_for_parent(hwnd, [(84, 90, 169)], 0.9, (887, 619, 927, 647))
        if x > 0 and y > 0:
            delay(400)
            left_click(hwnd, (906, 633))  # 高级装备勾选栏
            delay(400)
            if not sell(hwnd):
                left_click(hwnd, (906, 633))  # 高级装备勾选栏
                delay(400)
            delay(1000)
        key_press(hwnd, "esc")
        delay(400)
        key_press(hwnd, "esc")
        delay(400)


# 出售
def sell(hwnd):
    count = 0
    while True:
        x, y = colors_son_for_parent(hwnd, [(221, 221, 223)], 0.9, (800, 682, 1000, 721))
        if x > 0 and y > 0:
            delay(300)
            left_click(hwnd, (x, y))
            return True
        else:
            delay(500)
            count = count + 1
            if count > 5:
                return False


# 分解
def decompose(hwnd):
    delay(200)
    key_press(hwnd, "6")
    delay(200)
    key_press(hwnd, "F")
    delay(400)
    left_click(hwnd, (1400, 864))
    delay(1500)
    left_click(hwnd, (633, 353))
    delay(2500)
    key_press(hwnd, "enter")
    delay(150)
    key_press(hwnd, "enter")
    delay(150)
    key_press(hwnd, "enter")
    delay(2500)
    key_press(hwnd, "enter")
    log.info("分解完毕")


if __name__ == '__main__':
    hwnd = findHwnd("JFZR")
    # sell_page(hwnd)  # 卖东西
    # loop_map(hwnd)  # 循环开图
    # move_to(hwnd,(410, 460))
    while True:
        delay(200)
        key_press(hwnd, "6")
        delay(200)
        key_press(hwnd, "F")
        delay(600)
        left_click(hwnd, (1285, 864))  # 商店按钮
        delay(400)
        left_click(hwnd, (1251, 161))  # 角色栏
        delay(400)
        left_click(hwnd, (1239, 423))  # 装备栏
        delay(400)
        left_click(hwnd, (593, 313))  # 出售栏 点一下会有bug(失效)
        delay(1000)
        key_press(hwnd, "esc")
        delay(400)
        key_press(hwnd, "esc")

