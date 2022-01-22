import socket
import threading
import sys
import random

#AF_INET is address of socket
#SOL_SOCKET is the type of socket
#SOCK_STREAM means using TCP socket and the data & character read in sequence
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#checking server and size of the argument
if len(sys.argv) != 3:
    print ("Print : script, IP address, port number")
    exit()

#first argument of string act as IP Address
IP_address = str(sys.argv[1])
#second argument become the port number
Port = int(sys.argv[2])

#value that client need to alert
server.bind((IP_address, Port))
server.listen(100)
