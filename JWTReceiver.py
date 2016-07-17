import requests
import urllib
import re
import Utils
from Constants import *


class JWTReceiver(object):
	"""
		Contstants for use in request
	"""
	# TODO: Transfer to Constants.py
	

	def __init__(self, user_email, user_token):
		self.token = user_token
		self.email = user_email
		self.request = self._prepare_request()

	def _prepare_request(self):
		data = {
			"androidId": ANDROID_ID,
			"lang": LANG,
			"google_play_services_version": GOOGLE_PLAY_SERVICES_VERSION,
			"sdk_version": SDK_VERSION,
			"device_country": DEVICE_COUNTRY,
			"client_sig": CLIENT_SIG,
			"callerSig": CALLER_SIG,
			"Email": self.email,
			"service": SERVICE,
			"app": APP,
			"check_email": CHECK_EMAIL,
			"token_request_options": TOKEN_REQUEST_OPTIONS,
			"callerPkg": CALLER_PKG,
			"Token": self.token
		}
		prepared_data = urllib.urlencode(data)
		headers = {
			"device": "3e93a95e2fd2b281",
			"app": "com.nianticlabs.pokemongo",
			"Accept-Encoding": "gzip",
			"User-Agent": "GoogleAuth/1.4 (A0001 MHC19Q); gzip",
			"content-length": len(prepared_data),
			"content-type": "application/x-www-form-urlencoded",
			"Connection": "Keep-Alive"
		}
		request = requests.Request('POST', ANDROID_AUTH_ENDPOINT, data=prepared_data, headers = headers)
		return request.prepare()

	def _extract_token(self, data):
		matches = re.match("Auth=(.*)", data)
		return matches.group(1)

	def get_token(self):
		proxies = {}
		if USE_PROXY:
			proxies = FIDDLER_PROXY
		s = requests.Session()
		try:
			response = s.send(self.request, verify=False, proxies=proxies)
		except requests.exceptions.ConnectionError:
			raise Utils.ServerDownException("Could not connect to Google auth server")
		return self._extract_token(response.content)