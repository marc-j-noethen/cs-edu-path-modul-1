import socket


HOST = "example.com"
PORT = 80


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Client: Socket erstellt.")

    try:
        ip_address = socket.gethostbyname(HOST)
        print(f"Client: Verbinde zu {ip_address}:{PORT}...")
        client_socket.connect((HOST, PORT))
        print("Client: Verbunden!")

        request = (
            "GET / HTTP/1.1\r\n"
            f"Host: {HOST}\r\n"
            "Connection: close\r\n"
            "\r\n"
        )
        client_socket.sendall(request.encode())

        response_parts = []
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            response_parts.append(data)

        print(b"".join(response_parts).decode(errors="replace"))
    finally:
        client_socket.close()
        print("Client: Socket geschlossen.")


if __name__ == "__main__":
    main()
