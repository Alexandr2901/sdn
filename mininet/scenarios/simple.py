#!/usr/bin/env python
from time import sleep
from mininet.net import Mininet
from mininet.node import RemoteController, Node, OVSSwitch
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import Link


def emptyNet():
    net = Mininet(controller=RemoteController, waitConnected=True)
    # c1 = net.addController('c1',controller=RemoteController, ip="127.0.0.1",port=6633)
    c1 = net.addController('c1',controller=RemoteController, ip="172.19.0.2",port=6633)
    # c2 = net.addController('c2',controller=RemoteController, ip="172.19.0.3",port=6633)
    # c3 = net.addController('c3',controller=RemoteController, ip="172.19.0.4",port=6633)

    S1 = net.addSwitch('s1')
    # H1 = net.addHost('h1')
    # H2 = net.addHost('h1')

    # net.addLink(H1,S1)
    # net.addLink(H2,S1)

    net.start()
    for i in range(3):
        Hn = net.addHost( 'h' + str(i+3))
        hlink = net.addLink(S1,Hn)
        S1.attach(hlink.intf1)
        Hn.configDefault(defaultRoute=Hn.defaultIntf())
        net.pingAll()
        sleep(1)
    for i in range(1):
        net.pingAll()
        sleep(1)
    CLI(net)
    net.stop()
if __name__ == '__main__':
    setLogLevel('info')
    emptyNet()