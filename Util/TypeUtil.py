import struct


def double_to_hex(number):
    return struct.unpack('<Q', struct.pack('<d', number))[0]

def hex_to_double(number):
	return struct.unpack('>d', hex(number)[2:-1].decode("hex"))[0]

def hex_to_float(number):
	return struct.unpack('>f', hex(number)[2:].decode("hex"))[0]