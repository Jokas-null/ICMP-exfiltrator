#!/usr/bin/python3

from scapy.all import *
import signal,sys

def def_handler(sig,frame):
	print("\n\n[!] Exit...\n")
	sys.exit(1)

#ctrl + c

signal.signal(signal.SIGINT, def_handler)

def data_parcer(packet):
	if packet.haslayer(ICMP):
		if packet[ICMP].type == 8:
			data = packet[ICMP].load[-4:].decode("utf-8")
			print(data, flush=True, end='')

if __name__ == '__main__':
	sniff(iface='eth0', prn=data_parcer)
