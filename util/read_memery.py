# -*- coding: utf-8 -*-
import win32api
import win32process
from win32con import PROCESS_ALL_ACCESS
import ctypes

from util.window import findHwnd

mirror_base_address = 0x00400000  # 镜像基址
gold_deviation_address = mirror_base_address + 0x2CCF69C  # 金币基址


def get_money(hwnd):
    return read_process_memory(hwnd, gold_deviation_address, 4)


def read_process_memory(hwnd, address, length):
    h_pid, pid = win32process.GetWindowThreadProcessId(hwnd)  # 获取窗口ID
    h_process = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, pid)  # 获取进程句柄
    kernel32 = ctypes.windll.LoadLibrary("kernel32.dll")  # 加载动态链接库
    ReadProcessMemory = kernel32.ReadProcessMemory
    t_address = ctypes.c_ulong()
    ReadProcessMemory(int(h_process), address, ctypes.byref(t_address), length, None)
    win32api.CloseHandle(h_process)  # 关闭句柄
    return t_address.value



if __name__ == '__main__':
    hwnd = findHwnd("JFZR")
    value = read_process_memory(hwnd, gold_deviation_address, 4)
    print(value)
