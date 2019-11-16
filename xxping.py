from scapy.all import IP,ICMP,sr1
import logging

def ping(host):

    packet = IP(dst=host)/ICMP()
    r = sr1(packet,timeout=1,verbose=False)
    if r:
        return True
    else:
        return False

if __name__ == '__main__':
    
    print(ping('www.baidu.com'))
