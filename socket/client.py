#coding=utf-8
from socket import *
tcpClientSocket=socket(AF_INET,SOCK_STREAM)
serAddr=('172.16.0.30',7788)
tcpClientSocket.connect(serAddr)#绑定服务器
while True:
        sendData=raw_input("send:")
        if len(sendData)>0:
                tcpClientSocket.send(sendData)
        else:
                break
        recvData=tcpClientSocket.recv(1024)
        print("recv:",recvData)
tcpClientSocket.close()
