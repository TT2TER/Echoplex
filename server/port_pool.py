import random


def create_port_pool(start, end):
    return list(range(start, end + 1))


def take_port(port_pool):
    if port_pool:
        index = random.randint(0, len(port_pool) - 1)
        return port_pool.pop(index)
    else:
        print("Port pool is empty.")
        return None


def return_port(port_pool, port):
    if port in range(port_pool[0], port_pool[-1] + 1):
        port_pool.append(port)
    else:
        print(f"Port {port} is out of range or not taken.")


# def main():
#     port_pool = create_port_pool(13560, 13569)
#
#     taken_ports = []
#     for _ in range(5):
#         port = take_port(port_pool)
#         if port is not None:
#             taken_ports.append(port)
#
#     print("Taken ports:", taken_ports)
#
#     for port in taken_ports:
#         return_port(port_pool, port)
#
#
# if __name__ == "__main__":
#     main()
