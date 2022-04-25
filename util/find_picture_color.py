import operator
import sys
from math import sqrt
from time import time

import win32gui
import win32api
import win32ui
import win32con
import cv2
import numpy as np

from util.window import findHwnd

# 这个截图会把程序的导航（最上面含有标题的白色背景部分算进去。所以需要在y轴加上相应的高度）
TITLE_Y = 25


# 多色找图 color_rbg为列表，示例：[(1,1,1)]
def colors_son_for_parent(hwnd, color_rbgs, threshold, pos):
    for color_rbg in color_rbgs:
        # color 为rgb,需转为bgr
        color_gbr = color_rbg[::-1]

        # 先截图
        father_img = sys.path[2] + "/img_temp/color_temp.bmp"
        window_capture(father_img, hwnd, pos)
        father_img_cv = cv2.imread(father_img)
        w, h = father_img_cv.shape[:2]
        for a in range(w):
            for b in range(h):
                if color_similarity(father_img_cv[a, b], color_gbr) >= threshold:
                    return pos[0] + b - 3, pos[1] + a - 1    # 这样减返回才是正确的坐标
    return 0, 0


def picture_son_for_parent(hwnd, son_img, threshold, pos=None):
    # 先截图父图
    father_img = sys.path[2] + "/img_temp/picture_temp.bmp"
    window_capture(father_img, hwnd, pos)
    father_img_cv = cv2.imread(father_img)
    son_img_cv = cv2.imread(son_img)

    # 匹配子图
    h, w = son_img_cv.shape[:2]  # 获取模板的高和宽
    result = cv2.matchTemplate(father_img_cv, son_img_cv, 1)  # 进行模板匹配  TM_SQDIFF_NORMED 匹配数值越低表示匹配效果越好
    loc = np.where(result <= (1-threshold))  # 提取小于阈值的点位
    for pt in zip(*loc[::-1]):  # 打包点位之后遍历寻
        # top_left = pt
        # bottom_right = (pt[0] + w, pt[1] + h)  # 右下角的点
        # cv2.rectangle(father_img_cv, top_left, bottom_right, 255, 2)  # 绘制矩形框
        # # 显示图片
        # cv2.imshow("father_img_cv", father_img_cv)
        # # cv2.imshow("son_img_cv", son_img_cv)
        # cv2.waitKey()
        # cv2.destroyAllWindows()

        pt = (pt[0] + pos[0], pt[1] + pos[1])  # 返回相对于整个页面的坐标，否则是所选坐标框内的
        return pt
    return 0, 0


# 截取当前窗口屏幕 pos 代表区域[x1,y1,x2,y2] ,默认全屏
def window_capture(filename, hwnd, pos=None):
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


def color_similarity(color1, color2):
    r = (color1[0] - color2[0]) / 256
    g = (color1[1] - color2[1]) / 256
    b = (color1[2] - color2[2]) / 256
    diff = 1 - sqrt(r * r + g * g + b * b)
    return diff


def picture_son_for_parent1(hwnd, son_img, threshold, pos=None):
    # 先截图父图
    father_img = sys.path[2] + "/img_temp/picture_temp.bmp"
    window_capture(father_img, hwnd, pos)
    father_img_cv = cv2.imread(father_img)
    son_img_cv = cv2.imread(son_img)

    # 匹配子图
    h, w = son_img_cv.shape[:2]  # 获取模板的高和宽
    result = cv2.matchTemplate(father_img_cv, son_img_cv, 1)  # 进行模板匹配  TM_SQDIFF_NORMED 匹配数值越低表示匹配效果越好
    loc = np.where(result <= (1-threshold))  # 提取小于阈值的点位
    for pt in zip(*loc[::-1]):  # 打包点位之后遍历寻
        top_left = pt
        bottom_right = (pt[0] + w, pt[1] + h)  # 右下角的点
        cv2.rectangle(father_img_cv, top_left, bottom_right, 255, 2)  # 绘制矩形框
        # 显示图片
        cv2.imshow("father_img_cv", father_img_cv)
        # cv2.imshow("son_img_cv", son_img_cv)
        cv2.waitKey()
        cv2.destroyAllWindows()

        pt = (pt[0] + pos[0], pt[1] + pos[1])  # 返回相对于整个页面的坐标，否则是所选坐标框内的
        return pt
    return 0, 0


def capture_the_current_window_screen(hwnd, file_name):
    window_capture(sys.path[2] + "/img_temp/" + file_name, hwnd, get_length_width(hwnd))


def get_length_width(hwnd):
    l_w = win32gui.GetWindowRect(hwnd)
    x1 = l_w[0]
    y1 = l_w[1]
    x2 = l_w[2]
    y2 = l_w[3]
    return x1 - x1, y1 - y1, x2 - x1, y2 - y1


if __name__ == '__main__':
    # 多往下25px  39
    hwnd = findHwnd("JFZR")
    # window_capture("../3.bmp", hwnd, (1305, 64, 1500, 765))
    # # start = time()
    x, y = picture_son_for_parent(hwnd, sys.path[2] + "/resources/img/cityAndPage/role_change.bmp", 0.9,
                                      (1333, 854, 1400, 885))
    print(x,y)
    # stop = time()
    # # print(str(stop - start) + "秒")

    # # print(inty)
    # # # # (18,324,47,348)
    # a, b = colors_son_for_parent(hwnd, [(150, 255, 255)], 0.9, (60, 785, 110, 851))
    # print(a, b)
    # print(color_similarity((84, 90, 169),(84, 90, 169)))
    # hwnd = findHwnd("钉钉")
    # print(get_length_width(hwnd))
    # window_capture(sys.path[2] + "/img_temp/1.bmp", hwnd, get_length_width(hwnd))