import win32gui


# 窗口工具类
# 找句柄，title为窗口标题
def findHwnd(title):
    hwnds = []
    hwnd_title = dict()  # 函数用于创建一个字典

    def get_all_hwnd(hwnd, param):  # param:指定一个传递给回调函数的应用程序定义值(传指定参数用的)
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t != "":
            # print(h,t)
            if title in t:
                hwnds.append(h)

    if len(hwnds) == 0:
        print("找不到相应的句柄")
    else:
        return hwnds[0]


# 遍历所有窗口信息
def getAllHwnd():
    hwnd_title = dict()  # 函数用于创建一个字典

    def get_all_hwnd(hwnd, param):  # param:指定一个传递给回调函数的应用程序定义值(传指定参数用的)
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_title.items():
        if t != "":
            print(h, t)
    return hwnd_title.items()
