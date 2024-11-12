FROM kalilinux/kali-rolling

RUN apt-get update -y
RUN apt-get install -y metasploit-framework
RUN apt-get install -y iputils-ping net-tools
RUN apt-get install -y golang-go
RUN apt-get install -y w3m
RUN apt-get install -y nikto
RUN apt-get install -y sqlmap

RUN apt-get update -y
RUN apt-get install -y python3-pip --fix-missing
RUN pip install bandit --break-system-packages


