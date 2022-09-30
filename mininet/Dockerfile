FROM ubuntu:latest
USER root
WORKDIR /root
RUN apt-get -y update
RUN apt-get -y install mininet openvswitch-switch iproute2 iputils-ping 
COPY mininet/ENTRYPOINT.sh /
# EXPOSE 6633 6653 6640
ENTRYPOINT ["/ENTRYPOINT.sh"]
