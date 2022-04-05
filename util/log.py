import logging
import os
import sys
import time

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.FileHandler(sys.path[2]+"\\log\\"+time.strftime("%Y-%m-%d", time.localtime())+".txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

log.addHandler(handler)
log.addHandler(console)

if __name__ == '__main__':
    log.info("333")