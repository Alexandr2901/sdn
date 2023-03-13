#!/usr/bin/env bash
arrVar=()
for ((i=1; i<=10;i++)); do
    # ip="172.16.0.$i"
    param=$(dig +short sdn_opendaylight_max_$i.sdn_sdn)
    # echo $param
    arrVar+=($param)
    # param=$(ping -c 1 127.0.0.1)
    # if [[$param =="0"]]; then
    #     echo $param
    # fi
    # arrVar+="172.16.0.$i "
done
# echo "hi"
# for value in "${arrVar[@]}"
# do
#      echo $value
# done
index=1
# allThreads=(172.19.0.2 172.19.0.3 172.19.0.4)
# echo $allThreads
param=$(hostname -i)
# echo $param
for i in "${!arrVar[@]}"; do
    [[ "${arrVar[$i]}" = "${param}" ]] && index=$(($i+1))
done
string="${arrVar[*]}"
# echo $string
# echo /opt/odl/karaf-0.8.4/bin/configure_cluster.sh $index $string
/opt/odl/karaf-0.8.4/bin/configure_cluster.sh $index $string
sed -i 's/cluster {/cluster { \n      akka.cluster.downing-provider-class = "akka.cluster.sbr.SplitBrainResolverProvider"/' /opt/odl/karaf-0.8.4/configuration/initial/akka.conf 
/opt/odl/karaf-0.8.4/bin/stop
JAVA_MAX_MEM=4G JAVA_MAX_PERM_MEM=512m /opt/odl/karaf-0.8.4/bin/karaf 