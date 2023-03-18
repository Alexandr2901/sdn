#!/bin/bash
# docker rm -f sdn_opendaylight1_1 sdn_opendaylight2_1 sdn_opendaylight3_1 sdn_mininet_1 sdn_nginx_1
docker-compose up -d --build --remove-orphans
# docker exec sdn_mininet_1 service openvswitch-switch start
# docker exec -it sdn_mininet_1 mn --topo linear,3 --mac --controller=remote,ip=opendaylight,port=6633 --switch ovs,protocols=OpenFlow13
# echo 'hi'
# docker exec -it sdn_opendaylight1_1 /opt/odl/karaf-0.8.4/bin/status
# sleep 15
# docker exec -it sdn_opendaylight1_1 /opt/odl/karaf-0.8.4/bin/configure_cluster.sh 1 sdn_opendaylight1_1 sdn_opendaylight2_1 sdn_opendaylight3_1
# docker exec -it sdn_opendaylight2_1 /opt/odl/karaf-0.8.4/bin/configure_cluster.sh 2 sdn_opendaylight1_1 sdn_opendaylight2_1 sdn_opendaylight3_1
# docker exec -it sdn_opendaylight3_1 /opt/odl/karaf-0.8.4/bin/configure_cluster.sh 3 sdn_opendaylight1_1 sdn_opendaylight2_1 sdn_opendaylight3_1
# docker exec -it sdn_opendaylight1_1 /opt/odl/karaf-0.8.4/bin/client -r 10 "restart org.opendaylight.controller.sal-distributed-datastore"
# docker exec -it sdn_opendaylight2_1 /opt/odl/karaf-0.8.4/bin/client -r 10 "restart org.opendaylight.controller.sal-distributed-datastore"
# docker exec -it sdn_opendaylight3_1 /opt/odl/karaf-0.8.4/bin/client -r 10 "restart org.opendaylight.controller.sal-distributed-datastore"
# docker exec sdn_opendaylight1_1 /opt/odl/karaf-0.8.4/bin/client -r 10 "restart"
# docker exec sdn_opendaylight2_1 /opt/odl/karaf-0.8.4/bin/client -r 10 "restart"
# docker exec sdn_opendaylight3_1 /opt/odl/karaf-0.8.4/bin/client -r 10 "restart"

# sleep 30
# docker exec -it sdn_mininet_1 mn -c && docker exec -it sdn_mininet_1 python3 net.py
# docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}" 
# mininet dpctl dump-flows
# sudo docker exec -it sdn_mininet_1 /bin/bash
# nc -vz 172.19.0.2 1-10000 2>&1 | grep succeeded
# scp mininet@192.168.56.106:/home/mininet/projects/sdn/mininet/scenarios/dump.pcap  .
# tcpdump -i any -nq
docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}" 
# netcat -zv 172.16.0.2 1-9000 2>&1 | grep succeeded