import socket
import time

# Mengatur server untuk menerima permintaan waktu dari klien
PORT = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('172.25.185.27', PORT))

print("Server started, waiting for client request...")

while True:
    # Menerima permintaan dari klien
    message, client_address = server_socket.recvfrom(1024)
    T2 = time.time()  # T2 - Waktu server menerima permintaan

    # Kirimkan T2 dan T3 (waktu pengiriman respons dari server)
    T3 = time.time()  # T3 - Waktu server mengirimkan respons
    server_socket.sendto(f"{T2},{T3}".encode(), client_address)
    print(f"Sent T2: {T2} and T3: {T3} to client {client_address}")