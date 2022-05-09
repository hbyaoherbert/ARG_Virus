import os

for filename in os.listdir('crcoutput'):
    print(filename.split('.')[0])
