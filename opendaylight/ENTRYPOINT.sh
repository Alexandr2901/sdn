#!/usr/bin/env bash
arrVar=()
for ((i=1; i<=10;i++)); do
    param=$(dig +short sdn_opendaylight_max_$i.sdn_sdn)
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
# echo /opt/odl/karaf-0.8.4/bin/configure_cluster.sh $index $string
./configure_cluster.sh $index $string
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
JAVA_MAX_MEM=4G JAVA_MAX_PERM_MEM=512m ./karaf
/bin/bash
# JAVA_MAX_MEM=4G JAVA_MAX_PERM_MEM=512m ./karaf
