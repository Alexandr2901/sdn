#!/bin/bash
  #   <is-install-lldp-flow>false</is-install-lldp-flow>
#  <lldp-flow-table-id>3</lldp-flow-table-id>
mkdir -p ../etc/opendaylight/datastore/initial/config/
# touch ../etc/opendaylight/datastore/initial/config/l2switch-main-config_l2switch-main-config.xml
# touch ../etc/opendaylight/datastore/initial/config/arp-handler-config_arp-handler-config.xml
# touch ../etc/opendaylight/datastore/initial/config/l2switch-main-config_l2switch-main-config.xml

#   #  <is-install-lldp-flow>false</is-install-lldp-flow>
# echo '<?xml version="1.0" encoding="UTF-8"?> 
#   <loop-remover-config xmlns="urn:opendaylight:packet:loop-remover-config">
#    <lldp-flow-table-id>3</lldp-flow-table-id>
# </loop-remover-config>' > ../etc/opendaylight/datastore/initial/config/loop-remover-config_loop-remover-config.xml
#   # <is-proactive-flood-mode>false</is-proactive-flood-mode>
# echo '<?xml version="1.0" encoding="UTF-8"?>
#   <arp-handler-config xmlns="urn:opendaylight:packet:arp-handler-config">
#   <flood-flow-table-id>3</flood-flow-table-id>
# </arp-handler-config>' > ../etc/opendaylight/datastore/initial/config/arp-handler-config_arp-handler-config.xml
#   # <is-install-dropall-flow>false</is-install-dropall-flow>
#   # <dropall-flow-table-id>3</dropall-flow-table-id>
#     # <reactive-flow-table-id>3</reactive-flow-table-id>
# echo '<?xml version="1.0" encoding="UTF-8"?> 
#   <l2switch-config xmlns="urn:opendaylight:l2switch:l2switch-config">
#   <is-install-dropall-flow>false</is-install-dropall-flow>
#   <dropall-flow-table-id>3</dropall-flow-table-id>
#   <reactive-flow-table-id>3</reactive-flow-table-id>
# </l2switch-config>' > ../etc/opendaylight/datastore/initial/config/l2switch-config_l2switch-config.xml


echo '<?xml version="1.0" encoding="UTF-8"?> 
  <l2switch-config xmlns="urn:opendaylight:l2switch:l2switch-config">
  <is-install-dropall-flow>false</is-install-dropall-flow>
</l2switch-config>' > ../etc/opendaylight/datastore/initial/config/l2switch-config_l2switch-config.xml
