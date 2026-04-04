import socket
from tkinter import *

def send(entry,listbox):
    message = entry.get()
    listbox.insert('end',message)
    entry.delete(0, END)
    s.send(bytes(message, "utf-8"))
    recieve(listbox)

def recieve(listbox):
    reply = s.recv(50)
    listbox.insert('end',"Server : "+reply.decode("utf-8"))


root = Tk()
entry = Entry()
entry.pack(side = BOTTOM)

listbox = Listbox(root)
listbox.pack()

button = Button(root,text="Send",command = lambda : send(entry,listbox))
button.pack(side = BOTTOM)

rbutton = Button(root,text="Recieve",command = lambda : recieve(listbox))
rbutton.pack(side = BOTTOM)

root.title("Client")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST_NAME = socket.gethostname() #subsitute of IP address as we are going to use same device
PORT = 8080

s.connect((HOST_NAME,PORT))
#100 is buffer size , size of chunks
# msg = s.recv(10)
# msg1 = s.recv(10)
# print(msg.decode('utf-8'))
# print(msg1.decode('utf-8'))

# while True:
#     message = ''
#     while True:
#         msg = s.recv(10)
#         if len(msg)<=0:
#             break
#         message += msg.decode('UTF-8')
#     if len(message)>0:
#         print(message)

# while True:
#     message = s.recv(50)
#     print("Server : ",message.decode('UTF-8'))
#
#     reply = input ("Client : ")
#     s.send(bytes(reply,'UTF-8'))

root.geometry("350x250")
root.mainloop()



