import time
import RequestEnvelop_pb2, ResponseEnvelop_pb2, EnvelopData_pb2
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
			auth_ticket = EnvelopData_pb2.AuthTicket()
			token = f.readline()[:-2]
			auth_ticket.token = token
			timestamp = f.readline()[:-2]
			auth_ticket.expire_timestamp_ms = long(timestamp)
			sig = f.readline()[:-2]
			auth_ticket.sig = sig
			return url, auth_ticket


	def _cache_login(self):
		with open(self.CACHE_FILE, "wb") as f:
			f.write(str(time.time()) + "\r\n")
			f.write(self.url + "\r\n")
			f.write(self.auth_ticket.token + "\r\n")
			f.write(str(self.auth_ticket.expire_timestamp_ms) + "\r\n")
			f.write(self.auth_ticket.sig + "\r\n")


	def _get_auth_ticket(self, jwt_token):
		# Creating a raw request
		req_env = RequestEnvelop_pb2.RequestEnvelop()
		req_env.status_code = 2
		req_env.rpc_id = Utils.randomize_rpc_id()
		# It doesn't matter what kind of response you request here, you won't get any response. You must send at least one, though.
		request = req_env.requests.add()
		request.request_type = Constants.GET_MAP_OBJECTS_REQUEST
		# Adding the authentication details
		req_env.auth_info.provider = "google"
		req_env.auth_info.token.contents = jwt_token
		req_env.unknown12 = 1036

		raw_data = req_env.SerializeToString()
		if self.logger:
			self.logger.debug("Sending session token request:\r\n%s" % req_env)
		return NetUtil.request("POST", Constants.BASE_NIANTIC_URL, raw_data)


	def _handle_response(self, response):
		res_pb = ResponseEnvelop_pb2.ResponseEnvelop()
		res_pb.ParseFromString(response.content)
		assert res_pb.api_url
		assert res_pb.auth_ticket
		# The url we recieve doesn't have a scheme prefix, or the rpc suffix.
		return "https://" + res_pb.api_url + "/rpc", res_pb.auth_ticket


	def _authenticate(self, jwt_token):
		response = self._get_auth_ticket(jwt_token)
		return self._handle_response(response)


	def login(self):
		if self._has_cache_login():
			try:
				self.url, self.auth_ticket = self._get_cache_login()
			except Exception:
				self.logger.warning("Unable to get cached login, logging normally...")
				jwt_token = JWTTokenReceiver(self.email, self.oauth_token, self.logger).get_token()
				self.url, self.auth_ticket = self._authenticate(jwt_token)
				self._cache_login()
		else:
			jwt_token = JWTTokenReceiver(self.email, self.oauth_token, self.logger).get_token()
			self.url, self.auth_ticket = self._authenticate(jwt_token)
			self._cache_login()

		assert self.url
		assert self.auth_ticket
		if self.logger:
			self.logger.debug("Received endpoint url and token:\r\n%s\r\n%s" % (self.url, self.auth_ticket))
		
		return self.url, self.auth_ticket