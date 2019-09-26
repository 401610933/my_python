# 服务端 server.py
# 客户端 client.py

import socket

s = socket.socket() #实例化对象
host = socket.gethostname()  #获取本地主机名
port = 12345 #设置端口
s.bind((host,port)) #绑定端口

s.listen(5) #等待通讯连接

while True:
    c,addr=s.accept()  #建立客户端连接
    print('地址:',addr)
    str = "欢迎访问我的链接"
    str = str.encode()
    c.send(str)
    c.close()  #关闭