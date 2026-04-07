
#!/usr/bin/env python

from scapy.all import DNS, DNSQR, IP, sr1, UDP

import sys

SERVER_IP = "cs177.seclab.cs.ucsb.edu"
DOMAIN="amplifiedsecurity.com"

def main():
    if len(sys.argv) != 2:
        print("Usage: python dns_amplify.py <port>")
        return 1 

    port = int(sys.argv[1])

    packet = IP(dst=SERVER_IP) / UDP(dport=port) / DNS(qd=DNSQR(qname=DOMAIN, qtype=255))

    response = sr1(packet, verbose=0)

    if response:
        response.show()

    request_size = len(packet)
    response_size = len(response) if response else 0

    print(f"Request Size: {request_size}")
    print(f"Response Size: {response_size}")
    print(f"Amplification: {response_size / request_size:.2f}")
    
if __name__ == "__main__":
    main()
