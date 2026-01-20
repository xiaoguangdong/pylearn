"""
    该案例演示了TCP编程服务器端
"""
import random
import threading

"""
# 服务器端最基本的实现
import socket

# 创建socket对象
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定ip和端口
socket_tcp.bind(('0.0.0.0', 9999))
# 设置监听 监听客户端请求
socket_tcp.listen(5)
# 等待客户端连接
socket_client,client_info =  socket_tcp.accept()
# 循环
while True:
    # 接收客户端发送的消息
    recv_data = socket_client.recv(1024)
    print(f"客户端{client_info[0]}说:{recv_data.decode('utf-8')}")

    # 向客户端发送消息
    socket_client.send("你好".encode('utf-8'))
# 关闭socket
socket_client.close()
socket_tcp.close()
"""
"""
# 优化1：让服务器回话更丰富一些
import socket

# 创建socket对象
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定ip和端口
socket_tcp.bind(('127.0.0.1', 9999))
# 设置监听 监听客户端请求
socket_tcp.listen(5)
# 等待客户端连接
socket_client,client_info =  socket_tcp.accept()
# 循环
while True:
    # 接收客户端发送的消息
    recv_data = socket_client.recv(1024)
    print(f"客户端{client_info[0]}说:{recv_data.decode('utf-8')}")

    # 向客户端发送消息
    data_list = ["你好","在呢，同学","你还在吗","是不是想要资料","要咨询大模型课程码","扫描右下角二维码加v"]

    socket_client.send(data_list[random.randint(0,len(data_list) - 1)].encode('utf-8'))
# 关闭socket
socket_client.close()
socket_tcp.close()
"""
"""
# 优化2：让服务器也在控制台输入回话内容
import socket

# 创建socket对象
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定ip和端口
socket_tcp.bind(('0.0.0.0', 9999))
# 设置监听 监听客户端请求
socket_tcp.listen(5)
# 等待客户端连接
socket_client,client_info =  socket_tcp.accept()
# 循环
while True:
    # 接收客户端发送的消息
    recv_data = socket_client.recv(1024)
    print(f"客户端{client_info[0]}说:{recv_data.decode('utf-8')}")

    # 向客户端发送消息
    socket_client.send(input(f"服务器>>客户端{client_info[0]}说:").encode('utf-8'))
# 关闭socket
socket_client.close()
socket_tcp.close()
"""
# 优化3： 在程序中加入异常处理以及多线程
import socket

# 处理客户端请求
def func(socket_client,client_info):
    try:
        # 循环
        while True:
            # 接收客户端发送的消息
            recv_data = socket_client.recv(1024)
            if not recv_data:
                break
            print(f"客户端{client_info[0]}说:{recv_data.decode('utf-8')}")
            # 向客户端发送消息
            socket_client.send(input(f"服务器>>客户端{client_info[0]}说:").encode('utf-8'))
    except Exception as e:
        print(f"和客户端{client_info[0]}通信的时候发生了异常~")
    finally:
        socket_client.close()

def main():
    # 创建socket对象
    socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定ip和端口
    socket_tcp.bind(('0.0.0.0', 9999))
    # 设置监听 监听客户端请求
    socket_tcp.listen(70)

    while True:
        # 等待客户端连接
        socket_client,client_info =  socket_tcp.accept()
        # 为每一个连接的客户端 单独开一个线程  进行处理
        threading.Thread(target=func,args=(socket_client,client_info)).start()

    # 关闭socket
    socket_tcp.close()

if __name__ == "__main__":
    main()