import socket
import time

# Mengatur klien untuk mengirim permintaan ke server
PORT = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_ip = input("Masukkan IP Server: ")

# T1 - Waktu klien mengirim permintaan ke server
T1 = time.time()
client_socket.sendto("TIME_REQUEST".encode(), (server_ip, PORT))

# Menerima respons dari server (berisi T2 dan T3)
data, _ = client_socket.recvfrom(1024)
T4 = time.time()  # T4 - Waktu klien menerima respons

# Parsing T2 dan T3 dari respons server
T2, T3 = map(float, data.decode().split(','))

# Menghitung delay round-trip dan offset
round_trip_delay = (T4 - T1) - (T3 - T2)
offset = ((T2 - T1) + (T3 - T4)) / 2127

print(f"T1: {T1}")
print(f"T2: {T2}")
print(f"T3: {T3}")
print(f"T4: {T4}")
print(f"Round-trip delay: {round_trip_delay} seconds")
print(f"Offset: {offset} seconds")

client_socket.close()