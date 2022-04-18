from time import time

from src.city.before import login, is_login, email
from src.city.enter import role_chance
from util.ini_file_operation import readIni, initIni, writeIni
from util.log import log
from util.process_operation import kill
from util.read_memery import get_money
from util.role_json_operation import getData
from util.utils import delay
from util.window import findHwnd


def begin():
    hwnd = findHwnd("JFZR")
    roles = getData().get("roles")
    role_size = len(roles)
    start = int(readIni("start"))
    all_money = 0
    today_money = 0
    map_type = 0   # 用于频道的切换，普通图刷完后切戈多迷宫频道，所以刷迷宫的角色需要放在普通图的后面
    while start < role_size:  # 用ini文件的start 记录当前角色，角色完成或者跳过时，start+1 并写入ini文件
        initIni(roles[start])
        start_time = time()
        begin_money = 0     # 防止角色重启而重复读取覆盖
        while True:
            map_name = readIni("map")
            if map_type == 0:
                if map_name == "ge_duo_mi_gong":
                    # 换频道
                    map_type = 1
            log.info("角色开始：" + readIni("name") + "  地图：" + map_name)
            if not login(hwnd,  readIni("full_name")):     # 登录角色
                log.info("找不到角色跳过")
                break  # 跳过此角色
            if not is_login(hwnd):              # 判断是否已登录
                log.info("登录不了角色跳过")
                break  # 跳过此角色
            if begin_money == 0:
                begin_money = get_money(hwnd)
                log.info("拥有金币: " + str(begin_money))
            if not email(hwnd):              # 判断接收邮件、开盒子、装备宠物等
                continue  # 重启
            role_chance_result = role_chance(hwnd, readIni("name"), map_name)
            if role_chance_result == "break":         # 开始刷图
                break  # 结束这个角色
            elif role_chance_result == "reset":
                continue  # 重启
            elif not role_chance_result:
                continue  # 重启
            break  # 结束这个角色
        end_money = get_money(hwnd)
        money = int(end_money) - int(begin_money)
        stop_time = time()
        log.info("角色耗时: "+str(stop_time - start_time)+" 秒,获取金币：" + str(money))
        start = start + 1
        writeIni("start", start)
        all_money = int(all_money) + int(end_money)
        today_money = int(today_money) + int(money)
    log.info("程序结束,今日共获取金币：" + str(today_money) + ", 总金币：" + str(all_money))
    kill(hwnd)


def test():
    return True

if __name__ == '__main__':
    real_money = int(8828388888) - int(7777237777)
    print(real_money)