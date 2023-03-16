#!/usr/bin/env python
from time import sleep
from mininet.net import Mininet
from mininet.node import RemoteController, Node, OVSSwitch
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import Link
import os

def emptyNet():
    net = Mininet(controller=RemoteController, waitConnected=True)
    S1 = net.addSwitch('s1')
    for i in range(3):
        # cn = net.addController('c'+ str(i+1),controller=RemoteController, ip="172.16.0."+str(i+1),port=6633)
        cn = net.addController('c'+ str(i+1),controller=RemoteController, ip="sdn_opendaylight_max_"+str(i+1)+".sdn_sdn",port=6633)
    fileName = 'links.pcap'
    try:
        os.remove(fileName)
    except OSError:
        pass
    s1_pcap = S1.popen('tcpdump -i any -w '+fileName) # s1-eth1 eth0 any
    # for i in range(2):
    #     Hn = net.addHost('h' + str(i+1))
    #     net.addLink(Hn,S1)
 
    # S1 = net.addSwitch('s1')
    S2 = net.addSwitch('s2')
    S3 = net.addSwitch('s3')
    S4 = net.addSwitch('s4')
    S5 = net.addSwitch('s5')
    S6 = net.addSwitch('s6')
    S7 = net.addSwitch('s7')
    S8 = net.addSwitch('s8')
    S9 = net.addSwitch('s9')

    H1 = net.addHost('h1')
    H2 = net.addHost('h2')
    net.addLink(H1,S1)
    net.addLink(H2,S9)
    # net.addLink(H2,H1)
    # switches = [S1,S2,S3,S7,S8,S9,S4,S6]

    net.addLink(S1,S2)
    net.addLink(S4,S1)
    net.addLink(S5,S2)
    net.addLink(S5,S4)
    
    net.addLink(S7,S4)
    net.addLink(S2,S3)
    net.addLink(S3,S6)
    net.addLink(S6,S9)
    net.addLink(S9,S8)
    net.addLink(S8,S7)
    net.addLink(S5,S6)
    net.addLink(S5,S8)

    # net.addLink(S1,S5)
    # net.addLink(S2,S4)
    # net.addLink(S3,S5)
    # net.addLink(S2,S6)
    # net.addLink(S4,S8)
    # net.addLink(S5,S7)
    # net.addLink(S6,S8)
    # net.addLink(S5,S9)
    net.start()
    # for h in net.hosts:
    #     h.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
    #     h.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
    #     h.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")
    # net.pingAll()
    # sleep(60)

    # 1 2 3 свитч линки
    # 4 5 6
    # 7 8 9
    # net.ping(net.switches)
    net.pingAll()

    for i in range(1):
        print (H1.cmd('ping -c 10 -i 0.001 -q4r -s 100 ' + H2.IP()))
        net.delLinkBetween(S1,S2)
        net.delLinkBetween(S4,S5)
        net.delLinkBetween(S5,S6)
        net.delLinkBetween(S8,S9)
        sleep(1)
        net.pingAll()
        print (H1.cmd('ping -c 10 -i 0.001 -q4r -s 100 ' + H2.IP()))

        net.delLinkBetween(S7,S8)
        net.delLinkBetween(S2,S3)
        net.addLink(S1,S2)
        net.addLink(S8,S9)
        sleep(1)
        print (H1.cmd('ping -c 10 -i 0.001 -q4r -s 100 ' + H2.IP()))

        net.addLink(S4,S5)
        net.addLink(S5,S6)
        net.addLink(S7,S8)
        net.addLink(S2,S3)
        sleep(1)
    net.pingAll()
    sleep(1)
    s1_pcap.terminate()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    emptyNet()