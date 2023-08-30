import socket
from collections import defaultdict

online_clients = {}
chat_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_ip = '10.194.149.248'
server_address = ('127.0.0.1', 13579)

# Create a defaultdict to store user mailboxes (offline messages)
user_mailboxes = defaultdict(list)
system_name = None