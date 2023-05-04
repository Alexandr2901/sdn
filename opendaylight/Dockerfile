FROM ubuntu:latest
RUN apt-get -y update && apt install -y openjdk-8-jre wget zip tcpdump dnsutils iputils-ping net-tools nano
RUN mkdir /opt/odl
RUN wget -O /opt/odl/odl.zip https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/karaf/0.8.4/karaf-0.8.4.zip
# RUN wget -O /opt/odl/odl.zip https://nexus.opendaylight.org/content/repositories/public/org/opendaylight/integration/opendaylight/16.2.0/opendaylight-16.2.0.zip
# RUN wget -O /opt/odl/odl.zip https://nexus.opendaylight.org/content/repositories/public/org/opendaylight/integration/distribution-karaf/0.4.4-Beryllium-SR4/distribution-karaf-0.4.4-Beryllium-SR4.zip
RUN unzip /opt/odl/odl.zip -d /opt/odl
# WORKDIR /opt/odl/distribution-karaf-0.4.4-Beryllium-SR4/bin
WORKDIR /opt/odl/karaf-0.8.4/bin
RUN rm /opt/odl/odl.zip 
# RUN echo "feature:install odl-restconf odl-l2switch-switch odl-mdsal-apidocs http odl-mdsal-distributed-datastore odl-dluxapps-applications odl-dluxapps-nodes odl-dluxapps-topology odl-dluxapps-yangui odl-dluxapps-yangvisualizer odl-dluxapps-yangman odl-dluxapps-yangutils && logout" | ./karaf
# RUN echo "feature:install odl-mdsal-clustering odl-netconf-clustered-topology && logout" | ./karaf
# RUN echo "sleep 1 && feature:install odl-mdsal-clustering odl-netconf-clustered-topology && logout" | ./karaf
# RUN echo "feature:install odl-l2switch-switch odl-mdsal-distributed-datastore && logout" | ./karaf
# ENV FEATURES="odl-l2switch-switch,odl-mdsal-apidocs,http,odl-mdsal-distributed-datastore,odl-dluxapps-applications,odl-dluxapps-nodes,odl-dluxapps-topology,odl-dluxapps-yangui,odl-dluxapps-yangvisualizer,odl-dluxapps-yangman,odl-dluxapps-yangutils,odl-mdsal-clustering,odl-netconf-clustered-topology,odl-openflowplugin-flow-services"
# ENV FEATURES="odl-mdsal-clustering,odl-openflowplugin-flow-services"
# ENV FEATURES="odl-l2switch-switch,odl-dluxapps-applications,odl-dluxapps-nodes,odl-dluxapps-topology,\
# odl-dluxapps-yangui,odl-dluxapps-yangvisualizer,odl-dluxapps-yangman,odl-dluxapps-yangutils\
# odl-mdsal-clustering,odl-openflowplugin-flow-services,odl-netconf-clustered-topology"
# ENV FEATURES="odl-dl2switch-switch,odl-dluxapps-applications,odl-dluxapps-nodes,odl-dluxapps-topology,\
# odl-dluxapps-yangui,odl-dluxapps-yangvisualizer,odl-dluxapps-yangman,odl-dluxapps-yangutils"
# RUN sed -i "s/\(featuresBoot= \|featuresBoot = \)/featuresBoot = ${FEATURES},/g" ../etc/org.apache.karaf.features.cfg
# RUN cat ../etc/org.apache.karaf.features.cfg
# RUN apt-get -y update && apt-get install -y nano
# RUN ./start && ./client -r 10 "feature:install odl-openflowplugin-all odl-l2switch-all " && ./stop

# RUN rm /opt/odl/karaf-0.8.4/system/org/opendaylight/openflowplugin/openflowplugin/0.6.4/openflowplugin-0.6.4.jar
# COPY ./openflowplugin-0.6.4.jar /opt/odl/karaf-0.8.4/system/org/opendaylight/openflowplugin/openflowplugin/0.6.4/openflowplugin-0.6.4.jar
# COPY ./openflowplugin-api-0.6.4.jar /opt/odl/karaf-0.8.4/system/org/opendaylight/openflowplugin/openflowplugin-api/0.6.4/openflowplugin-api-0.6.4.jar 
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre

RUN ./start && ./client -r 10 "feature:install odl-l2switch-all features-dluxapps features-restconf odl-netconf-clustered-topology odl-mdsal-clustering odl-jolokia" && ./stop
# RUN ./start && ./client -r 10 "feature:install odl-l2switch-all odl-openflowplugin-drop-test" && ./stop odl-mdsal-clustering 
# odl-mdsal-clustering odl-netconf-clustered-topology odl-openflowplugin-flow-services  odl-jolokia
# RUN ./set_persistence.sh off 
# WORKDIR /opt/odl/opendaylight-16.2.0/bin

COPY ./ENTRYPOINT.sh .
COPY ./l2.sh .
COPY ./akka.sh .
ENTRYPOINT ["./ENTRYPOINT.sh"]

# 4 core
# RESULT: 16 switches 15 tests min/max/avg/stdev = 7496.97/34509.83/25729.74/9030.40 responses/s
# RESULT: 16 switches 15 tests min/max/avg/stdev = 9421.56/33963.79/29032.29/5694.77 responses/s

# 2 core
# RESULT: 16 switches 15 tests min/max/avg/stdev = 1121.00/16534.98/9931.26/5830.27 responses/s
# RESULT: 16 switches 15 tests min/max/avg/stdev = 4602.00/16698.82/13957.51/2957.43 responses/s

# 2*1 core
# RESULT: 16 switches 15 tests min/max/avg/stdev = 1796.00/17767.98/10737.46/5719.36 responses/s
# RESULT: 16 switches 15 tests min/max/avg/stdev = 3421.00/17784.98/14659.79/3570.16 responses/s

# 2*3 core
# RESULT: 16 switches 15 tests min/max/avg/stdev = 1214.00/16470.40/8268.31/4981.57 responses/s
# RESULT: 16 switches 15 tests min/max/avg/stdev = 12770.96/16577.15/15209.38/1162.12 responses/s
# RESULT: 16 switches 15 tests min/max/avg/stdev = 1248.00/16488.84/9324.04/5496.45 responses/s
# RESULT: 16 switches 15 tests min/max/avg/stdev = 3707.00/16888.98/14693.03/3149.92 responses/s
# RESULT: 16 switches 15 tests min/max/avg/stdev = 1825.00/15907.98/9960.27/4981.05 responses/s
# RESULT: 16 switches 15 tests min/max/avg/stdev = 13580.99/17884.98/15881.25/1360.74 responses/s

# sudo docker exec -it sdn_opendaylight_max_1 ./client -r 10 "dropallpacketsrpc on" && sudo docker exec -it sdn_opendaylight_max_2 ./client -r 10 "dropallpacketsrpc on" && sudo docker exec -it sdn_opendaylight_max_3 ./client -r 10 "dropallpacketsrpc on"

