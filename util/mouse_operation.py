
import win32gui
import win32api
import win32con

from util.utils import delay
from util.window import findHwnd


def left_down(hwnd, pos):
    wparam = 0
    long_position = win32api.MAKELONG(pos[0], pos[1])
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, wparam, long_position)


def left_up(hwnd, pos):
    wparam = 0
    long_position = win32api.MAKELONG(pos[0], pos[1])
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, wparam, long_position)


def right_down(hwnd, pos):
    wparam = 0
    long_position = win32api.MAKELONG(pos[0], pos[1])
    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, wparam, long_position)


def right_up(hwnd, pos):
    wparam = 0
    long_position = win32api.MAKELONG(pos[0], pos[1])
    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONUP, wparam, long_position)


def move_to(hwnd, pos):
    wparam = 0
    long_position = win32api.MAKELONG(pos[0], pos[1])
    win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, wparam, long_position)


def left_click(hwnd, pos):
    wparam = 0
    long_position = win32api.MAKELONG(pos[0], pos[1])
    win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, wparam, long_position)
    delay(80)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, wparam, long_position)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, wparam, long_position)


def left_double_click(hwnd, pos):
    wparam = 0
    long_position = win32api.MAKELONG(pos[0], pos[1])
    win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, wparam, long_position)
    delay(80)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, wparam, long_position)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, wparam, long_position)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, wparam, long_position)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, wparam, long_position)


def right_click(hwnd, pos):
    wparam = 0
    long_position = win32api.MAKELONG(pos[0], pos[1])
    win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, wparam, long_position)
    delay(80)
    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, wparam, long_position)
    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONUP, wparam, long_position)


def right_double_click(hwnd, pos):
    wparam = 0
    long_position = win32api.MAKELONG(pos[0], pos[1])
    win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, wparam, long_position)
    delay(80)
    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, wparam, long_position)
    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONUP, wparam, long_position)
    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, wparam, long_position)
    win32gui.SendMessage(hwnd, win32con.WM_RBUTTONUP, wparam, long_position)


# delta 整数为向上，负数为向下。120为一次滚轮
def scroll(hwnd, delta, pos):
    wparam = delta << 16
    pos = win32gui.ClientToScreen(hwnd, pos)   # 将窗口相对位置转为屏幕相对位置
    long_position = win32api.MAKELONG(pos[0], pos[1])
    win32gui.SendMessage(hwnd, win32con.WM_MOUSEWHEEL, wparam, long_position)  # 传入的是屏幕的相对位置


if __name__ == '__main__':
    hwnd = findHwnd("JFZR")
    print(hwnd)
    move_to(hwnd, (1400, 445))
    # scroll(hwnd, -120, (1354, 503))
