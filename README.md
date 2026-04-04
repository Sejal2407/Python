Output is in following drive link 
https://drive.google.com/drive/folders/1_nwCHTVcAB6zNQFYyklvDY59bb4T81Mh?usp=sharing

 Socket Chat App — Tkinter GUI

A simple two-way chat application built with Python's `socket` and `tkinter` modules. Runs both the server and client on the same machine using the local hostname.

---

 How to Run
 Step 1 — Start the server first

python server.py


The server window will open and display:

--- Waiting for client to connect... ---


 Step 2 — Start the client (in a separate terminal)

python client.py

The client window will open and display:
```
--- Connected to server ---
```
The server window will also update to confirm the connection.

 Step 3 — Chat

- Type a message in the text box and press **Send** or hit **Enter**.
- Messages from the other side appear automatically — no need to click "Receive".
- Type `bye` to disconnect and close both windows cleanly.

---
- Both scripts must run on the **same machine** (they use the local hostname)

---

Key Socket Concepts

| Function | Purpose |
|----------|---------|
| socket() | Creates a new socket object |
| bind() | Binds the server socket to a hostname and port |
| listen() | Puts the server in listening mode for incoming connections |
| accept() | Blocks until a client connects; returns the client socket |
| connect() | Connects the client socket to the server |
| send() | Sends data (must be converted to bytes first) |
| recv(n) | Receives up to n bytes of data |
| close() | Closes the socket and frees the port |

---

 What Was Improved

- **Threading**: `receive_loop()` runs in a background daemon thread so messages arrive automatically without clicking a button.
- **`bye` exit condition**: Typing `bye` sends a disconnect signal and closes both sockets cleanly.
- **Socket cleanup**: `close()` is called on all sockets in a `close_connection()` function, triggered on exit or `bye`.
- **Error handling**: `try-except OSError` blocks wrap all socket operations to catch connection failures gracefully.
- **Buffer size**: Increased from 50 → 1024 bytes so longer messages are not truncated.
- **Enter key support**: Pressing Enter sends the message, same as clicking Send.