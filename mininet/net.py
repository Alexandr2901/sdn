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
    c1 = net.addController('c1',controller=RemoteController, ip="opendaylight1",port=6633)
    # c2 = net.addController('c2',controller=RemoteController, ip="opendaylight2",port=6633)
    # c3 = net.addController('c3',controller=RemoteController, ip="opendaylight3",port=6633)

    # net.addController('co2',controller=RemoteController, ip="opendaylight2",port=6633)
    # net.addController('co3',controller=RemoteController, ip="opendaylight3",port=6633)

    H2 = net.addHost('h2')
    H3 = net.addHost('h3')
    H4 = net.addHost('h4')
    S1 = net.addSwitch('s1')
    S2 = net.addSwitch('s2')
    S3 = net.addSwitch('s3')
    S4 = net.addSwitch('s4')
    net.addLink(H2,S2)
    net.addLink(H3,S3)
    net.addLink(H4,S4)
    net.addLink(S2,S1)
    net.addLink(S3,S1)
    net.addLink(S4,S1)

    net.addLink(S2,S3)
    net.addLink(S3,S4)
    net.addLink(S4,S2)

    # net.build()
   
    net.start()
    # SC = net.addSwitch('s5')
    # net.addLink(SC,S1)
    # SC.start([c1,c2,c3])
    # S1.start()
    # S2.start()
    # S3.start()
    # S4.start()
    # net.addLink(SC,c1)
   
    # 
    net.pingAll()
    for i in range(1):
        S1 = net.get('s1')
        Sn = net.addSwitch('s' + str(i+6))
        Hn = net.addHost('h' + str(i+6))
        hlink = net.addLink(Hn,Sn)
        slink = net.addLink(S1,Sn)
        S1.attach(slink.intf1)
        Sn.start(net.controllers)
        Sn.attach(slink.intf1)
        Sn.attach(hlink.intf1)
        Hn.configDefault(defaultRoute=Hn.defaultIntf())
        net.pingAll()
        sleep(1)
    # for i in range(1000):
    #     net.pingAll()
    #     sleep(5)
    CLI(net)
    net.stop()
if __name__ == '__main__':
    setLogLevel('info')
    emptyNet()