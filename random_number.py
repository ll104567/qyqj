# date 2019.11.9
# author Hu
# ll104567i@163.com

import random

def random_number(n=6):
    a = []
    for i in range(n):
        a.append(random.randint(1,9))

    return a

print(random_number())
