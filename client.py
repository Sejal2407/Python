import socket
from tkinter import *

def send(entry,listbox):
    message = entry.get()
    listbox.insert('end',message)
    entry.delete(0, END)
    s.send(bytes(message, "utf-8"))
    if message == 'bye':
        s.close()
        root.destroy()
    else:
        recieve(listbox)

def recieve(listbox):
    reply = s.recv(1024)
    listbox.insert('end',"Server : "+reply.decode("utf-8"))
    if reply.decode("utf-8") == 'bye':
        s.close()
        root.destroy()


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

root.geometry("350x250")
root.mainloop()

s.close()