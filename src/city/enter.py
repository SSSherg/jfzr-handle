# -*- coding: utf-8 -*-
import sys

from src.city.exit import back_change_role
from src.instance_zones.cangqiong.role_fight.role_daoshi import daoshi
from src.instance_zones.cangqiong.role_fight.role_diyue import diyue
from src.instance_zones.cangqiong.role_fight.role_fuwen import fuwen
from src.instance_zones.cangqiong.role_fight.role_hongling import hongling
from src.instance_zones.cangqiong.role_fight.role_jianmo import jianmo
from src.instance_zones.cangqiong.role_fight.role_jiulv import jiulv
from src.instance_zones.cangqiong.role_fight.role_lang import lang
from src.instance_zones.cangqiong.role_fight.role_lieyan import lieyan
from src.instance_zones.cangqiong.role_fight.role_mingzun import mingzun
from src.instance_zones.cangqiong.role_fight.role_moying import moying
from src.instance_zones.cangqiong.role_fight.role_quansha import quansha
from src.instance_zones.cangqiong.role_fight.role_ruina import ruina
from src.instance_zones.cangqiong.role_fight.role_shikong import shikong
from src.instance_zones.cangqiong.role_fight.role_shuangyu import shuangyu
from src.instance_zones.cangqiong.role_fight.role_wuji import wuji
from src.instance_zones.cangqiong.role_fight.role_yemo import yemo
from src.instance_zones.cangqiong.role_fight.role_zhankuang import zhankuang
from src.instance_zones.ge_duo_mi_gong.role_fight.role_hongling import hongling_mi_gong
from src.instance_zones.public_method import is_frequency_over, is_no_pilao
from src.instance_zones.tao_fa.role_fight.role_nvwang import nvwang
from util.find_picture_color import colors_son_for_parent, picture_son_for_parent
from util.keyboard_operation import key_press, key_down, key_up
from util.log import log
from util.mouse_operation import scroll, left_click, move_to, left_double_click
from util.utils import delay
from util.window import findHwnd


def role_chance(hwnd, name, map):
    if name == "shikong":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return shikong(hwnd, into_result, "out")
        else:
            log.info("???????????????"+map)
            return "break"
    elif name == "shuangyu":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return shuangyu(hwnd, into_result, "out")
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "jianmo":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return jianmo(hwnd, into_result, "out")
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "quansha":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return quansha(hwnd, into_result, "out")
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "diyue":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return diyue(hwnd, into_result, "out")
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "hongling":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return hongling(hwnd, into_result, "out")
        elif map == "ge_duo_mi_gong":
            into_result = into_mi_gong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return hongling_mi_gong(hwnd)
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "chengling":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return hongling(hwnd, into_result, "out")
        elif map == "ge_duo_mi_gong":
            into_result = into_mi_gong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return hongling_mi_gong(hwnd)
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "huangling":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return hongling(hwnd, into_result, "out")
        elif map == "ge_duo_mi_gong":
            into_result = into_mi_gong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return hongling_mi_gong(hwnd)
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "qingling":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return hongling(hwnd, into_result, "out")
        elif map == "ge_duo_mi_gong":
            into_result = into_mi_gong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return hongling_mi_gong(hwnd)
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "lvling":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return hongling(hwnd, into_result, "out")
        elif map == "ge_duo_mi_gong":
            into_result = into_mi_gong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return hongling_mi_gong(hwnd)
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "fenling":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return hongling(hwnd, into_result, "out")
        elif map == "ge_duo_mi_gong":
            into_result = into_mi_gong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return hongling_mi_gong(hwnd)
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "moying":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return moying(hwnd, into_result, "out")
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "jiulv":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return jiulv(hwnd, into_result, "out")
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "ruina":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return ruina(hwnd, into_result, "out")
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "lieyan":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return lieyan(hwnd, into_result, "out")
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "mingzun":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return mingzun(hwnd, into_result, "out")
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "wuji":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return wuji(hwnd, into_result, "out")
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "daoshi":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return daoshi(hwnd, into_result, "out")
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "fuwen":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return fuwen(hwnd, into_result, "out")
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "yemo":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return yemo(hwnd, into_result, "out")
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "zhankuang":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return zhankuang(hwnd, into_result, "out")
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "lang":
        if map == "cangqiong":
            into_result = into_cangqiong(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return lang(hwnd, into_result, "out")
        else:
            log.info("???????????????" + map)
            return "break"
    elif name == "nvwang":
        if map == "taofa":
            into_result = into_taofa(hwnd)
            if into_result == "reset":
                return "reset"
            elif into_result == "break":
                return "break"
            else:
                return nvwang(hwnd)
        else:
            log.info("???????????????" + map)
            return "break"
    else:
        log.info("???????????????" + name)
        return "break"


# ??????reset?????????????????????left?????????right??????
def into_cangqiong(hwnd):
    key_press(hwnd, "W")
    delay(500)
    for i in range(5):
        scroll(hwnd, -120, (50, 50))
        delay(200)
    key_down(hwnd, "W")
    key_down(hwnd, "D")
    delay(6500)
    count = 0
    while True:
        x, y = colors_son_for_parent(hwnd, [(150, 255, 255)], 0.9, (60, 785, 110, 851))
        if x > 0 and y > 0:
            key_up(hwnd, "W")
            key_up(hwnd, "D")
            delay(200)
            left_click(hwnd, (740, 830))
            delay(1200)
            move_to(hwnd, (410, 460))  # ????????????
            delay(500)
            key_press(hwnd, "F")
            delay(500)
            key_press(hwnd, "enter")
            delay(500)
            if is_frequency_over(hwnd):  # ??????????????????
                delay(300)
                key_press(hwnd, "enter")
                delay(500)
                left_click(hwnd, (740, 830))
                delay(500)
                move_to(hwnd, (710, 460))  # ??????
                delay(300)
                key_press(hwnd, "F")
                delay(500)
                key_press(hwnd, "enter")
                delay(500)
                if is_frequency_over(hwnd):  # ??????????????????
                    delay(300)
                    key_press(hwnd, "enter")
                    delay(300)
                    key_press(hwnd, "esc")
                    delay(300)
                    log.info("?????????????????????")
                    back_change_role(hwnd)
                    return "break"
                else:
                    log.info("?????????")
                    return "right"
            else:
                log.info("?????????")
                return "left"
        else:
            count = count + 1
            delay(500)
            if count > 10:
                log.info("????????????????????????")
                back_change_role(hwnd)
                return "reset"

# ??????????????????reset???????????????
def into_taofa(hwnd):
    key_press(hwnd, "W")
    delay(500)
    key_down(hwnd, "W")
    key_down(hwnd, "A")
    delay(1500)
    key_up(hwnd, "W")
    key_up(hwnd, "A")
    key_down(hwnd, "W")
    delay(3000)
    key_up(hwnd, "W")
    key_down(hwnd, "W")
    key_down(hwnd, "A")
    delay(500)
    count = 0
    while True:
        x, y = colors_son_for_parent(hwnd, [(150, 255, 255)], 0.9, (60, 785, 110, 851))
        if x > 0 and y > 0:
            key_up(hwnd, "W")
            key_up(hwnd, "A")
            delay(200)
            left_click(hwnd, (600, 820))
            delay(1200)
            move_to(hwnd, (1050, 480))  # ?????????
            delay(500)
            key_press(hwnd, "F")
            delay(500)
            key_press(hwnd, "enter")
            delay(500)
            if is_no_pilao(hwnd):  # ????????????
                delay(300)
                key_press(hwnd, "enter")
                delay(300)
                key_press(hwnd, "esc")
                delay(300)
                log.info("??????????????????")
                back_change_role(hwnd)
                return "break"
            return True
        else:
            count = count + 1
            delay(500)
            if count > 10:
                log.info("????????????????????????")
                back_change_role(hwnd)
                return "reset"


# ??????reset????????????
def into_mi_gong(hwnd):
    key_press(hwnd, "W")
    delay(500)
    key_down(hwnd, "W")
    delay(5500)
    count = 0
    while True:
        x, y = colors_son_for_parent(hwnd, [(150, 255, 255)], 0.9, (60, 785, 110, 851))
        if x > 0 and y > 0:
            key_up(hwnd, "W")
            delay(200)
            left_click(hwnd, (502, 830))
            delay(1200)
            move_to(hwnd, (1022, 316))  # ?????????
            delay(500)
            key_press(hwnd, "F")
            delay(500)
            key_press(hwnd, "enter")
            delay(500)
            if is_frequency_over(hwnd):  # ????????????
                delay(300)
                key_press(hwnd, "enter")
                delay(300)
                key_press(hwnd, "esc")
                delay(300)
                log.info("??????????????????")
                back_change_role(hwnd)
                return "break"
            return True
        else:
            count = count + 1
            delay(500)
            if count > 10:
                log.info("????????????????????????")
                back_change_role(hwnd)
                return "reset"


# ??????1???????????????????????????????????????
def enter_pindao(hwnd, change):
    count = 0
    while True:
        x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/cityAndPage/pindao_button.bmp", 0.9,
                                  (1365, 761, 1510, 813))
        if x > 0 and y > 0:
            if change == "1":
                log.info("??????????????????")
                left_click(hwnd, (1451, 520))
                delay(500)
                left_click(hwnd, (x, y))
                delay(5000)
                return
            else:
                left_click(hwnd, (1421, 690))
                delay(500)
                left_click(hwnd, (x, y))
                delay(500)
                key_press(hwnd, "enter")
                delay(5000)
                return
        else:
            count = count + 1
            delay(500)
            if count > 10:
                log.info("????????????????????????")
                #todo
                return


# ????????????????????????????????????
def role_change(hwnd):
    delay(500)
    count = 0
    while True:
        x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/cityAndPage/role_change.bmp", 0.9,
                                      (1333, 854, 1400, 885))
        if x > 0 and y > 0:
            log.info("???????????????")
            delay(1200)
            left_click(hwnd, (x, y))
            delay(2000)
            return
        else:
            count = count + 1
            delay(500)
            if count > 10:
                log.info("????????????????????????")
                return


if __name__ == '__main__':
    hwnd = findHwnd("JFZR")
    enter_pindao(hwnd,"12")
