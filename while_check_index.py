# date 2019.11.9
# author Hu
# ll104567i@163.com

import time
import os

filename = 'index.html'
filesize = os.path.getsize(filename)
flag = True

count = 1
while 1:
   
    if os.path.exists(filename):
        pass
    else:
        print('{} Delete.'.format(filename))        
        flag = False
        break
    
    if os.path.getsize(filename) == filesize:
        pass
    else:
        print('{} Modify.'.format(filename))        
        flag = False
        break

    print(count)
    count += 1
    time.sleep(2)

if flag:
    print('{} is ok'.format(filename))

