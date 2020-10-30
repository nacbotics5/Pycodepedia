import socket
#Client
# TCP Client Code
 
host="0.0.0.0"            # Set the server IP address
port = 33000               # Sets the variable port to 4444
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create socket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #prevents timeouts

sock.connect((host,port))# Connect to server address

print("Connected to Server !!!")
while True: 
    msg = sock.recv(1024)# Receives data upto 1024 bytes
    data = msg.strip().decode('ascii') 
    print("Message from server : " + data)
    response = input("Me ::")
    sock.send(response.encode("ascii"))
    

sock.close()# Closes the socket 
# End of code




