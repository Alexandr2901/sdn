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

# arrVar[0]="10.0.0.2"
# arrVar[1]="10.0.0.3"
# arrVar[2]="10.0.0.4"
# string="${arrVar[*]}"
# echo "${arrVar[2]}"


echo "
odl-cluster-data {
  akka {
    remote {
      log-remote-lifecycle-events = off
      artery {
        enabled = on
        transport = tcp
        canonical.hostname = ${arrVar[index]}
        canonical.port = 2550
      }
      netty.tcp {
        hostname = ${arrVar[index]}
        port = 2550
      #   maximum-frame-size = 419430400
      #   send-buffer-size = 52428800
      #   receive-buffer-size = 52428800
      }
      # when under load we might trip a false positive on the failure detector
      # transport-failure-detector {
        # heartbeat-interval = 4 s
        # acceptable-heartbeat-pause = 16s
      # }
      downing-provider-class = "akka.cluster.sbr.SplitBrainResolverProvider"
      split-brain-resolver {
        active-strategy = keep-majority
        stable-after = 7s
      }
      distributed-data {
        # How often the Replicator should send out gossip information.
        # This value controls how quickly Entity Ownership Service data is replicated
        # across cluster nodes.
        gossip-interval = 100 ms

        # How often the subscribers will be notified of changes, if any.
        # This value controls how quickly Entity Ownership Service decisions are
        # propagated within a node.
        notify-subscribers-interval = 20 ms
      }
    }

    cluster {
      # Remove ".tcp" when using artery.
      seed-nodes = ["akka://opendaylight-cluster-data@${arrVar[0]}:2550",
                                "akka://opendaylight-cluster-data@${arrVar[1]}:2550",
                                "akka://opendaylight-cluster-data@${arrVar[2]}:2550"]

      roles = ["member-$index"]

    }

    persistence {
      # By default the snapshots/journal directories live in KARAF_HOME. You can choose to put it somewhere else by
      # modifying the following two properties. The directory location specified may be a relative or absolute path. 
      # The relative path is always relative to KARAF_HOME.

      # snapshot-store.local.dir = "target/snapshots"
      # journal.leveldb.dir = "target/journal"
      journal {
        leveldb {
          # Set native = off to use a Java-only implementation of leveldb.
          # Note that the Java-only version is not currently considered by Akka to be production quality.

          # native = off
        }
      }
    }
  }
}"
# > /opt/odl/karaf-0.8.4/configuration/initial/akka.conf

# http://localhost:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/0/flow/def_goto

# {
#    "flow-node-inventory:flow":[
#       {
#          "id":"def_gotow",
#          "table_id":0,
#          "priority":0,
#           "match": {},
#          "instructions":{
#             "instruction":[
#                {
#                   "order":0,
#                   "go-to-table":{
#                      "table_id":3
#                   }
#                }
#             ]
#          }
#       }
#    ]
# }
