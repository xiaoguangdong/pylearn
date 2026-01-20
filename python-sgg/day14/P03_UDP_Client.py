"""
    该案例演示了udp客户端
"""
import socket
# 创建socket对象
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 循环
while True:
    # 向服务器发送消息
    server_ip = "127.0.0.1"
    server_port = 8888
    socket.sendto(input("客户端说:").encode("utf-8"), (server_ip, server_port))
    # 接收服务器消息
    recv_data,server_info = socket.recvfrom(1024)
    print(f"服务器{server_info[0]}说:{recv_data.decode('utf-8')}")
# 关闭socket对象
socket.close()
