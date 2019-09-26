# 服务端 server.py
# 客户端 client.py

import socket

s=socket.socket()  #实例化对象
host = socket.gethostname() #获取主机名
port = 12345

s.connect((host,port))  #连接

back = s.recv(1024)
back = back.decode()
print(back)

s.close()

