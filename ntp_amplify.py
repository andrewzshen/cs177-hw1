#!/usr/bin/env python

from scapy.all import Raw, IP, sr1, send, UDP

import sys

SERVER_IP = "cs177.seclab.cs.ucsb.edu"

def send_mode6(request_type: int, port: int):
    payload = bytes([
        0x16,
        0x00,
        0x03,
        request_type,
        0x00, 0x00, 0x00, 0x00
    ]) + 40 * b"\x00" 
    
    packet = IP(dst=SERVER_IP) / UDP(dport=port) / Raw(load=payload)

    print(f"\n[+] Sending Mode 6 request type {request_type}")
    response = sr1(packet, timeout=3, verbose=0)

    if response and Raw in response:
        data = bytes(response[Raw])

        print(f"Received {len(data)} bytes")
        print(data)

        amp = len(data) / len(payload)
        print(f"Amplification: {amp:.2f}")

    else:
        print("No response")

def main():
    if len(sys.argv) != 2:
        print("Usage: python dns_amplify.py <port>")
        return 1 

    port = int(sys.argv[1])
    
    for request_type in range(5):
        send_mode6(request_type, port)
    
if __name__ == "__main__":
    main()
