import socket


def scan_ports(host, ports):
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
            scanner.settimeout(1)
            result = scanner.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
    return open_ports


if __name__ == "__main__":
    target_host = "127.0.0.1"
    target_ports = [22, 80, 443, 9999]
    print(scan_ports(target_host, target_ports))
