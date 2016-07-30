import ResponseEnvelop_pb2
from Util import NetUtil
from Requests import DownloadSettingsRequest_pb2
from Responses import DownloadSettingsResponse_pb2

class DownloadSettings(object):
	
	def __init__(self, raw_request, url, logger=None):
		self.request = raw_request
		self.url = url
		self.logger = logger
	

	def _handle_response(self, response):
		response_envelop = ResponseEnvelop_pb2.ResponseEnvelop()
		response_envelop.ParseFromString(response.content)
		download_settings_response = DownloadSettingsResponse_pb2.DownloadSettingsResponse()
		download_settings_response.ParseFromString(response_envelop.responses[0])
		assert download_settings_response

		if self.logger:
			self.logger.info("Received DOWNLOAD_SETTINGS response:\r\n")
			self.logger.debug("%s" % download_settings_response)
		return download_settings_response

	
	def get(self):
		data = self.request.SerializeToString()

		if self.logger:
			self.logger.info("Sending DOWNLOAD_SETTINGS request:\r\n")
			self.logger.debug("%s" % self.request)
		return self._handle_response(NetUtil.request("POST", self.url, data))