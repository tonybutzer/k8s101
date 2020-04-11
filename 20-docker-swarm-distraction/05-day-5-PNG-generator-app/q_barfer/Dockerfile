FROM ubuntu:18.04
ENV theVersion 1.5

RUN apt-get update && apt-get install -y git && apt-get install -y make &&  apt-get -y install sudo && \
	apt-get install -y software-properties-common && \
	apt-get install -y vim && \
	apt-get install -y ca-certificates && \
	apt-get install -y python3-pip

# Fix an issue with libcurl...
RUN mkdir -p /etc/pki/tls/certs \
	&& ln -s /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt;

USER root
CMD /bin/bash


RUN mkdir -p /opt 
WORKDIR /opt


RUN git clone https://github.com/tonybutzer/npset

WORKDIR /opt/npset/mylib/playLib
RUN make build-root

ENV cloneVersion 1.5
RUN mkdir -p /opt/run
WORKDIR /opt/run
COPY requirements.txt /opt/run
RUN pip3 install -r requirements.txt
COPY q_barfer.py /opt/run
COPY sleepy.sh /opt/run
CMD ["/usr/bin/python3", "q_barfer.py"]
#CMD ["./sleepy.sh"]
