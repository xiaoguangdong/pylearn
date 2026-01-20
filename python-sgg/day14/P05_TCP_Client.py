"""
    该案例演示了TCP编程客户端
"""
import socket
# 创建socket对象
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立和服务器的连接
server_ip = '192.168.34.78'
server_port = 9999
socket_tcp.connect((server_ip, server_port))
# 循环
while True:
    # 向服务器发送数据
    socket_tcp.send(input(f"客户端>>服务器说:").encode('utf-8'))
    # 接收服务器返回的消息
    recv_data = socket_tcp.recv(1024)
    print(f"服务器>>客户端说:{recv_data.decode('utf-8')}")

# 关闭socket
socket_tcp.close()