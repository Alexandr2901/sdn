#!/usr/bin/env python
from time import sleep
from mininet.net import Mininet
from mininet.node import RemoteController, Node, OVSSwitch
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import Link


def emptyNet():
    net = Mininet(controller=RemoteController, waitConnected=True)
    # net.addController('co1',controller=RemoteController, ip="opendaylight1",port=6633)
    # c0 = net.addController('c0',controller=RemoteController, ip="nginx",port=6633)
    
    c1 = net.addController('c1',controller=RemoteController, ip="172.19.0.2",port=6633)
    c2 = net.addController('c2',controller=RemoteController, ip="172.19.0.3",port=6633)
    c3 = net.addController('c3',controller=RemoteController, ip="172.19.0.4",port=6633)

    S1 = net.addSwitch('s1')
    S2 = net.addSwitch('s2')
    # S3 = net.addSwitch('s3')
    S4 = net.addSwitch('s4')
    S5 = net.addSwitch('s5')
    # S6 = net.addSwitch('s6')
    # S7 = net.addSwitch('s7')
    # S8 = net.addSwitch('s8')
    # S9 = net.addSwitch('s9')

    # H1 = net.addHost('h1')
    # H2 = net.addHost('h2')
    # net.addLink(H1,S5)
    # net.addLink(H2,S5)

    # switches = [S1,S2,S3,S7,S8,S9,S4,S6]
    switches = [S1,S2,S4,S5]


    # 1 2 3 свитч линки
    # 4 5 6
    # 7 8 9

    net.addLink(S1,S2)
    net.addLink(S4,S1)
    net.addLink(S5,S2)
    net.addLink(S5,S4)
    
    # net.addLink(S7,S4)
    # net.addLink(S2,S3)
    # net.addLink(S3,S6)
    # net.addLink(S6,S9)
    # net.addLink(S9,S8)
    # net.addLink(S8,S7)
    # net.addLink(S5,S6)
    # net.addLink(S5,S8)

    # net.addLink(S1,S5)
    # net.addLink(S2,S4)
    # net.addLink(S3,S5)
    # net.addLink(S2,S6)
    # net.addLink(S4,S8)
    # net.addLink(S5,S7)
    # net.addLink(S6,S8)
    # net.addLink(S5,S9)

    net.start()
    for i in range(3):
        counter = 0
        hosts = []
        for switch in switches:
            counter +=1
            numder = i*(len(switches)) + counter + 10
            Hn = net.addHost('s'+ str(counter) + 'h' + str(i+1))
            hlink = net.addLink(switch,Hn)
            switch.attach(hlink.intf1)
            Hn.configDefault(defaultRoute=Hn.defaultIntf())
            # print(Hn.IP())
            # hosts.append(Hn)
            net.pingAll()
            sleep(1)
        # sleep(1)
        # net.ping(hosts)
        # net.pingAll()
    for i in range(100):
        net.pingAll()
        sleep(10)
    CLI(net)
    net.stop()
if __name__ == '__main__':
    setLogLevel('info')
    emptyNet()