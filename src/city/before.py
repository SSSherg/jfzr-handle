import sys
import time

from src.city.exit import back_city, back_change_role
from util.date_utils import getTimeStr
from util.find_picture_color import picture_son_for_parent, capture_the_current_window_screen
from util.ini_file_operation import readIni, writeIni
from util.keyboard_operation import key_press
from util.log import log
from util.mouse_operation import left_click, left_double_click, scroll, right_click, move_to
from util.utils import delay
from util.window import findHwnd


def login(hwnd, full_name):
    loop_count = 0
    move_count = 0
    while True:
        x, y = picture_son_for_parent(hwnd, full_name, 0.9, (1305, 39, 1500, 711))
        if x > 0 and y > 0:
            left_click(hwnd, (x, y))
            delay(300)
            left_double_click(hwnd, (x, y))
            delay(8000)
            return True
        else:
            move_to(hwnd, (1449, 234))
            if move_count < 16:
                scroll(hwnd, -120, (1449, 234))
                delay(500)
                move_count = move_count + 1
            if move_count > 15:
                for j in range(10):
                    scroll(hwnd, 120, (1449, 234))
                    delay(500)
                move_count = 0
                loop_count = loop_count + 1
            if loop_count > 1:
                log.info(full_name + "循环2次未找到！")
                return False


def is_login(hwnd):
    count = 0
    while True:
        x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/cityAndPage/right_bottom_login.bmp", 0.9,
                                      (1562, 852, 1600, 900))
        if x > 0 and y > 0:
            return True
        else:
            count = count + 1
            delay(1000)
            if count > 20:
                log.info("没进游戏！")
                return False


def email(hwnd):
    key_press(hwnd, "M")  # 一定要按
    delay(300)
    email_count = 1
    email_temp = True
    while email_temp:  # 先检测打开邮箱
        x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/email/email.bmp", 0.9,
                                      (780, 220, 880, 300))
        if x > 0 and y > 0:
            email_temp = False
        else:
            key_press(hwnd, "M")
            email_count = email_count + 1
            delay(300)
            if email_count > 10:
                log.info("没检测到邮箱！")
                capture_the_current_window_screen(hwnd, getTimeStr(time.time()) + readIni("name") + "-email.bmp")
                back_city(hwnd)
                back_change_role(hwnd)
                return False
    email_temp = True
    if readIni("isEmail") == "yes":
        while email_temp:  # 再开始收邮箱
            x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/email/have_email.bmp", 0.9,
                                          (660, 275, 718, 405))
            if x > 0 and y > 0:
                left_click(hwnd, (693, 676))
                delay(200)
                left_click(hwnd, (813, 676))
                delay(200)
                left_click(hwnd, (903, 676))
                delay(200)
                key_press(hwnd, "enter")
                delay(1400)
            else:
                writeIni("isEmail", "no")  # 邮件收过了就不用再收了
                email_temp = False
    if readIni("isGeDuoBox") == "yes":  # 要先点到背包消耗品位置
        delay(200)
        left_click(hwnd, (1265, 160))
        delay(500)
        left_click(hwnd, (1305, 422))
        delay(500)
        # 使用戈多宝箱
        x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/email/geduo_box.bmp", 0.6,
                                      (1204, 424, 1560, 781))
        if x > 0 and y > 0:
            log.info("开启戈多箱子！")
            right_click(hwnd, (x, y))
            delay(1000)
            key_press(hwnd, "enter")
            delay(2500)
            key_press(hwnd, "enter")
            writeIni("isGeDuoBox", "no")  # 戈多开过了
            delay(1000)
    if readIni("isGiftBox") == "yes":  # 要先点到背包消耗品位置
        delay(200)
        left_click(hwnd, (1240, 100))
        delay(500)
        left_click(hwnd, (1276, 362))
        delay(500)
        # 使用超凡礼盒
        x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/email/geduo_box.bmp", 0.7,
                                  (1204, 364, 1560, 721))
        if x > 0 and y > 0:
            right_click(hwnd, (x, y))
            delay(200)
            key_press(hwnd, "enter")
            delay(2500)
            key_press(hwnd, "enter")
            writeIni("isGiftBox", "no")  # 礼盒开过了
    email_temp = True
    if readIni("isPet") == "yes":  # 要先点到宠物栏
        count = 0
        while email_temp:
            delay(200)
            left_click(hwnd, (1428, 99))
            delay(500)
            left_click(hwnd, (1225, 363))
            delay(500)
            # 使用超凡礼盒
            x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/email/pig.bmp", 0.9,
                                          (1204, 374, 1560, 731))
            if x > 0 and y > 0:
                right_click(hwnd, (x, y))
                delay(200)
                email_temp = False
                writeIni("isPet", "no")  # 装备猪了
            else:
                x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/email/pig_on.bmp", 0.9,
                                              (1200, 216, 1269, 280))
                if x > 0 and y > 0:
                    email_temp = False
                    writeIni("isPet", "no")  # 装备猪了
                else:
                    count = count + 1
                    if count > 2:
                        log.info("找不到猪八戒")
                        return False
    return True


if __name__ == '__main__':
    hwnd = findHwnd("JFZR")
    email(hwnd)
