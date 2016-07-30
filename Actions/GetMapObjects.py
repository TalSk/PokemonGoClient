import ResponseEnvelop_pb2
from Util import Utils, NetUtil, Constants
from Requests import GetMapObjectsRequest_pb2
from Responses import GetMapObjectsResponse_pb2


class GetMapObjects(object):
	
	def __init__(self, raw_request, url, logger=None):
		self.request = raw_request
		self.url = url
		self.logger = logger
		

	def _handle_response(self, response):
		response_envelop = ResponseEnvelop_pb2.ResponseEnvelop()
		response_envelop.ParseFromString(response.content)
		get_map_objects_response = GetMapObjectsResponse_pb2.GetMapObjectsResponse()
		get_map_objects_response.ParseFromString(response_envelop.responses[0])
		assert get_map_objects_response

		if self.logger:
			self.logger.info("Received GET_MAP_OBJECTS response:\r\n%s" % get_map_objects_response)
		return get_map_objects_response


	def get(self, latitude, longitude, cell_ids):
		get_map_objects_request = GetMapObjectsRequest_pb2.GetMapObjectsRequest()
		for cell_id in cell_ids:
		 	get_map_objects_request.cell_id.append(cell_id.id())
		 	get_map_objects_request.since_time_ms.append(0)
		get_map_objects_request.latitude = latitude
		get_map_objects_request.longitude = longitude

		self.request.requests[0].message = get_map_objects_request.SerializeToString()
		data = self.request.SerializeToString()

		if self.logger:
			self.logger.info("Sending GET_MAP_OBJECTS request:\r\n%s" % get_map_objects_request)
		return self._handle_response(NetUtil.request("POST", self.url, data))

		