#!/usr/bin/env python
from time import sleep, time
from mininet.net import Mininet
from mininet.node import RemoteController, Node, OVSSwitch,Controller
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import Link
import random
import os
from mininet.node import OVSSwitch


def emptyNet():
    net = Mininet(controller=RemoteController, waitConnected=True,
                  autoSetMacs=True,
                  autoStaticArp=True,
                  build=False,
                #   listenPort=6633,
                #   autoPinCpus=True,
                ipBase='10.255.255.0/24',
                  switch=OVSSwitch
                  )
    # net = Mininet( controller=Controller, switch=OVSSwitch,
    #                waitConnected=True )
    S1 = net.addSwitch('s1')
    for i in range(1):  
        # cn = net.addController('c'+ str(i+1),controller=RemoteController, ip="172.16.0.6",port=6633)
        # cn = net.addController('c'+ str(i+1),controller=RemoteController, ip="sdn_opendaylight_max_"+str(i+1)+".sdn_sdn",port=6633)
        # cn = net.addController('c'+ str(i+1),controller=RemoteController, ip="172.16.0."+str(i+2),port=6633)
        cn = net.addController('c'+ str(i+1),controller=RemoteController, ip="192.168.31.250",port=(6633+i))
        cn.start()
    fileName = 'links.pcap'
    try:
        os.remove(fileName)
    except OSError:
        pass    
    s1_pcap = S1.popen('tcpdump -c 20000 -i any -w '+fileName) # s1-eth1 eth0 an

    # for i in range(9):
    #     hn = net.addHost("h" + str(i+1))
    #     sn = net.getNodeByName("s" + str((i)%len(net.switches)+1))
    #     net.addLink(hn,sn)
    # for i in range(len(net.switches)):
    #     net.switches[i].start([net.controllers[i% len(net.controllers)] ])
    #     # net.switches[i].start([net.controllers[0]])

    net.start()
    # h1 = net.hosts[0]
    # h2 = net.hosts[8]
    start = time()
    for i in range(9):
        Sn = net.addSwitch('s'+ str(i+2))
        slink = net.addLink(S1,Sn)
        Sn.attach(slink.intf1)
        S1.attach(slink.intf1)
        for j in range(2):
            Hn = net.addHost('h' + str(i+2)+'_'+ str(j+1))
            # Hn = net.addHost('h' + str(i+2))
            hlink = net.addLink(Hn,Sn)
            Sn.attach(hlink.intf1)
            Hn.configDefault(defaultRoute=Hn.defaultIntf())
        
        Sn.start(net.controllers)


        # sleep(10)
        net.pingAll()
        # Sn.stop()
        # for switch in switches:
        #     counter +=1
        #     numder = i*(len(switches)) + counter + 10
        #     Hn = net.addHost('s'+ str(counter) + 'h' + str(i+1))
        #     hlink = net.addLink(switch,Hn)
        #     switch.attach(hlink.intf1)
        #     Hn.configDefault(defaultRoute=Hn.defaultIntf())
        #     # print(Hn.IP())
        #     # hosts.append(Hn)
        #     net.pingAll()
        #     sleep(1)


    # for i in range(5):
    #     print (h1.cmd('ping -c 100 -f ' + h2.IP()))
    #     net.iperf((h1,h2),
    #           l4Type='UDP',
    #           seconds=2,
    #           udpBw='1000M'
    #           )

    print('time Time TIME')
    print(time() - start)
    # net.pingAll()
    s1_pcap.terminate()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    emptyNet()


# sudo mn --controller=remote,ip=192.168.31.250:6633 --controller=remote,ip=192.168.31.250:6634 --controller=remote,ip=192.168.31.250:6635  --mac -i 10.1.1.0/24 --switch=ovs,protocol=OpenFlow13 --topo=linear,4 --arp --test=pingall