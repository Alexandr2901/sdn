#!/usr/bin/env python
from time import sleep
from mininet.net import Mininet
from mininet.node import RemoteController, Node, OVSSwitch
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import Link
import random
import os

def emptyNet():
    net = Mininet(controller=RemoteController, waitConnected=True)
    S1 = net.addSwitch('s1')
    for i in range(3):
        # cn = net.addController('c'+ str(i+1),controller=RemoteController, ip="172.16.0.6",port=6633)
        # cn = net.addController('c'+ str(i+1),controller=RemoteController, ip="sdn_opendaylight_max_"+str(i+1)+".sdn_sdn",port=6633)
        cn = net.addController('c'+ str(i+1),controller=RemoteController, ip="172.16.0."+str(i+2),port=6633)
    fileName = 'square.pcap'
    try:
        os.remove(fileName)
    except OSError:
        pass
    s1_pcap = S1.popen('tcpdump -c 30000 -i any -w '+fileName) # s1-eth1 eth0 any
 
    # S1 = net.addSwitch('s1')
    S2 = net.addSwitch('s2')
    S3 = net.addSwitch('s3')
    S4 = net.addSwitch('s4')
    # S5 = net.addSwitch('s5')
    # S6 = net.addSwitch('s6')
    # S7 = net.addSwitch('s7')
    # S8 = net.addSwitch('s8')
    # S9 = net.addSwitch('s9')


    for i in range(8):
        hn = net.addHost("h" + str(i+1))
        sn = net.getNodeByName("s" + str((i)%len(net.switches)+1))
        net.addLink(hn,sn)
        hn.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
        hn.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
        hn.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")
        # hn.configDefault(defaultRoute=hn.defaultIntf())


    # H1 = net.addHost('h1')
    # H2 = net.addHost('h2')
    # net.addLink(H1,S1)
    # net.addLink(H2,S9)
    # H3 = net.addHost('h3')
    # H4 = net.addHost('h4')
    # net.addLink(H3,S8)
    # net.addLink(H4,S9)
    # net.addLink(H2,H1)
    # switches = [S1,S2,S3,S7,S8,S9,S4,S6]

    net.addLink(S1,S2)
    net.addLink(S4,S1)
    # net.addLink(S5,S2)
    # net.addLink(S5,S4)
    
    # net.addLink(S7,S4)
    net.addLink(S2,S3)
    net.addLink(S1,S3)

    # net.addLink(S3,S6)
    # net.addLink(S6,S9)
    # net.addLink(S9,S8)
    # net.addLink(S8,S7)
    # net.addLink(S5,S6)
    # net.addLink(S5,S8)

    # links = [net.addLink(S1,S5),
    net.addLink(S2,S4),
    # net.addLink(S3,S5),
    # net.addLink(S2,S6),
    # net.addLink(S4,S8),
    # net.addLink(S5,S7),
    # net.addLink(S6,S8),
    # net.addLink(S5,S9)]
    # for i in range(len(net.switches)):
        # hn.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
        # hn.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
        # hn.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")
        # net.switches[i].start([net.controllers[i%len(net.controllers)]])
    # switches = net.switches
    # for sname in switches:
    #         sname.start(net.controllers)
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
    # CLI(net)
    # h1 = net.hosts[0]
    # h2 = net.hosts[8]
    for i in range(100):
        net.pingAll()
        # print (h1.cmd('ping -c 1000 -i 0.0001 -q  ' + h2.IP()))
        # net.delLink(links[i])
    
        for j in range(8):
            # net.delHost(net.getNodeByName("h" + str(i*4+j+1)))
            hn = net.getNodeByName("h" + str(j+1))
            hn.setIP("10.0.0." + str(i*4+j+5))
            # sn.setIp
            # net.delHost(net.hosts[0])
            # hn = net.addHost("h" + str(i*4+j+5))
            # sn = net.getNodeByName("s" + str((j)%len(net.switches)+1))
            # hlink = net.addLink(sn,hn)
            # sn.attach(hlink.intf1)
            # hn.configDefault(defaultRoute=hn.defaultIntf())
        sleep(5)
        # CLI(net)
    sleep(1)
    s1_pcap.terminate()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    emptyNet()
