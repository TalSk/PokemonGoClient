import time
import RequestEnvelop_pb2
from Enums import RequestEnums_pb2
from Util import Constants, Logger, NetUtil, TypeUtil, Utils
from Auth import GoogleLogin
from Actions import GetMapObjects, GetPlayer, GetInventory, DownloadSettings


class PokemonGoClient(object):
	
	def __init__(self, location, log=False):
		self.location = location
		self.logger=None
		if log:
			self.logger = Logger.initialize_logger()


	def _create_raw_request(self):
		request_envelop = RequestEnvelop_pb2.RequestEnvelop()
		request_envelop.status_code = 2
		request_envelop.rpc_id = Utils.randomize_rpc_id()

		request_envelop.latitude = self.location[0]
		request_envelop.longitude = self.location[1]
		request_envelop.altitude = self.location[2] # TODO

		request_envelop.auth_ticket.token = self.session_token.token
		request_envelop.auth_ticket.expire_timestamp_ms = self.session_token.expire_timestamp_ms
		request_envelop.auth_ticket.sig = self.session_token.sig
		request_envelop.unknown12 = 3122 # TODO

		return request_envelop


	def change_location(self, location):
		self.location = location


	def login(self, email, oauth_token):
		google_login = GoogleLogin.GoogleLogin(email, oauth_token, self.logger)
		self.url, self.session_token = google_login.login()
		if self.logger:
			self.logger.info("Logged in successfully as %s!" % email)


	def get_map_objects(self, latitude, longitude, altitude):
		neighboring_cell_ids = Utils.get_neighbors(latitude, longitude)
		self.logger.debug("Received the following neighboring cell ids:\r\n%s" % neighboring_cell_ids)

		raw_request = self._create_raw_request()
		new_request = raw_request.requests.add()
		new_request.request_type = RequestEnums_pb2.GET_MAP_OBJECTS

		raw_request.latitude = latitude
		raw_request.longitude = longitude
		raw_request.altitude = altitude # TODO

		return GetMapObjects.GetMapObjects(raw_request, self.url, self.logger).get(latitude, longitude, neighboring_cell_ids)


	def get_player(self):
		raw_request = self._create_raw_request()
		new_request = raw_request.requests.add()
		new_request.request_type = RequestEnums_pb2.GET_PLAYER

		return GetPlayer.GetPlayer(raw_request, self.url, self.logger).get()


	def get_inventory(self):
		raw_request = self._create_raw_request()
		new_request = raw_request.requests.add()
		new_request.request_type = RequestEnums_pb2.GET_INVENTORY

		return GetInventory.GetInventory(raw_request, self.url, self.logger).get()


	def download_settings(self):
		raw_request = self._create_raw_request()
		new_request = raw_request.requests.add()
		new_request.request_type = RequestEnums_pb2.DOWNLOAD_SETTINGS

		return DownloadSettings.DownloadSettings(raw_request, self.url, self.logger).get()

	

