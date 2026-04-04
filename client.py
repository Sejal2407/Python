import socket
import threading
from tkinter import *
from tkinter import messagebox


def send(entry, listbox):
    message = entry.get().strip()
    if not message:
        return

    listbox.insert('end', "You: " + message)
    entry.delete(0, END)

    try:
        s.send(bytes(message, "utf-8"))
    except OSError:
        messagebox.showerror("Error", "Failed to send message. Connection may be closed.")
        return

    # Close connection cleanly if user types 'bye'
    if message.lower() == 'bye':
        close_connection()


def receive_loop(listbox):
    while True:
        try:
            reply = s.recv(1024)
            if not reply:
                break
            decoded = reply.decode("utf-8")
            listbox.insert('end', "Server: " + decoded)

            # If server says bye, close gracefully
            if decoded.lower() == 'bye':
                listbox.insert('end', "--- Server disconnected ---")
                close_connection()
                break
        except OSError:
            break


def close_connection():
    try:
        s.close()
    except OSError:
        pass
    root.quit()


# --- GUI setup ---
root = Tk()
root.title("Client")
root.geometry("400x350")
root.resizable(False, False)

listbox = Listbox(root, width=55, height=18)
listbox.pack(padx=10, pady=10)

entry = Entry(root, width=40)
entry.pack(side=LEFT, padx=(10, 5), pady=(0, 10))

button = Button(root, text="Send", command=lambda: send(entry, listbox))
button.pack(side=LEFT, pady=(0, 10))

# Allow Enter key to send messages
root.bind('<Return>', lambda event: send(entry, listbox))

# --- Socket setup ---
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()  # Use hostname instead of IP for local communication
PORT = 8080

try:
    s.connect((HOST_NAME, PORT))
    listbox.insert('end', "--- Connected to server ---")

    # Start background thread to receive messages without blocking the GUI
    thread = threading.Thread(target=receive_loop, args=(listbox,), daemon=True)
    thread.start()

except OSError as e:
    messagebox.showerror("Connection Error", f"Could not connect to server:\n{e}")
    root.quit()

root.protocol("WM_DELETE_WINDOW", close_connection)
root.mainloop()