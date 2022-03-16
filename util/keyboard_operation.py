import string
import time

import win32gui
import win32api
import win32con

from util.mouse_operation import left_click
from util.window import findHwnd

VkCode = {
    "back":  0x08,
    "tab":  0x09,
    "return":  0x0D,
    "shift":  0x10,
    "control":  0x11,
    "menu":  0x12,
    "pause":  0x13,
    "capital":  0x14,
    "escape":  0x1B,
    "space":  0x20,
    "end":  0x23,
    "home":  0x24,
    "left":  0x25,
    "up":  0x26,
    "right":  0x27,
    "down":  0x28,
    "print":  0x2A,
    "snapshot":  0x2C,
    "insert":  0x2D,
    "delete":  0x2E,
    "lwin":  0x5B,
    "rwin":  0x5C,
    "numpad0":  0x60,
    "numpad1":  0x61,
    "numpad2":  0x62,
    "numpad3":  0x63,
    "numpad4":  0x64,
    "numpad5":  0x65,
    "numpad6":  0x66,
    "numpad7":  0x67,
    "numpad8":  0x68,
    "numpad9":  0x69,
    "multiply":  0x6A,
    "add":  0x6B,
    "separator":  0x6C,
    "subtract":  0x6D,
    "decimal":  0x6E,
    "divide":  0x6F,
    "f1":  0x70,
    "f2":  0x71,
    "f3":  0x72,
    "f4":  0x73,
    "f5":  0x74,
    "f6":  0x75,
    "f7":  0x76,
    "f8":  0x77,
    "f9":  0x78,
    "f10":  0x79,
    "f11":  0x7A,
    "f12":  0x7B,
    "numlock":  0x90,
    "scroll":  0x91,
    "lshift":  0xA0,
    "rshift":  0xA1,
    "lcontrol":  0xA2,
    "rcontrol":  0xA3,
    "lmenu":  0xA4,
    "rmenu":  0XA5
}


def get_virtual_keycode(key):
    if len(key) == 1 and key in string.printable:
        return ord(key)
    else:
        return VkCode[key]


def key_down(hwnd, key):
    vk_code = get_virtual_keycode(key)
    scan_code = win32api.MapVirtualKey(vk_code, 0)
    wparam = vk_code
    print(wparam)
    lparam = (scan_code << 16) | 1
    win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, wparam, lparam)


def key_up(hwnd, key):
    vk_code = get_virtual_keycode(key)
    scan_code = win32api.MapVirtualKey(vk_code, 0)
    wparam = vk_code
    lparam = (scan_code << 16) | 0XC0000001
    win32gui.SendMessage(hwnd, win32con.WM_KEYUP, wparam, lparam)


def key_press(hwnd, key):
    key_down(hwnd, key)
    time.sleep(0.3)
    key_up(hwnd, key)


if __name__ == '__main__':
    hwnd = findHwnd("备注.md - Typora")
    left_click(hwnd, (25,51))
    time.sleep(0.5)
    key_press(hwnd, "f8")