import socket

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
print("Bilgisayar ismi : "+ hostname)
print("IP Address : " +IP)
