import sfml.network as sfn
import _thread
import string

def HandShake():
    tcpList = sfn.TcpListener()
    tcpList.listen(55002)
    tcpSock = sfn.TcpSocket()
    while(1):
        try:
            tcpSock=tcpList.accept()
            print("Connected to : "+tcpSock.remote_address.__str__())
            break
        except sf.SocketException as error:
            print("An error occured! Error: {0}".format(error))
            exit(1)
        

    while(1):
        message = tcpSock.receive(1024)
        print("1")
        print(tcpSock.remote_address.__str__()+" : "+message.decode('utf-8'))

#def Listen(Sock):

print("Vptre Adresse IP: {0}".format(sfn.IpAddress.get_local_address()))
_thread.start_new_thread(HandShake,())
print("Entrer la chaine de connection:")
inp = input()

ip = sfn.IpAddress.from_string(inp)
tcpSock = sfn.TcpSocket()
tcpSock.connect(ip,55001)
tcpSock.send("Hi, I am a client".encode('utf-8'))

while(1):
    inp = input()
    tcpSock.send(inp.encode('utf-8'))

#tcpSock = HandShake()



