#!/usr/bin/env python
from time import sleep
from mininet.net import Mininet
from mininet.node import RemoteController, Node, OVSSwitch
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import Link


def emptyNet():
    net = Mininet(controller=RemoteController, waitConnected=True)
    c1 = net.addController('c1',controller=RemoteController, ip="172.19.0.2",port=6633)
    c2 = net.addController('c2',controller=RemoteController, ip="172.19.0.3",port=6633)
    c3 = net.addController('c3',controller=RemoteController, ip="172.19.0.4",port=6633)
    S0 = net.addSwitch('s0')
    s1_pcap = S0.popen('tcpdump -w star.pcap -i any')
    for h in net.hosts:
        h.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
        h.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
        h.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")
    net.start()
    for i in range(50):
        Sn = net.addSwitch('s' + str(i+1))
        Hn = net.addHost('h' + str(i+1))
        hlink = net.addLink(Hn,Sn)
        slink = net.addLink(S0,Sn)
        S0.attach(slink.intf1)
        Sn.start(net.controllers)
        Sn.attach(slink.intf1)
        Sn.attach(hlink.intf1)
        Hn.configDefault(defaultRoute=Hn.defaultIntf())
        Hn.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
        Hn.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
        Hn.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")
        sleep(1)
        net.pingAll()
    for i in range(5):
        net.pingAll()
        sleep(1)
    s1_pcap.terminate()
    CLI(net)
    net.stop()
if __name__ == '__main__':
    setLogLevel('info')
    emptyNet()
