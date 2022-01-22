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

#questions and answers respectively
questions = [" What's the national flower of Malaysian? \n A.Cherry blossom B.Hibiscus C.Rose D.Lily",
             " What's the national animal of Malaysian? \n A.Kangaroo B.Elephant C.Lion D.Tiger",
             " Which state has the highest concentration of rafflesia? \n A.Sarawak B.Pahang C.Sabah D.Johor",
             " Which of the following is more than 0.35 but less than 0.41? \n A.8/25 B.3/10 C.2/5 D.9/26",
             " 106 x 106 - 94 x 94 = ? \n A.2004 B.2400 C.1904 D.1906",
             " Which of the following is not greater than 7/16? \n A.3/8 B.1/2 C.31/62 D.15/17",
             " The brain of any computer system is.. \n A.ALU B.Memory C.CPU D.Control Unit",
             " The two kinds of main memory are: \n A.Primary&Secondary B.ROM&RAM C.Random&Sequential D.All",
             " The two major types of computer chips are: \n A.Both B&C B.Primary memory chip C.Microprocessor chip D.External memory chip",
             " The Olympics are held every how many years? \n A.1 years B.2 years C.3 yeasr D.4 years",
             " Which football team is known as 'The Red Devils'?  \n A.Manchester United B.Liverpool C.None of them D.Chelsea",
             " Which country has won the most World Cups? \n A.England B.Belgium C.Brazil D.Italy",
             " Name Disney's first film? \n A.Frozen B.Cinderella C.Mulan D.Snow White",
             " What is Mjolnir? \n A.Loki's Scepter B.Thor's Hammer C.Captain America's Shield D.Winter Soldier's Arm",
             " What is the closest planet to the Sun? \n A.Mercury B.Saturn C.Jupiter C.Mars",
             " Electric current is measured using what device? \n A.Voltage B.Ammater C.Ohm D.Watts",
             " True or false? Batteries convert chemical to electrical energy. \n A.True B.False"]

answers = ['B', 'D', 'C', 'C', 'B', 'A', 'C', 'B', 'A', 'D', 'A', 'C', 'D', 'B', 'A', 'B', 'A']
