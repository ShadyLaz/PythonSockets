
import socket
import json


HOST = "10.180.55.54"
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

lines = socket.recv(1024).decode("UTF-8")

print(lines)

res = json.loads(lines)

print(type(res))
