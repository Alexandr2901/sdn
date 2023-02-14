FROM ubuntu:latest
# RUN echo $cluster_number
RUN apt-get -y update && apt install -y openjdk-8-jre wget zip 
RUN mkdir /opt/odl
RUN wget -O /opt/odl/odl.zip https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/karaf/0.8.4/karaf-0.8.4.zip
# RUN wget -O /opt/odl/odl.zip https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/karaf/0.16.2/karaf-0.16.2.zip
RUN unzip /opt/odl/odl.zip -d /opt/odl
# RUN mv /opt/odl/dist* -d /opt/odl/boron
# CMD /opt/odl/boron/bin/karaf
# EXPOSE 8181 6633 8101
# grep "featuresBoot = " opt/odl/karaf-0.8.4/etc/org.apache.karaf.features.cfg
RUN /opt/odl/karaf-0.8.4/bin/start && /opt/odl/karaf-0.8.4/bin/client -r 10 \
"feature:install odl-dlux-core odl-dluxapps-nodes odl-dluxapps-topology odl-dluxapps-yangui \ 
odl-dluxapps-yangvisualizer odl-dluxapps-yangman odl-restconf odl-l2switch-switch odl-mdsal-apidocs http jolokia \ 
odl-mdsal-distributed-datastore" && \ 
/opt/odl/karaf-0.8.4/bin/set_persistence.sh off && \
# /opt/odl/karaf-0.8.4/bin/configure_cluster.sh $cluster_number 172.19.0.2 172.19.0.3 172.19.0.4 && \ 
# /opt/odl/karaf-0.8.4/bin/client -r 10 restart org.opendaylight.controller.sal-distributed-datastore && \ 
/opt/odl/karaf-0.8.4/bin/stop
# ARG cluster_number
# ENV cluster_number $cluster_number
# RUN /opt/odl/karaf-0.8.4/bin/configure_cluster.sh $cluster_number 172.19.0.2 172.19.0.3 172.19.0.4
CMD /opt/odl/karaf-0.8.4/bin/karaf