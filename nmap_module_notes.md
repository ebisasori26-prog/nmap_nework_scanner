\# Assignment 3: Read About the Nmap Module



Nmap (Network Mapper) is a tool used to discover devices connected to a network and identify open ports and services running on those devices.



The Python Nmap module (`python-nmap`) allows programmers to use Nmap through Python code instead of typing every command manually in the terminal.



It makes network scanning easier because we can write Python programs to scan a target, check its status, identify open ports, and collect information about network services.



\### Important Functions of the Python Nmap Module



1\. `nmap.PortScanner()` – Creates a scanner object.

2\. `scan()` – Starts scanning a target IP address.

3\. `all\_hosts()` – Returns the hosts discovered during scanning.

4\. `state()` – Checks whether a host is up or down.

5\. `all\_protocols()` – Returns the protocols found, such as TCP and UDP.



\### Example



```python

import nmap



scanner = nmap.PortScanner()



scanner.scan("127.0.0.1", arguments="-p 1-100")



print(scanner.all\_hosts())

```



In this example, Python uses the Nmap module to scan ports 1 to 100 on the local computer.



\### Conclusion



The Python Nmap module helps us automate network scanning using Python. It is useful for network discovery, port scanning, and identifying services running on network devices.



\*\*Note:\*\* The Python package alone is not enough; the Nmap application must also be installed on the computer.

