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
    fileName = 'simple.pcap'
    try:
        os.remove(fileName)
    except OSError:
        pass
    s1_pcap = S1.popen('tcpdump -i any -w '+fileName) # s1-eth1 eth0 any


    # s1_pcap.terminate()
    c1 = net.addController('c1',controller=RemoteController, ip="172.19.0.2",port=6633)
    c2 = net.addController('c2',controller=RemoteController, ip="172.19.0.3",port=6633)
    c3 = net.addController('c3',controller=RemoteController, ip="172.19.0.4",port=6633)

    # net.addLink(c1,S1)
    for i in range(2):
        Hn = net.addHost('h' + str(i+1))
        net.addLink(Hn,S1)
    for h in net.hosts:
        # print("disable ipv6")
        h.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
        h.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
        h.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")
    net.start()
    

    # CLI.do_dpctl('dump-flows -O OpenFlow13')
    # H1 = net.getNodeByName('h1')
    # for h in net.hosts:
        # net.ping([H1,h])
        # net.pingAll()
    # sleep(5)
    # s1_pcap = S1.popen('tcpdump -w '+fileName+' -i any')
    # for i in range(10):
    #     # sleep(5)
    #     net.pingAll("0")
    #     # sleep(1)
    h1 = net.hosts[0]
    h2 = net.hosts[1]
    # print(h2.IP())
    print (h1.cmd('ping -c 100 -i 0.1 -q -s 100 ' + h2.IP()))
    sleep(5)
    # net.iperf(hosts=net.hosts,
    #         #   l4Type='UDP',
    #           seconds=1,
    #         #   udpBw='1M'
    #           )
    # for i in range(3):
    #     Hn = net.addHost( 'h' + str(i+3))
    #     hlink = net.addLink(S1,Hn)
    #     S1.attach(hlink.intf1)
    #     Hn.configDefault(defaultRoute=Hn.defaultIntf())
    #     net.pingAll()
    #     sleep(1)
    # sleep(1)
    # for i in range(1):
    #     net.pingAll()
    #     # os.system("ping -c 1 127.0.0.1" ) # FLAG
    #     sleep(1)
    # net.delLinkBetween(H2,S1)
    # for i in range(1):
    #     net.pingAll()
    #     # sleep(5)
    sleep(3)
    s1_pcap.terminate()
    # CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    emptyNet()
