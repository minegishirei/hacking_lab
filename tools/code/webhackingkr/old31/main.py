import os

for i in range(10000,10100):
    os.system("nc -l {} &".format(i))
