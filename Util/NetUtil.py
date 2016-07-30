import collections
import requests
import Config
import Constants


DEFAULT_HEADERS = collections.OrderedDict({
		"Connection": "Keep-Alive",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": Config.USER_AGENT,
		"Accept-Encoding": "gzip"
	})

def request(method, url, data=None, headers=None):
	if headers == None:
		headers = DEFAULT_HEADERS
	headers["Content-Length"] = len(data)

	req = requests.Request(method, url, data=data, headers=headers)
	prepped = req.prepare()
	return request_with_prepared(prepped)


def request_with_prepared(prepared_request):
	proxies = {}
	if Config.USE_PROXY:
		proxies = Constants.FIDDLER_PROXY
	try:
		s = requests.Session()
		response = s.send(prepared_request, verify=False, proxies=proxies)
		if response.status_code != 200:
			raise BadStatusException("Received bad status code from server: %s" % response.status_code)
		if len(response.content) == 2:
			raise AuthExpiredException("Auth token expired")
		return response
	except requests.exceptions.ConnectionError:
		raise ServerDownException("Could not connect to Pokemon Go servers")

class ServerDownException(Exception):
	pass

class AuthExpiredException(Exception):
	pass

class BadStatusException(Exception):
	pass