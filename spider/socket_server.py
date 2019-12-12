#服务端
import socket
server = socket.socket()
server.bind(("0.0.0.0", 8888))
server.listen()

sock, addr=server.accept()
data = ""
while True:
    tmp_data = sock.recv(1024)
    if tmp_data:
        data += tmp_data.decode("utf8")
    else:
        break
print(data)
sock.close()