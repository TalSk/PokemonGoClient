import time
from Constants import *
from Config import *

def initialize_logger(log_level="i"):
	if DEBUG:
		return Logger("d")
	return Logger(log_level)


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

