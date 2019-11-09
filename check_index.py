# date 2019.11.9
# author Hu
# ll104567i@163.com

import time
import os

filename = 'index.html'
flag = True


for i in range(10):
    
    if os.path.exists(filename):
        pass
    else:
        print('{} Delete.'.format(filename))
        
        flag = False
        break

    print(i)
    time.sleep(3)

if flag:
    print('{} is ok'.format(filename))

