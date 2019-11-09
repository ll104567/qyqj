# date 2019.11.9
# author Hu
# ll104567i@163.com

import random
import string

def random_number(n=6):
    a = ''
    for i in range(n):
        new_random_digit = random.choice(string.digits)
        a += new_random_digit

    return a

def random_string(n=6):
    a = ''
    for i in range(n):
        new_random_string = random.choice(string.ascii_lowercase)
        a += new_random_string

    return a

def random_mix(n=6):
    a = ''
    for i in range(n):
        new_random_string = random.choice(string.ascii_lowercase+string.digits)
        a += new_random_string

    return a
for i in range(10):
    
    print(random_mix(10))

