
import os
import requests
from bs4 import BeautifulSoup

heros_list = []
heros_file = 'heros.txt'

heros_url = 'https://pvp.qq.com/web201605/herolist.shtml'
rsp = requests.get(heros_url)
if rsp.status_code == 200:
    rsp.encoding = 'gbk'
    b = BeautifulSoup(rsp.text,'lxml')

    for i in b.select('li>a>img'):
        heros_list.append((i['alt'],i['src'][2:]))

if not os.path.exists(heros_file):
    with open(heros_file,'w') as f:
        for i in heros_list:
            f.write(i[0]+'\n')

for i in heros_list:
    with open ('img/'+i[0]+'.jpg','wb') as f:
        a = requests.get('http://'+i[1])
        if a.status_code == 200:
            for j in a:
                f.write(j)

            print('{} download...'.format(i[0]))
