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
RUN ./start && ./client -r 10 "feature:install odl-l2switch-all features-dluxapps features-restconf odl-mdsal-clustering odl-netconf-clustered-topology odl-mdsal-distributed-datastore odl-jolokia" && ./stop
# RUN ./start && ./client -r 10 "feature:install odl-l2switch-all " && ./stop
# odl-mdsal-clustering odl-netconf-clustered-topology odl-openflowplugin-flow-services  odl-jolokia
# RUN ./set_persistence.sh off 
# WORKDIR /opt/odl/opendaylight-16.2.0/bin

COPY ./ENTRYPOINT.sh .
COPY ./l2.sh .

ENTRYPOINT ["./ENTRYPOINT.sh"]

