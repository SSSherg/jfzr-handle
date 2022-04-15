# -*- coding: utf-8 -*-
import os
import signal

import win32process

from util.window import findHwnd


def kill(pid):
    try:
        os.kill(pid, signal.SIGINT)
        print('The process with PID %s has been killed' % pid)
    except OSError as e:
        print("no this process")


if __name__ == '__main__':
    hwnd = findHwnd("记事本")
    h_pid, pid = win32process.GetWindowThreadProcessId(hwnd)  # 获取窗口ID
    kill(pid)