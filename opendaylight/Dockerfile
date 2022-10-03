FROM ubuntu:latest
RUN apt-get -y update && apt install -y openjdk-8-jre wget zip 
RUN mkdir /opt/odl
RUN wget -O /opt/odl/odl.zip https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/karaf/0.8.4/karaf-0.8.4.zip
# RUN tar -xzf /opt/odl/odl.tar.zip -C /opt/odl/
RUN unzip /opt/odl/odl.zip -d /opt/odl

# RUN mv /opt/odl/dist* -d /opt/odl/boron
# CMD /opt/odl/boron/bin/karaf
EXPOSE 8181 6633 8101

# RUN apt-get -y install expect

# COPY opendaylight/install.exp /opt/odl/install.exp

# RUN chmod +x /opt/odl/install.exp
# RUN /opt/odl/install.exp
# RUN ls -l opt/odl/karaf-0.8.4/etc/org.apache.karaf.features.cfg

RUN echo "featuresBoot = 8da8bcd0-dacc-440e-bd40-cf2f893c2284,odl-dlux-core,odl-dluxapps-nodes,odl-dluxapps-topology,\
odl-dluxapps-yangui,odl-dluxapps-yangvisualizer,odl-dluxapps-yangman, \
odl-restconf,odl-l2switch-switch,odl-mdsal-apidocs,odl-mdsal-distributed-datastore" >> opt/odl/karaf-0.8.4/etc/org.apache.karaf.features.cfg
# grep "featuresBoot = " opt/odl/karaf-0.8.4/etc/org.apache.karaf.features.cfg


# RUN /opt/odl/karaf-0.8.4/bin/karaf 
# RUN /opt/odl/karaf-0.8.4/bin/start
# RUN /opt/odl/karaf-0.8.4/bin/client
CMD /opt/odl/karaf-0.8.4/bin/karaf
# ENTRYPOINT ["ls", "/opt/odl/karaf-0.8.0/bin/karaf"]

# ssh -p 8101 karaf@localhost 
# featuresBoot=odl-dlux-core
