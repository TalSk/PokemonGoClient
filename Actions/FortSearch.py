import ResponseEnvelop_pb2
from Util import NetUtil
from Requests import FortSearchRequest_pb2
from Responses import FortSearchResponse_pb2

class FortSearch(object):
	
	def __init__(self, raw_request, url, logger=None):
		self.request = raw_request
		self.url = url
		self.logger = logger
	

	def _handle_response(self, response):
		response_envelop = ResponseEnvelop_pb2.ResponseEnvelop()
		response_envelop.ParseFromString(response.content)
		fort_search_response = FortSearchResponse_pb2.FortSearchResponse()
		fort_search_response.ParseFromString(response_envelop.responses[0])
		assert fort_search_response

		if self.logger:
			self.logger.info("Received FORT_SEARCH response:\r\n")
			self.logger.debug("%s" % fort_search_response)
		return fort_search_response

	
	def get(self, details, latitude, longitude):
		fort_search_request = FortSearchRequest_pb2.FortSearchRequest()
		fort_search_request.fort_id = details["id"]
		fort_search_request.player_latitude= latitude
		fort_search_request.player_longitude = longitude
		fort_search_request.fort_latitude = details["latitude"]
		fort_search_request.fort_longitude = details["longitude"]
		self.request.requests[0].message = fort_search_request.SerializeToString()
		data = self.request.SerializeToString()

		if self.logger:
			self.logger.info("Sending FORT_SEARCH request:\r\n")
			self.logger.debug("%s" % fort_search_request)
		return self._handle_response(NetUtil.request("POST", self.url, data))