import socket
from collections import defaultdict
import sys
sys.path.append("..")
from global_config import *

online_clients = {}
chat_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (get_value('server_address'), get_value('server_port'))

# Create a defaultdict to store user mailboxes (offline messages)
user_mailboxes = defaultdict(list)