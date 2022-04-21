# -*- coding: utf-8 -*-
import sys
import unittest


# 截取当前窗口屏幕 pos 代表区域[x1,y1,x2,y2] ,默认全屏
import win32api
import win32con
import win32gui
import win32ui

from util.mouse_operation import left_click
from util.utils import delay
from util.window import findHwnd

TITLE_Y = 25


def window_c(filename, hwnd, pos=None):
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    if pos is None:  # 强烈建议传坐标，否则w,h是依照监控器长宽，图片会很大
        x1 = 0
        y1 = 0
        w = MoniterDev[0][2][2]
        h = MoniterDev[0][2][3]
    else:
        x1 = pos[0]
        y1 = pos[1] + TITLE_Y
        w = pos[2] - pos[0]
        h = pos[3] - pos[1]
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (x1, y1), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
    # 内存释放
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)


def test(hwnd):
    left_click(hwnd,(660,460))
    delay(4000)
    for i in range(7):
        window_c(sys.path[2] + "/other_function/card_matching/img_temp/" + str(i) + ".bmp", hwnd,(323,147,1027,740))
        delay(500)


if __name__ == '__main__':
    hwnd = findHwnd("JFZR")
    test(hwnd)
