import sys
from configobj import ConfigObj

from util.log import log
from util.role_json_operation import getData


# 获取ini配置  此配置主要是记录当前正常运行的角色的相关信息
def getIni():
    configTemp = ConfigObj(sys.path[2] + "/resources/config_file/role_current.ini", encoding='UTF8')
    return configTemp


def initIni(role):
    tempIni = getIni()
    name = role.get("name")
    tempIni['config']['name'] = name[25:len(name)-4]
    tempIni['config']['full_name'] = sys.path[2] + name
    tempIni['config']['map'] = role.get("map")
    tempIni['config']['map_level'] = role.get("map_level")
    tempIni['config']['isGiftBox'] = role.get("isGiftBox")
    tempIni['config']['isGeDuoBox'] = role.get("isGeDuoBox")
    tempIni['config']['isPet'] = role.get("isPet")
    tempIni['config']['isEmail'] = role.get("isEmail")
    tempIni.write()


def writeIni(key, value):
    tempIni = getIni()
    tempIni['config'][key] = value
    tempIni.write()


def readIni(key):
    return getIni()['config'][key]


if __name__ == '__main__':
    roles = getData().get("roles")
    role_size = len(roles)
    start = int(readIni("start"))
    while start < role_size:    # 用ini文件的start 记录当前角色，角色完成或者跳过时，start+1 并写入ini文件
        initIni(roles[start])
        start = start + 1
        writeIni("start", start)
        # while True:
        #     print(3)
            # if not login(people):     # 登录角色
            #     break  # 跳过此角色
            # if not getEmail(people):   # 收邮件
            #     break  # 跳过此角色
    log.info("程序结束！")

