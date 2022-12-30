import socket
import pyfiglet

# Use pyfiglet to print a banner
banner = pyfiglet.figlet_format("Port Scanner", font="slant")
print(banner)


# Prompt user for target IP address
target_ip = input("Enter the Target IP address: ")


# Prompt user for range of ports to scan
start_port = int(input("Enter the Starting Port: "))
end_port = int(input("Enter the Ending Port: "))


#Scan the specified range of ports
for port in range(start_port, end_port+1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        print(f"Port {port}: OPEN")
    sock.close()