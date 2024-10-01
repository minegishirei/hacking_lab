docker build . -t myclang
docker run --name myclang -it --rm -v ${PWD}/code:/code myclang bash
