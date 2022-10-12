#!/usr/bin/env python
from time import sleep
from mininet.net import Mininet
from mininet.node import RemoteController, Node, OVSSwitch
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import Link


def emptyNet():

    net = Mininet(controller=RemoteController, waitConnected=True)
    net.addController('co',controller=RemoteController, ip="opendaylight1",port=6633)

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
    net.start()
    net.pingAll()
    for i in range(50):
        S1 = net.get('s1')
        Sn = net.addSwitch('s' + str(i+5))
        Hn = net.addHost('h' + str(i+5))
        hlink = net.addLink(Hn,Sn)
        slink = net.addLink(S1,Sn)
        S1.attach(slink.intf1)
        Sn.start(net.controllers)
        Sn.attach(slink.intf1)
        Sn.attach(hlink.intf1)
        Hn.configDefault(defaultRoute=Hn.defaultIntf())
        net.pingAll()
        sleep(5)
    for i in range(1000):
        net.pingAll()
        sleep(5)
    CLI(net)
    net.stop()
if __name__ == '__main__':
    setLogLevel('info')
    emptyNet()