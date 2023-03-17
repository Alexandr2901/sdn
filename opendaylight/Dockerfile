FROM ubuntu:latest
RUN apt-get -y update && apt install -y openjdk-8-jre wget zip 
RUN mkdir /opt/odl
RUN wget -O /opt/odl/odl.zip https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/karaf/0.8.4/karaf-0.8.4.zip
RUN unzip /opt/odl/odl.zip -d /opt/odl
WORKDIR /opt/odl/karaf-0.8.4/bin
RUN ./set_persistence.sh off 
RUN apt-get -y update && apt-get install -y tcpdump dnsutils iputils-ping net-tools
RUN echo "feature:install odl-restconf odl-l2switch-switch odl-mdsal-apidocs http odl-mdsal-distributed-datastore odl-dluxapps-applications odl-dluxapps-nodes odl-dluxapps-topology odl-dluxapps-yangui odl-dluxapps-yangvisualizer odl-dluxapps-yangman odl-dluxapps-yangutils && logout" | ./karaf
RUN rm /opt/odl/odl.zip 
COPY opendaylight/ENTRYPOINT.sh /
ENTRYPOINT ["/ENTRYPOINT.sh"]
