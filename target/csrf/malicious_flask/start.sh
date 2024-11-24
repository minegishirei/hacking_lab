docker image build -t flask .
docker run -it -p 10404:10404 -v ./code:/code flask bash -c "python main.py"