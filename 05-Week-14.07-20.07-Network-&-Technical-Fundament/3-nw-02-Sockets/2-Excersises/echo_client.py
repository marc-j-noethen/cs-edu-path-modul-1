import socket

HOST = "127.0.0.1"
PORT = 9999
MESSAGE = "Hello Echo Chamber!"


def main():
    client_socket = None

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Client socket created.")
        print(f"Connecting to {HOST}:{PORT}...")

        client_socket.connect((HOST, PORT))
        print("Client connected.")

        client_socket.sendall(MESSAGE.encode())
        print(f"Sent: {MESSAGE}")

        data = client_socket.recv(1024)
        print(f"Server echoed: {data.decode(errors='replace')}")

    except socket.error as error:
        print(f"Socket error: {error}")
    finally:
        if client_socket is not None:
            client_socket.close()
        print("Client socket closed.")


if __name__ == "__main__":
    main()
