docker image build -t flask .
docker run -it -p 80:80 -v ./code:/code flask bash -c "python main.py"