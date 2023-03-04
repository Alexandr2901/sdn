#!/usr/bin/env bash
index=-1
allThreads=(172.19.0.2 172.19.0.3 172.19.0.4)
# echo $allThreads
param=$(hostname -i)
# echo $param
for i in "${!allThreads[@]}"; do
    [[ "${allThreads[$i]}" = "${param}" ]] && index=$(($i+1))
done
string="${allThreads[*]}"
# echo $string
# echo /opt/odl/karaf-0.8.4/bin/configure_cluster.sh $index $string

/opt/odl/karaf-0.8.4/bin/configure_cluster.sh $index $string
/opt/odl/karaf-0.8.4/bin/stop
# /opt/odl/karaf-0.8.4/bin/client -r 10 "restart"
/opt/odl/karaf-0.8.4/bin/karaf