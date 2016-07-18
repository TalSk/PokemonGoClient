import ResponseEnvelop_pb2
from Util import NetUtil
from Responses import GetPlayerResponse_pb2

class GetPlayer(object):
	
	def __init__(self, raw_request, url, logger=None):
		self.request = raw_request
		self.url = url
		self.logger = logger
	

	def _handle_response(self, response):
		response_envelop = ResponseEnvelop_pb2.ResponseEnvelop()
		response_envelop.ParseFromString(response.content)
		get_player_response = GetPlayerResponse_pb2.GetPlayerResponse()
		get_player_response.ParseFromString(response_envelop.responses[0])
		assert get_player_response

		if self.logger:
			self.logger.debug("Received GET_PLAYER response:\r\n%s" % get_player_response)
		return get_player_response

	
	def get(self):
		data = self.request.SerializeToString()

		if self.logger:
			self.logger.debug("Sending GET_PLAYER request:\r\n%s" % self.request)
		return self._handle_response(NetUtil.request("POST", self.url, data))