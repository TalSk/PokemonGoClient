import time
import request_pb2, response_pb2
from Util import NetUtil, Constants, Utils
from JWTTokenReceiver import JWTTokenReceiver


class GoogleLogin(object):
	CACHE_FILE = "googlelogin.cache"
	
	def __init__(self, email, oauth_token, logger=None):
		self.email = email
		self.oauth_token = oauth_token
		self.logger = logger


	def _has_cache_login(self):
		try:
			with open(self.CACHE_FILE, "rb") as f:
				timestamp = f.readline()
				if not timestamp:
					return False
				if time.time() > float(timestamp) + Constants.HALF_AN_HOUR:
					return False
				return True
		except Exception:
			return False


	def _get_cache_login(self):
		with open(self.CACHE_FILE, "rb") as f:
			f.readline()
			url = f.readline()[:-2] # To remove \r\n
			token_data = response_pb2.ResponseEnvelop.TokenData()
			token = f.readline()[:-2]
			token_data.token = token
			timestamp = f.readline()[:-2]
			token_data.timestamp = long(timestamp)
			sig = f.readline()[:-2]
			token_data.sig = sig
			return url, token_data


	def _cache_login(self):
		with open(self.CACHE_FILE, "wb") as f:
			f.write(str(time.time()) + "\r\n")
			f.write(self.url + "\r\n")
			f.write(self.session_token.token + "\r\n")
			f.write(str(self.session_token.timestamp) + "\r\n")
			f.write(self.session_token.sig + "\r\n")


	def _get_session_token(self, jwt_token):
		# Creating a raw request
		req_env = request_pb2.RequestEnvelop()
		req_env.unknown1 = 2
		req_env.rpc_id = Utils.randomize_rpc_id()
		# It doesn't matter what kind of response you request here, you won't get any response. You must send at least one, though.
		request = req_env.requests.add()
		request.type = Constants.GET_MAP_OBJECTS_REQUEST
		# Adding the authentication details
		req_env.auth.provider = "google"
		req_env.auth.token.contents = jwt_token
		req_env.time_delta = 1036 # TODO

		raw_data = req_env.SerializeToString()
		if self.logger:
			self.logger.debug("Sending session token request:\r\n%s" % req_env)
		return NetUtil.request("POST", Constants.BASE_NIANTIC_URL, raw_data)


	def _handle_response(self, response):
		res_pb = response_pb2.ResponseEnvelop()
		res_pb.ParseFromString(response.content)
		assert res_pb.endpoint
		assert res_pb.token
		# The endpoint we recieve doesn't have a scheme prefix, or the rpc suffix.
		return "https://" + res_pb.endpoint + "/rpc", res_pb.token


	def _authenticate(self, jwt_token):
		response = self._get_session_token(jwt_token)
		return self._handle_response(response)


	def login(self):
		if self._has_cache_login():
			self.url, self.session_token = self._get_cache_login()
		else:
			jwt_token = JWTTokenReceiver(self.email, self.oauth_token, self.logger).get_token()
			self.url, self.session_token = self._authenticate(jwt_token)
			self._cache_login()

		assert self.url
		assert self.session_token
		if self.logger:
			self.logger.debug("Received endpoint url and token:\r\n%s\r\n%s" % (self.url, self.session_token))
		
		return self.url, self.session_token