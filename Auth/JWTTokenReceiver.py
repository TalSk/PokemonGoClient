import requests
import urllib
import re
from Util import NetUtil, Constants, Config


class JWTTokenReceiver(object):	

	def __init__(self, email, oauth_token, logger=None):
		self.token = oauth_token
		self.email = email
		self.logger = logger
		self.request = self._prepare_request()

	def _prepare_request(self):
		data = {
			"androidId": Constants.ANDROID_ID,
			"lang": Constants.LANG,
			"google_play_services_version": Constants.GOOGLE_PLAY_SERVICES_VERSION,
			"sdk_version": Constants.SDK_VERSION,
			"device_country": Constants.DEVICE_COUNTRY,
			"client_sig": Constants.CLIENT_SIG,
			"callerSig": Constants.CALLER_SIG,
			"Email": self.email,
			"service": Constants.SERVICE,
			"app": Constants.APP,
			"check_email": Constants.CHECK_EMAIL,
			"token_request_options": Constants.TOKEN_REQUEST_OPTIONS,
			"callerPkg": Constants.CALLER_PKG,
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
		request = requests.Request('POST', Constants.ANDROID_AUTH_ENDPOINT, data=prepared_data, headers=headers)
		return request.prepare()


	def _extract_token(self, data):
		matches = re.match("Auth=(.*)", data)
		return matches.group(1)


	def get_token(self):
		proxies = {}
		if Config.USE_PROXY:
			proxies = Constants.FIDDLER_PROXY
		response = NetUtil.request_with_prepared(self.request)
		token = self._extract_token(response.content)
		if self.logger:
			self.logger.debug("Received JWT token successfully:\r\n%s" % token)
		return token