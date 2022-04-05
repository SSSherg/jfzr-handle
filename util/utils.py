import time
import random

from util.log import log


def delay(times):
    if 0 < times < 100:
        times = times + random.randint(0, 20)
    elif 100 <= times < 1000:
        times = times + random.randint(50, 100)
    elif 1000 <= times < 10000:
        times = times + random.randint(100, 200)
    elif 10000 <= times < 30000:
        times = times + random.randint(1000, 2000)
    elif times >= 30000:
        times = times + random.randint(1000, 1500)
    else:
        log.info("奇怪的延迟")
    time.sleep(times / 1000)


if __name__ == '__main__':
    log.info("start")
    delay(1000)
    log.info("end")
