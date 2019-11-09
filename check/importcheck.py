# date 2019.11.9
# author Hu
# ll104567i@163.com

import time
import os
import random

from f_checklib import f_exists,f_modify,f_sleep


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
