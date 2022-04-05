import json
import sys


def getData():
    with open(sys.path[2] + '/resources/config_file/role_all.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
    return json_data


if __name__ == '__main__':
    s = "/resources/img/people/role-huangling.bmp"
    print(len(s))
    print(s[25:len(s)-4])
