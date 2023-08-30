import sys
import threading
import time
import argparse
from video_chat import Video_Server, Video_Client, Audio_Server, Audio_Client

parser = argparse.ArgumentParser()

parser.add_argument('--host', type=str, default='127.0.0.1')
parser.add_argument('--port', type=int, default=10087)
parser.add_argument('--level', type=int, default=1)
parser.add_argument('-v', '--version', type=int, default=4)

args = parser.parse_args()

IP = args.host
PORT = args.port
VERSION = args.version
LEVEL = args.level
# IP = '10.194.44.22'
# PORT = 10087
# VERSION = 4
# LEVEL = 1

if __name__ == '__main__':
    vclient = Video_Client(IP, PORT, LEVEL, VERSION)
    vserver = Video_Server(PORT, VERSION)
    aclient = Audio_Client(IP, PORT + 1, VERSION)
    aserver = Audio_Server(PORT + 1, VERSION)
    vclient.start()
    aclient.start()
    time.sleep(1)  # make delay to start server
    vserver.start()
    aserver.start()
    while True:
        time.sleep(1)
        if not vserver.is_alive() or not vclient.is_alive():
            print("Video connection lost...")
            sys.exit(0)
        if not aserver.is_alive() or not aclient.is_alive():
            print("Audio connection lost...")
            sys.exit(0)
