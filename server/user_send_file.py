import socket
import os
def receive_file(connection, filename):
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)  # 创建文件夹路径
        with open(filename, 'xb') as file:
            while True:
                data = connection.recv(4096)
                if not data:
                    break
                file.write(data)
        print(f"File '{filename}' received and saved")
    except FileExistsError:
        print(f"File '{filename}' already exists")
    except Exception as e:
        print("An error occurred:", e)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(1)

    print("Server listening on port 12345")

    client_socket, client_address = server_socket.accept()
    print("Connected by", client_address)

    filename = "files/package.zip"
    receive_file(client_socket, filename)
    print(f"File '{filename}' received")

    client_socket.close()

if __name__ == "__main__":
    main()
