FROM ubuntu:latest
# USER root
# WORKDIR /root
# RUN apt-get -y update && apt-get -y install git sudo apt-utils
# # RUN apt-get -y install git
# RUN git clone https://github.com/mininet/mininet
# # RUN cd mininet && git tag && git checkout -b mininet-2.3.0 2.3.0 && cd .. && mininet/util/install.sh -a
# RUN mininet/util/install.sh -a

# RUN apt-get -y update
RUN apt-get update && apt-get -y install mininet openvswitch-switch iproute2 iputils-ping
RUN apt-get update && apt-get -y install tcpdump netcat python3-pip
RUN pip install requests prettytable
#RUN apt-get install -y python-pip
COPY mininet/ENTRYPOINT.sh /
#RUN git clone https://github.com/mininet/mininet
# RUN cd mininet && git tag && git checkout -b mininet-2.3.0 2.3.0 && cd .. 
# RUN cd mininet && export PYTHONPATH=$PYTHONPATH:mininet:
# RUN PYTHON=python2 mininet/util/install.sh -n
#RUN mininet/util/install.sh -fw
# EXPOSE 6633 6653 6640
ENTRYPOINT ["/ENTRYPOINT.sh"]
# mininet/util/install.sh -fw
