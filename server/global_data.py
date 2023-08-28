import socket
from collections import defaultdict

online_clients = {}
chat_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 13579)

# Create a defaultdict to store user mailboxes (offline messages)
user_mailboxes = defaultdict(list)