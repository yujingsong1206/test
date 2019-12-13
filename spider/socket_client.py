#客户端
import socket
client = socket.socket()
client.connect(("127.0.0.1",8888))

while True:
    input_data = input()
    client.send(input_data.encode("utf8"))
    if input_data == "#":
        break

client.close()