import ResponseEnvelop_pb2
from Util import NetUtil
from Requests import EncounterRequest_pb2
from Responses import EncounterResponse_pb2

class Encounter(object):
	
	def __init__(self, raw_request, url, logger=None):
		self.request = raw_request
		self.url = url
		self.logger = logger
	

	def _handle_response(self, response):
		response_envelop = ResponseEnvelop_pb2.ResponseEnvelop()
		response_envelop.ParseFromString(response.content)
		encounter_response = EncounterResponse_pb2.EncounterResponse()
		encounter_response.ParseFromString(response_envelop.responses[0])
		assert encounter_response

		if self.logger:
			self.logger.info("Received ENCOUNTER response:\r\n")
			self.logger.debug("%s" % encounter_response)
		return encounter_response

	
	def get(self, encounter_id, spawn_point_id, latitude, longitude):
		encounter_request = EncounterRequest_pb2.EncounterRequest()
		encounter_request.encounter_id = encounter_id
		encounter_request.spawn_point_id = spawn_point_id
		encounter_request.latitude = latitude
		encounter_request.longitude = longitude
		self.request.requests[0].message = encounter_request.SerializeToString()
		data = self.request.SerializeToString()

		if self.logger:
			self.logger.info("Sending ENCOUNTER request:\r\n")
			self.logger.debug("%s" % encounter_request)
		return self._handle_response(NetUtil.request("POST", self.url, data))