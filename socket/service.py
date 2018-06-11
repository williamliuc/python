from socket import *

#创建socket
tcpSerSocket=socket(AF_INET,SOCK_STREAM)

#绑定本地信息
address=('',7788)
tcpSerSocket.bind(address)#绑定端口号

#使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的

tcpSerSocket.listen(5)
while True:
        
        #如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
        #newSocket用来为这个客户端服务
        #tcpSerSocket就可以省下来专门等待其他新客户端的链接
        newSocket,clientAddr=tcpSerSocket.accept()
        while True:
                
                #就收对方发送过来的数据，最大接收1024个字节
                recvData=newSocket.recv(1024)
                if len(recvData)>0:
                        print("recv:",recvData)
                else:
                        break
                       
                #返回发送一些数据
                sendData=raw_input("send:")
                newSocket.send(sendData)
        
        #关闭为这个客户端服务的套接字
        newSocket.close()
        
#关闭监听套接字
tcpSerSocket.close()
