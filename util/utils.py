import time
import random

from util.log import log


def delay(min, max):
    time.sleep(random.randint(min, max)/1000)


if __name__ == '__main__':
    log.info("start")
    delay(100,200)
    log.info("end")
