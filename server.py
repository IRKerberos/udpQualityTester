# -*- coding: utf-8 -*-
import socket
import requests

def prRed(skk,end='\n'): print("\033[91m {}\033[00m".format(skk),end=end)
def prGreen(skk,end='\n'): print("\033[92m {}\033[00m".format(skk),end=end)
def prYellow(skk,end='\n'): print("\033[93m {}\033[00m".format(skk),end=end)
def prLightPurple(skk,end='\n'): print("\033[94m {}\033[00m".format(skk),end=end)
def prPurple(skk,end='\n'): print("\033[95m {}\033[00m".format(skk),end=end)
def prCyan(skk,end='\n'): print("\033[96m {}\033[00m".format(skk),end=end)
def prLightGray(skk,end='\n'): print("\033[97m {}\033[00m".format(skk),end=end)
def prBlack(skk,end='\n'): print("\033[98m {}\033[00m".format(skk),end=end)

def connection(port,packetsize):
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.listen(1)
    tcp_sock.bind(("127.0.0.1", port))
    udp_sock.bind(("127.0.0.1", port))
    while True:
        tcp_data, tcp_addr = tcp_sock.accept()
        tcp_data_sent_client = str(tcp_sock.recv(packetsize))
        udp_data, udp_addr = udp_sock.recvfrom(packetsize)
        udp_data_sent_client = str(udp_data.decode())
        udp_sock.sendto(udp_data_sent_client, udp_addr)
        tcp_sock.send(tcp_data_sent_client,tcp_addr)


def welcome():
    welcome_message = """
    ┓ ┏┏┓┓ ┏┓┏┓┳┳┓┏┓   ┏┳┓┏┓    ┳┳ ┳┓ ┏┓  ┏┓┳┳┏┓┓ ┳┏┳┓┓┏  ┏┳┓┏┓┏┓┏┳┓┏┓┳┓  ┏┓┏┓┳┓┓┏┏┓┳┓╹╹
    ┃┃┃┣ ┃ ┃ ┃┃┃┃┃┣     ┃ ┃┃    ┃┃ ┃┃ ┃┃  ┃┃┃┃┣┫┃ ┃ ┃ ┗┫   ┃ ┣ ┗┓ ┃ ┣ ┣┫  ┗┓┣ ┣┫┃┃┣ ┣┫  
    ┗┻┛┗┛┗┛┗┛┗┛┛ ┗┗┛    ┻ ┗┛    ┗┛ ┻┛ ┣┛  ┗┻┗┛┛┗┗┛┻ ┻ ┗┛   ┻ ┗┛┗┛ ┻ ┗┛┛┗  ┗┛┗┛┛┗┗┛┗┛┛┗  
    """

    prCyan(welcome_message)
    port = 0
    packetsize = 0
    while True:
        try:
            prYellow("Please Enter The Port (note that this port must be open and no service is running on it!) : ",
                     end="")
            port = int(input())
            break
        except:
            prRed("Invalid Port!")

    while True:
        try:
            prYellow("Please send the size of each packet (1-1460) : ", end="")
            packetsize = int(input())
            break
        except:
            prRed("Invalid Packet Size!")

    return port,packetsize

welcome()