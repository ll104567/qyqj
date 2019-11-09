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

if __name__ == '__main__':

    filename = 'index.html'
    filesize = os.path.getsize(filename)
    
    while 1:
       
        print(random.randint(1,100))
        f_sleep()
        if not f_exists(filename):
            print('{} deleted.'.format(filename))
            break
        if not f_modify(filesize,filename):
            print('{} modified.'.format(filename))
            break
