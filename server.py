import socket
from tkinter import *

def send(entry,listbox):
    message = entry.get()
    listbox.insert('end',message)
    entry.delete(0, END)
    client.send(bytes(message, "utf-8"))
    if message == 'bye':
        client.close()
        s.close()
        root.destroy()
    else:
        recieve(listbox)

def recieve(listbox):
    reply = client.recv(1024)
    listbox.insert('end',"Client : "+reply.decode("utf-8"))
    if reply.decode("utf-8") == 'bye':
        client.close()
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

root.title("Server")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname() #subsitute of IP address as we are going to use same device
port = 8080

s.bind((HOST_NAME, port))
s.listen(4)

# accept() waits for client to connect
client, address = s.accept()

root.geometry("350x250")
root.mainloop()

s.close()
client.close()