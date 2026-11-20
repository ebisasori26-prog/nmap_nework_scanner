
import nmap

scanner = nmap.PortScanner()

target = input("Enter target IP address: ")

print("Scanning target:", target)

scanner.scan(target, arguments="-p 1-1024")

for host in scanner.all_hosts():

    print("Host:", host)
    print("Status:", scanner[host].state())

    for protocol in scanner[host].all_protocols():

        print("Protocol:", protocol)

        ports = scanner[host][protocol].keys()

        for port in ports:

            print("Port:", port)
            print("State:", scanner[host][protocol][port]['state'])

print("Scanning completed!")
