from util.ini_file_operation import readIni, initIni
from util.log import log
from util.role_json_operation import getData
from util.window import findHwnd


def begin():
    hwnd = findHwnd("JFZR")
    roles = getData().get("roles")
    role_size = len(roles)
    start = int(readIni("start"))
    while start < role_size:  # 用ini文件的start 记录当前角色，角色完成或者跳过时，start+1 并写入ini文件
        initIni(roles[start])
        while True:
            log.info("角色开始：" + readIni("name"))
            # if not login(people):     # 登录角色
            #     break  # 跳过此角色
            # start = start + 1
            # writeIni("start", start)
            # if not getEmail(people):   # 收邮件
            #     break  # 跳过此角色
        log.info("角色耗时")
        start = start + 1
        writeIni("start", start)
    log.info("程序结束")
