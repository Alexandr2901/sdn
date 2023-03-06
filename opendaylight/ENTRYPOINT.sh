#!/usr/bin/env bash

# arrVar=("AC" "TV" "Mobile" "Fridge" "Oven" "Blender")
arrVar=()
for ((i=1; i<=10;i++)); do
    param=$(dig +short opendaylight$i)
    # echo $param
    arrVar+=($param)
done
echo "hi"

for value in "${arrVar[@]}"
do
     echo $value
done
index=-1
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
/opt/odl/karaf-0.8.4/bin/stop
# /opt/odl/karaf-0.8.4/bin/client -r 10 "restart"
/opt/odl/karaf-0.8.4/bin/karaf