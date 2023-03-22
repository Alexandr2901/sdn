FROM ubuntu:latest
RUN apt-get -y update && apt install -y openjdk-8-jre wget zip 
RUN mkdir /opt/odl
RUN wget -O /opt/odl/odl.zip https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/karaf/0.8.4/karaf-0.8.4.zip
RUN unzip /opt/odl/odl.zip -d /opt/odl
WORKDIR /opt/odl/karaf-0.8.4/bin
RUN apt-get -y update && apt-get install -y tcpdump dnsutils iputils-ping net-tools
RUN rm /opt/odl/odl.zip 
# RUN echo "feature:install odl-restconf odl-l2switch-switch odl-mdsal-apidocs http odl-mdsal-distributed-datastore odl-dluxapps-applications odl-dluxapps-nodes odl-dluxapps-topology odl-dluxapps-yangui odl-dluxapps-yangvisualizer odl-dluxapps-yangman odl-dluxapps-yangutils && logout" | ./karaf
# RUN echo "feature:install odl-mdsal-clustering odl-netconf-clustered-topology && logout" | ./karaf
# RUN echo "sleep 1 && feature:install odl-mdsal-clustering odl-netconf-clustered-topology && logout" | ./karaf
# RUN echo "feature:install odl-l2switch-switch odl-mdsal-distributed-datastore && logout" | ./karaf
# ENV FEATURES="odl-l2switch-switch,odl-mdsal-apidocs,http,odl-mdsal-distributed-datastore,odl-dluxapps-applications,odl-dluxapps-nodes,odl-dluxapps-topology,odl-dluxapps-yangui,odl-dluxapps-yangvisualizer,odl-dluxapps-yangman,odl-dluxapps-yangutils,odl-mdsal-clustering,odl-netconf-clustered-topology,odl-openflowplugin-flow-services"
# ENV FEATURES="odl-mdsal-clustering,odl-openflowplugin-flow-services"
ENV FEATURES="odl-l2switch-switch,odl-dluxapps-applications,odl-dluxapps-nodes,odl-dluxapps-topology,\
odl-dluxapps-yangui,odl-dluxapps-yangvisualizer,odl-dluxapps-yangman,odl-dluxapps-yangutils\
odl-mdsal-clustering,odl-openflowplugin-flow-services,odl-netconf-clustered-topology"
RUN sed -i "s/\(featuresBoot= \|featuresBoot = \)/featuresBoot = ${FEATURES},/g" ../etc/org.apache.karaf.features.cfg
RUN cat ../etc/org.apache.karaf.features.cfg
RUN ./set_persistence.sh off 
COPY opendaylight/ENTRYPOINT.sh /
ENTRYPOINT ["/ENTRYPOINT.sh"]
