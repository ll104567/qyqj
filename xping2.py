import logging
import ipaddress
import multiprocessing

from scapy.all import *
from random import randint

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def xping2(host):

    ip_id = randint(1,65535)
    icmp_id = randint(1,65535)
    icmp_seq = randint(1,65535)

    xxoo = IP(dst=host,ttl=64,id=ip_id)/ICMP(id=icmp_id,seq=icmp_seq)/b'hello'
    ping = sr1(xxoo,timeout=2,verbose=False)

    if ping:
        return True
    else:
        return False

def multi_xping(host_list):

    s = dict()
    for i in host_list:
        s[i] = xping2(i)

    return s

def multiscan(network):
    
    s = []
    for i in network:
        ping = multiprocessing.Process(target=xping2,args=(i,))
        ping.start()
        s.append([i,ping])

    return s

if __name__ == '__main__':

    a = multiscan(['192.168.1.1','192.168.1.101','192.168.1.102'])
    print(a)















