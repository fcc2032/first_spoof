from scapy.all import *

ip = IP(src='8.8.8.8', dst='10.9.0.1')
icmp = ICMP()
packet = ip/icmp
packet.show()
send(packet)