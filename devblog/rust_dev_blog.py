import os 
import sys
import time
import requests
import subprocess
import shutil

freq = 800
Dur = 150

if(len(sys.argv) > 1):
    DEVBLOG_URL = 'devblog-{0}'.format(sys.argv[1])
else:
    print("Error: no dev blog specified, use format:")
    print("$python devblog.py 142")
    sys.exit()

if __name__ == '__main__':
    status = 0
    url = 'http://playrust.com/{0}'.format(DEVBLOG_URL)
    print('Requesting {0}...'.format(url))
    while status != 200:
        req = requests.get(url)
        status = req.status_code

        if status == 200:
            for i in range(0,10):
                print('DEVBLOG IS LIVE')
            print('\7')
                
        else:
            print('...')
            time.sleep(10)
