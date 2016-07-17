import request_pb2, response_pb2
from Util import Utils, NetUtil, Constants
		

class GetMapObjectsRequest(object):
	
	def __init__(self, raw_request, url, logger=None):
		self.request = raw_request
		self.url = url
		self.logger = logger
		

	def _handle_response(self, response):
		response_envelop = response_pb2.ResponseEnvelop()
		response_envelop.ParseFromString(response.content)
		get_map_objects_response = response_pb2.PossibleResponse1()
		get_map_objects_response.ParseFromString(response_envelop.responses[0])
		assert get_map_objects_response

		if self.logger:
			self.logger.debug("Received GET_MAP_OBJECTS response:\r\n%s" % get_map_objects_response)
		return get_map_objects_response


	def get(self, latitude, longitude, cell_ids):
		get_map_objects_request = request_pb2.RequestEnvelop.GetMapObjectsRequest()
		for cell_id in cell_ids:
		 	get_map_objects_request.cell_id.append(cell_id.id())
		 	get_map_objects_request.since_time_ms.append(0)
		get_map_objects_request.player_lat = latitude
		get_map_objects_request.player_lng = longitude

		self.request.requests[0].message = get_map_objects_request.SerializeToString()
		data = self.request.SerializeToString()

		if self.logger:
			self.logger.debug("Sending GET_MAP_OBJECTS request:\r\n%s" % get_map_objects_request)
		return self._handle_response(NetUtil.request("POST", self.url, data))

		