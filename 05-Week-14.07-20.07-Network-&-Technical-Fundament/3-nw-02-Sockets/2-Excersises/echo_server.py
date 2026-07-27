import socket

HOST = "0.0.0.0"
PORT = 9999


def main():
    server_socket = None
    conn = None

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server is listening on {HOST}:{PORT}...")

        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        data = conn.recv(1024)
        print(f"Received: {data.decode(errors='replace')}")

        conn.sendall(data)
        print("Echo sent back to client.")

    except socket.error as error:
        print(f"Socket error: {error}")
    finally:
        if conn is not None:
            conn.close()
        if server_socket is not None:
            server_socket.close()
        print("Server socket closed.")


if __name__ == "__main__":
    main()
