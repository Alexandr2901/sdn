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
    # net = Mininet(controller=RemoteController)

    S1 = net.addSwitch('s1')
    # c1 = net.addController('c'+ str(i+1),controller=RemoteController, ip="sdn_opendaylight_max_"+str(i+1)+".sdn_sdn")
    for i in range(3):
        cn = net.addController('c'+ str(i+1),controller=RemoteController, ip="sdn_opendaylight_max_"+str(i+1)+".sdn_sdn",port=6633)

    # c2 = net.addController('c2',controller=RemoteController, ip="172.16.0.3",port=6633)
    # c3 = net.addController('c3',controller=RemoteController, ip="172.16.0.4",port=6633)
    # c4 = net.addController('c4',controller=RemoteController, ip="172.16.0.3",port=6633)
    # c5 = net.addController('c5',controller=RemoteController, ip="172.16.0.4",port=6633)
    # c3 = net.addController('c3',controller=RemoteController, ip="opendaylight1",port=6633)
    # sleep(5)
    fileName = 'simple.pcap'    
    try:
        os.remove(fileName)
    except OSError:
        pass
    s1_pcap = S1.popen('tcpdump -i any -w '+fileName) # s1-eth1 eth0 any
    # s1_pcap.terminate()

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
    net.pingAll("0")
    #     # sleep(1)
    h1 = net.hosts[0]
    h2 = net.hosts[1]
    # print(h2.IP())
    print("start ping flood")
    # print (h1.cmd('ping -c 10 -i 0.001 -q -s 1000 ' + h2.IP()))

    # sleep(1)
    net.iperf((h1,h2),
              l4Type='UDP',
              seconds=1,
            #   udpBw='1M'
              )
    # net.pingAll(timeout="0")
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
    sleep(1)
    s1_pcap.terminate()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    emptyNet()
