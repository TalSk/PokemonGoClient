import ResponseEnvelop_pb2
from Util import NetUtil
from Requests import FortDetailsRequest_pb2
from Responses import FortDetailsResponse_pb2

class FortDetails(object):
	
	def __init__(self, raw_request, url, logger=None):
		self.request = raw_request
		self.url = url
		self.logger = logger
	

	def _handle_response(self, response):
		response_envelop = ResponseEnvelop_pb2.ResponseEnvelop()
		response_envelop.ParseFromString(response.content)
		fort_details_response = FortDetailsResponse_pb2.FortDetailsResponse()
		fort_details_response.ParseFromString(response_envelop.responses[0])
		assert fort_details_response

		if self.logger:
			self.logger.debug("Received FORT_DETAILS response:\r\n%s" % fort_details_response)
		return fort_details_response

	
	def get(self, details):
		fort_details_request = FortDetailsRequest_pb2.FortDetailsRequest()
		fort_details_request.fort_id = details["id"]
		fort_details_request.latitude = details["latitude"]
		fort_details_request.longitude = details["longitude"]
		self.request.requests[0].message = fort_details_request.SerializeToString()
		data = self.request.SerializeToString()

		if self.logger:
			self.logger.debug("Sending FORT_DETAILS request:\r\n%s" % fort_details_request)
		return self._handle_response(NetUtil.request("POST", self.url, data))