import socket


def get_ip():
    return socket.gethostbyname_ex(socket.gethostname())


def test_node_info():
    my_ip = get_ip()
    print(my_ip)
