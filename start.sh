#!/bin/bash
docker-compose up -d --build 
# docker exec sdn_mininet_1 service openvswitch-switch start
# docker exec -it sdn_mininet_1 mn --topo linear,3 --mac --controller=remote,ip=opendaylight,port=6633 --switch ovs,protocols=OpenFlow13
