#!/usr/bin/env bash
# cp akka.test akka.conf

# sed -i 's/cluster {/cluster { \
#       downing-provider-class = "akka.cluster.sbr.SplitBrainResolverProvider split-brain-resolver " \
#       split-brain-resolver { \
#         active-strategy = "lease-majority" \
#         lease-majority { \
#             lease-implementation = "akka.coordination.lease.kubernetes" \
#         } \
#       } \
#     } /' ./akka.conf 

echo "module-shards = [
        {
                name = "default"
                shards = [
                        {
                                name = "default"
                                replicas = ["member-1",
                                "member-2",
                                "member-3"]
                        }
                ]
        },
      ]" > q.txt
# sed -i 's/cluster {/cluster { \n      akka.cluster.downing-provider-class = "akka.cluster.sbr.SplitBrainResolverProvider"/' ./akka.conf 
# sed -i 's/.tcp:/:/' ./akka.conf 
# sed -i 's/enabled = off/enabled = on/' ./akka.conf 

# sed -r 's/[\*]+//g'

# echo '\nakka.cluster.downing-provider-class = "akka.cluster.sbr.SplitBrainResolverProvider"' akka.conf >> ./akka.conf 
# param=$(grep -n "cluster {" akka.conf)
# echo $param

http://localhost:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/0/flow/def_goto

{
   "flow-node-inventory:flow":[
      {
         "id":"def_gotow",
         "table_id":0,
         "priority":0,
          "match": {},
         "instructions":{
            "instruction":[
               {
                  "order":0,
                  "go-to-table":{
                     "table_id":3
                  }
               }
            ]
         }
      }
   ]
}
