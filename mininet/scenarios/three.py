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
        # cn = net.addController('c'+ str(i+1),controller=RemoteController, ip="192.168.31.250",port=(6633+i))
        cn = net.addController('c'+ str(i+1),controller=RemoteController, ip="172.16.0."+str(i+2),port=6633)

        # cn = net.addController('c'+ str(i+1),controller=RemoteController, ip="sdn_opendaylight_max_"+str(i+1)+".sdn_sdn",port=6633)

    fileName = 'three.pcap'    
    
    try:
        os.remove(fileName)
    except OSError:
        pass
    s1_pcap = S1.popen('tcpdump -c 30000 -i any -w '+fileName) # s1-eth1 eth0 any
    S2 = net.addSwitch('s2')
    S3 = net.addSwitch('s3')
    net.addLink(S1,S2)
    net.addLink(S1,S3)
    net.addLink(S3,S2)


    # net.addLink(c1,S1)
    for i in range(3):
        Hn = net.addHost('h' + str(i+1))
        Sn =net.getNodeByName('s' + str(i+1))
        net.addLink(Hn,Sn)
    for h in net.hosts:
        # print("disable ipv6")
        h.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
        h.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
        h.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")

    for i in range(len(net.switches)):
        net.switches[i].start([net.controllers[i% len(net.controllers)] ])
        # net.switches[i].start([net.controllers[0]])
    net.start()
    net.pingAll()
    # h1 = net.hosts[0]
    # h2 = net.hosts[1]
    # print("start ping flood")
    # print (h1.cmd('ping -c 10 -i 0.001 -q -s 1000 ' + h2.IP()))
    # net.iperf((h1,h2),
    #           l4Type='UDP',
    #           seconds=3,
    #           udpBw='1000M'
    #           )
    # for i in range(1):
    #     net.pingAll()
    #     # sleep(5)
    sleep(1)
    s1_pcap.terminate()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    emptyNet()
