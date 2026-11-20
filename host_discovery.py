import socket
import subprocess
import ipaddress

# Get gateway IP
result = subprocess.check_output(
    "ip route | grep default",
    shell=True
).decode()

gateway = result.split()[2]

print("Gateway IP:", gateway)

# Get local IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((gateway, 80))

local_ip = s.getsockname()[0]
s.close()

print("Local IP:", local_ip)

# Determine IP class
first_octet = int(local_ip.split('.')[0])

if 1 <= first_octet <= 126:
    ip_class = "Class A"
elif 128 <= first_octet <= 191:
    ip_class = "Class B"
elif 192 <= first_octet <= 223:
    ip_class = "Class C"
elif 224 <= first_octet <= 239:
    ip_class = "Class D"
else:
    ip_class = "Class E"

print("IP Class:", ip_class)

# Discover active hosts
network = ipaddress.ip_network(local_ip + "/24", strict=False)

print("\nDiscovering hosts...")

for ip in network.hosts():
    response = subprocess.call(
        ["ping", "-c", "1", "-W", "1", str(ip)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if response == 0:
        print("Active Host:", ip)