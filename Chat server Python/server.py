import socket
#server
# TCP Server Code
 
host="0.0.0.0"                # Set the server address to variable host
port=33000                   # Sets the variable port to 4444

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create socket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #prevents timeouts

sock.bind((host,port))# bind server address
sock.listen(1000) # Sets socket to listening state with a  queue of 1000 connection
print("Listening for connections.. ")
client,address = sock.accept()               # Accepts incoming request from client and returns
print(f"{address} just connected !!")

while True:                                    # socket and address to variables q and addr
    try:
        data = input("Enter data to be sent:  ")  # Data to be sent                                          # user
        client.send(data.encode("ascii")) # Sends data to client
    except:
        pass
    try:
        msg = client.recv(1024)# Receives data upto 1024 bytes
        print("Message from client : " + msg.strip().decode('ascii'))
    except Exception as e:
        print(e)
 
sock.close()
# End of code

