"""
    该案例演示了udp服务器端
"""
import socket
# 创建socket对象
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定ip和端口号
socket.bind(('127.0.0.1', 8888))
# 循环
while True:
    # 接收客户端数据
    recv_data,client_info = socket.recvfrom(1024)
    print(f"客户端{client_info[0]}说:{recv_data.decode('utf-8')}")
    # 向客户端发送数据
    socket.sendto("你好".encode('utf-8'), client_info)
# 关闭套接字socket对象
socket.close()