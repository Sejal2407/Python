import socket
from tkinter import *

def send(entry,listbox):
    message = entry.get()
    listbox.insert('end',message)
    entry.delete(0, END)
    client.send(bytes(message, "utf-8"))
    recieve(listbox)

def recieve(listbox):
    reply = client.recv(50)
    listbox.insert('end',"Client : "+reply.decode("utf-8"))


root = Tk()
entry = Entry()
entry.pack(side = BOTTOM)

listbox = Listbox(root)
listbox.pack()

button = Button(root,text="Send",command = lambda : send(entry,listbox))
button.pack(side = BOTTOM)

rbutton = Button(root,text="Recieve",command = lambda : recieve(listbox))
rbutton.pack(side = BOTTOM)


root.title("Server")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME =  socket.gethostname()  #subsitute of IP address as we are going to use same deivce
#IP = 127.00

port = 8080

s.bind((HOST_NAME, port))

s.listen(4)
client, address = s.accept()
# while True:
#     message = input("Server : ")
#     # print("clients is connect and has the address ",address)
#     #client.send(bytes(message,"utf-8"))
#
#     reply = client.recv(50)
#     print("Cilent : ",reply.decode('UTF-8'))

root.geometry("350x250")
root.mainloop()
