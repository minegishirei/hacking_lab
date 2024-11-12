
DIR_NAME=`pwd | xargs dirname`
docker run -it --network my_network -v ./code:/code -v ${DIR_NAME}/target:/target mykalilinux bash
