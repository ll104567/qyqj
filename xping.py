import os

def xping(host='www.baidu.com'):
    '''
        这是一个ping的函数
        xping('www.baidu.com')
    '''

    response = os.system('ping {} -c 1 -W 2 -q'.format(host))
    if response == 0:
        return True
    else:
        return False


if __name__ == '__main__':
  
    a = []
    with open('url.txt') as f:
        for i in f:
            i = i.strip()
            a.append(i)
    with open('urlcheck.txt','w') as f:
        for i in a:
            if(xping(i)):
                f.write(i+' ok\n')
