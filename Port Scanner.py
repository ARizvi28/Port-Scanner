import socket
import sys

targetip = input("Enter IP Address")
for i in range (1,1025):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  socket.setdefaulttimeout(0.8)
  res = sock.connect_ex((targetip, i))
  if res == 0:
    print(f"Port {i} is open")
  sock.close()
