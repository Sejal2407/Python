Output is in following drive link 
https://drive.google.com/drive/folders/1_nwCHTVcAB6zNQFYyklvDY59bb4T81Mh?usp=sharing

- First run the server.py 
-It will not show anything because it is waiting for the connection
- Then Run the client.py
- Client.py connect the socket connection to the server.py
- Now two windows of tkinter will display one for client and another one for server
- Send and receiver the messages from the respective buttons
- Type bye to disconnect and close both windows cleanly.


Key Socket Concepts

| Function | Purpose |
|----------|---------|
| socket() | Creates a new socket object |
| listen() | Puts the server in listening mode for incoming connections |
| accept() | Blocks until a client connects; returns the client socket |
| connect() | Connects the client socket to the server |
| send() | Sends data (must be converted to bytes first) |
| recv(n) | Receives up to n bytes of data |
| close() | Closes the socket and frees the port |