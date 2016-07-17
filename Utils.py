import requests
import urllib
import struct
import s2sphere
import time
from random import randint
from collections import OrderedDict
from Constants import *


def get_neighbors(latitude, longitude):
	r = s2sphere.RegionCoverer()
	r.max_level = 15
	r.min_level = 15
	p1 = s2sphere.LatLng.from_degrees(latitude - 0.005, longitude - 0.005)
	p2 = s2sphere.LatLng.from_degrees(latitude + 0.005, longitude + 0.005)
	return r.get_covering(s2sphere.LatLngRect.from_point_pair(p1, p2))

def request(method, url, data=None):
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
	try:
		return s.send(prepped, verify=False, proxies=proxies)
	except requests.exceptions.ConnectionError:
		raise ServerDownException("Could not connect to Pokemon Go servers")

def randomize_rpc_id():
	return randint(1000000000000000000, 9000000000000000000)

def double_to_hex(number):
    return struct.unpack('<Q', struct.pack('<d', number))[0]

def hex_to_double(number):
	return struct.unpack('>d', hex(number)[2:-1].decode("hex"))[0]

def hex_to_float(number):
	return struct.unpack('>f', hex(number)[2:].decode("hex"))[0]

def initialize_logger(log_level="i"):
	if DEBUG:
		return Logger("d")
	return Logger(log_level)


class ServerDownException(Exception):
	pass


class Logger(object):
	LOG_LEVELS = {
		"i" : 0,
		"w" : 1,
		"d" : 2
	}
	DEBUG = 2
	WARNING = 1
	INFO = 0

	def __init__(self, log_level):
		self.log_level = self.LOG_LEVELS[log_level]
		self.file = open(DEFAULT_LOG_PATH, "a")
		
	def _write(self, prefix, string):
		self.file.write(BOUNDARY)
		self.file.write(prefix + time.ctime(time.time()) + "--" + string + "\r\n")
		self.file.write(BOUNDARY)

	def debug(self, string):
		if self.log_level >= self.DEBUG:
			prefix = "--(D)-- "
			self._write(prefix, string)

	def warning(self, string):
		if self.log_level >= self.WARNING:
			prefix = "--(W)-- "
			self._write(prefix, string)

	def info(self, string):
		if self.log_level >= self.INFO:
			prefix = "--(I)-- "
			self._write(prefix, string)

	def error(self, string):
		prefix = "!!(E)!! "
		self._write(prefix, string)

