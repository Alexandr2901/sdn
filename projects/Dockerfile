FROM ubuntu:14.04
RUN apt-get -y update &&  apt-get -y install git 
RUN git clone https://github.com/mininet/oflops.git
RUN git clone https://github.com/mininet/openflow

# RUN apt-get install -y libsnmp-dev libpcap-dev autoconf
# RUN apt-get install -y libtool 
# RUN apt-get install -y libconfig++-dev

RUN apt-get install -y autoconf automake libtool libsnmp-dev libpcap-dev
WORKDIR oflops
RUN apt-get install -y make libconfig8-dev

RUN sh boot.sh 
RUN ./configure --with-openflow-src-dir=/openflow
# RUN sh boot.sh          #   if no ./configure file
# RUN ./configure --with-openflow-src-dir=/path/to/openflow
RUN make
# RUN make docs           # build API documentation in ./doc
RUN make install
CMD /bin/bash

# cbench -c 172.16.0.2
