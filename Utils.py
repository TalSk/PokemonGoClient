import requests
import urllib
import struct
from collections import OrderedDict
from Constants import *


def make_request(method, url, data=None):
	headers = OrderedDict({
		"Connection": "Keep-Alive",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": USER_AGENT,
		"Accept-Encoding": "gzip",
		"Content-Length": len(data)
	})

	proxies = {}
	if USE_PROXY:
		proxies = FIDDLER_PROXY

	req = requests.Request(method, url, data=data, headers=headers)		
	s = requests.Session()
	prepped = s.prepare_request(req)
	return s.send(prepped, verify=False, proxies=proxies)


def double_to_hex(number):
    return struct.unpack('<Q', struct.pack('<d', number))[0]

def hex_to_double(number):
	return struct.unpack('>d', hex(number)[2:-1].decode("hex"))[0]

def hex_to_float(number):
	return struct.unpack('>f', hex(number)[2:].decode("hex"))[0]