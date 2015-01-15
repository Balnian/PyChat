import sfml.network as sfn
import _thread
import string
#import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText

def HandShake(root):
    tcpList = sfn.TcpListener()
    tcpList.listen(55001)
    w = Label(root, text="Port Locale : {0}".format(tcpList.local_port.__str__()))
    w.pack()
    MyText = ScrolledText(root)
    MyText.pack()
    print("Port Locale : {0}".format(tcpList.local_port.__str__()))
    tcpSock = sfn.TcpSocket()
    while(1):
        try:
            tcpSock=tcpList.accept()
            print("Connected to : "+tcpSock.remote_address.__str__())
            break
        except sf.SocketException as error:
            print("An error occured! Error: {0}".format(error))
            exit(1)
        
    message=[]
    while(1):
        message.append(tcpSock.receive(1024))
       # print("1")
        #print(tcpSock.remote_address.__str__()+" : "+message.decode('utf-8'))
        MyText = ScrolledText(root,width=300)
        MyText.pack()
        for i in range(message.__len__):
            MyText.insert(END,message(i))


#def Listen(Sock):

root = Tk()
#ViewFrame = Frame(root)
#Screen = ScrolledText(root)
#Screen.pack()
w = Label(root, text="allo")
w.pack()

print("Vptre Adresse IP: {0}".format(sfn.IpAddress.get_local_address()))
_thread.start_new_thread(HandShake,(root,))

print("Entrer la chaine de connection:")
inp = input()

ip = sfn.IpAddress.from_string(inp)
tcpSock2 = sfn.TcpSocket()
tcpSock2.connect(ip,55001)

tcpSock2.send("Hi, I am a client".encode('utf-8'))

#while(1):
inp = input()
tcpSock2.send(inp.encode('utf-8'))
root.mainloop()

#tcpSock = HandShake()



