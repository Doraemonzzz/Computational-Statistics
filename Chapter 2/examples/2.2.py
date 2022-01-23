# https://stackoverflow.com/questions/16444726/binary-representation-of-float-in-python-bits-not-hex

import struct

def binary(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!d', num))

print(binary(1.0))

