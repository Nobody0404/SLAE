#!/usr/bin/env python
# Title: Convert Integer (Port) to network order
#        and convert IP to hex presentation.
# Date: 2015-01-06
# Author: Dennis 'dhn' Herrmann
# Website: https://zer0-day.pw
# Github: https://github.com/dhn/SLAE/
# SLAE-721

# This piece  of code help to convert an integer to
# the network byte order  and convert IP address to
# the  hexadecimal presentation. This is  necessary
# for the PORT/IP variable in the shell_reverse_tcp
# file. If you want to change it.

import sys
import socket

def convert_port(port):
    if port <= 65535:
        network_order = socket.htons(port)
        network_hex = hex(network_order)
        return network_order, network_hex
    else:
        print("[!] port range is over 65535")
        sys.exit(1)

def convert_ip_addr(ip_addr):
    ip_addr_hex = ""
    for byte in ip_addr:
        ip_addr_hex += str(hex(int(byte)))[2:]

    return "0x" + ip_addr_hex

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: %s ip-address number" % __file__)
    else:
        port = int(sys.argv[2])
        ip_addr = str(sys.argv[1])
        network, inhex = convert_port(port)
        ip_addr_hex = convert_ip_addr(ip_addr.split('.'))
        print("port in dec: %s" % port)
        print("port in hex: %s" % inhex)
        print("IP address: %s" % ip_addr)
        print("IP address in hex: %s" % ip_addr_hex)