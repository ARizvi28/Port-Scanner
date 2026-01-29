import socket
import sys

targetip = "127.0.0.1"
for i in range (1,1025):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  socket.setdefaulttimeout(0.8)
  res = sock.connect_ex((targetip, i))
  if res == 0:
    print(f"Port {i} is open")
  sock.close()
