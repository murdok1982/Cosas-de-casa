import socket

def scan_ports(host, start, end):
    open_ports = []
    for port in range(start, end):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
            print(f"Port {port} is open")
        sock.close()
    return open_ports

host = "192.168.1.1/24"
open_ports = scan_ports(host, 1, 65535)
print(f"Open ports on {host}: {open_ports}")
