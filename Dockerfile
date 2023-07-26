FROM ubuntu:focal

RUN apt-get upgrade -y && apt-get update -y

RUN apt-get install -y python3 python3-pip git

WORKDIR /detector-script-tesis

RUN cd /detector-script-tesis

RUN git clone https://github.com/ViceAguilera/detector-script-tesis.git .

