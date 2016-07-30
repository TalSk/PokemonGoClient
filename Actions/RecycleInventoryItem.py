import ResponseEnvelop_pb2
import random
from Util import NetUtil
from Requests import RecycleInventoryItemRequest_pb2
from Responses import RecycleInventoryItemResponse_pb2

class RecycleInventoryItem(object):
	
	def __init__(self, raw_request, url, logger=None):
		self.request = raw_request
		self.url = url
		self.logger = logger


	def _handle_response(self, response):
		response_envelop = ResponseEnvelop_pb2.ResponseEnvelop()
		response_envelop.ParseFromString(response.content)
		recycle_inventory_item_response = RecycleInventoryItemResponse_pb2.RecycleInventoryItemResponse()
		recycle_inventory_item_response.ParseFromString(response_envelop.responses[0])
		assert recycle_inventory_item_response

		if self.logger:
			self.logger.info("Received RECYCLE_INVENTORY_ITEM response:\r\n")
			self.logger.debug("%s" % recycle_inventory_item_response)
		return recycle_inventory_item_response

	
	def get(self, item_id, count):
		recycle_inventory_item_request = RecycleInventoryItemRequest_pb2.RecycleInventoryItemRequest()
		recycle_inventory_item_request.item_id = item_id
		recycle_inventory_item_request.count = count

		self.request.requests[0].message = recycle_inventory_item_request.SerializeToString()
		data = self.request.SerializeToString()

		if self.logger:
			self.logger.info("Sending RECYCLE_INVENTORY_ITEM request:\r\n")
			self.logger.debug("%s" % recycle_inventory_item_request)
		return self._handle_response(NetUtil.request("POST", self.url, data))