# date 2019.11.9
# author Hu
# ll104567i@163.com

import time
import os
import random

def f_exists(filename):
    if os.path.exists(filename):
        return True
    else:
        return False

def f_modify(filesize,filename):

    if os.path.getsize(filename) == filesize:
        return True
    else:
        return False

def f_sleep(t=2):
    time.sleep(t)

