#!/usr/bin/env bash
arrVar=()
for ((i=1; i<=10;i++)); do
    # param=$(dig +short sdn_opendaylight_max_$i.sdn_sdn)
    param=$(dig +short opendaylight_max_$i)
    arrVar+=($param)
done
index=1
param=$(hostname -i)
for i in "${!arrVar[@]}"; do
    [[ "${arrVar[$i]}" = "${param}" ]] && index=$(($i+1))
done
string="${arrVar[*]}"
# echo $index $string
./stop
bash l2.sh
# echo /opt/odl/karaf-0.8.4/bin/configure_cluster.sh $index $string
./configure_cluster.sh $index $string
# bash akka.sh
# ./configure-cluster-ipdetect.sh $string
# sed -i 's/cluster {/cluster { \n akka.cluster.downing-provider-class = "akka.cluster.sbr.SplitBrainResolverProvider"/' /opt/odl/karaf-0.8.4/configuration/initial/akka.conf 
# sed -i 's/cluster {/cluster { \n      downing-provider-class = "akka.cluster.sbr.SplitBrainResolverProvider"/' /opt/odl/karaf-0.8.4/configuration/initial/akka.conf 
# sed -i 's/cluster {/cluster { \
#       downing-provider-class = "akka.cluster.sbr.SplitBrainResolverProvider split-brain-resolver " \
#       split-brain-resolver { \
#         active-strategy = "lease-majority" \
#         lease-majority { \
#             lease-implementation = "akka.coordination.lease.kubernetes" \
#         } \
#       } \
#     } /'  /opt/odl/karaf-0.8.4/configuration/initial/akka.conf 

# sed -i 's/.tcp:/:/' /opt/odl/karaf-0.8.4/configuration/initial/akka.conf 
# sed -i 's/enabled = off/enabled = on/' /opt/odl/karaf-0.8.4/configuration/initial/akka.conf 

# /opt/odl/karaf-0.8.4/bin/stop
# /opt/odl/karaf-0.8.4/bin/client -r 10 restart org.opendaylight.controller.sal-distributed-datastore
# /opt/odl/karaf-0.8.4/bin/karaf 
# ./karaf
JAVA_MAX_MEM=4G JAVA_MAX_PERM_MEM=512m ./karaf
/bin/bash


# 1*2 -t
# RESULT: 16 switches 15 tests min/max/avg/stdev = 0.00/4507.12/1223.91/1607.78 responses/s
# RESULT: 16 switches 15 tests min/max/avg/stdev = 0.00/34901.99/10499.06/9514.63 responses/s
# RESULT: 16 switches 15 tests min/max/avg/stdev = 0.00/30695.74/15026.50/9367.55 responses/s
# RESULT: 16 switches 15 tests min/max/avg/stdev = 453.85/44496.59/18529.38/14286.76 responses/s
# RESULT: 16 switches 15 tests min/max/avg/stdev = 0.00/58316.28/19943.60/17095.05 responses/s
# 12624,25

# 3*2 -t
# RESULT: 16 switches 15 tests min/max/avg/stdev = 0.00/3486.32/698.16/1155.18 responses/s
# RESULT: 16 switches 15 tests min/max/avg/stdev = 997.03/23696.62/10872.40/6586.97 responses/s
# RESULT: 16 switches 15 tests min/max/avg/stdev = 4700.13/66763.54/34392.07/22880.08 responses/s
# RESULT: 16 switches 15 tests min/max/avg/stdev = 0.99/46345.19/18702.59/13896.17 responses/s
# RESULT: 16 switches 15 tests min/max/avg/stdev = 4050.02/50739.32/21065.58/15228.18 responses/s
# 21257,75