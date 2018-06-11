from socket import *

tcpSerSocket=socket(AF_INET,SOCK_STREAM)
address=('',7788)
tcpSerSocket.bind(address)#绑定端口号
tcpSerSocket.listen(5)
while True:
        newSocket,clientAddr=tcpSerSocket.accept()
        while True:
                recvData=newSocket.recv(1024)
                if len(recvData)>0:
                        print("recv:",recvData)
                else:
                        break
                sendData=raw_input("send:")
                newSocket.send(sendData)
        newSocket.close()
tcpSerSocket.close()
