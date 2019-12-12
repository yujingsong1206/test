#客户端
import socket
client = socket.socket()
client.connect(("127.0.0.1",8888))

client.send(b"hello")
client.send("client".encode("utf8"))
client.close()