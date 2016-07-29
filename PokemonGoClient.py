import time
import RequestEnvelop_pb2
from Enums import RequestEnums_pb2
from Util import Constants, Logger, NetUtil, TypeUtil, Utils
from Auth import GoogleLogin
from Actions import GetMapObjects, GetPlayer, GetInventory, DownloadSettings, FortSearch, Encounter, CatchPokemon, FortDetails, ReleasePokemon


class PokemonGoClient(object):
	"""
		An all-purpose client for Pokemon Go server interaction.
	"""
	def __init__(self, location, log=False):
		"""
			Initializes class.


			location: A Location instance describing the user current position.
			log: Whether to log every request.
		"""
		self.location = location
		self.logger=None
		if log:
			self.logger = Logger.initialize_logger()


	def _create_raw_request(self):
		"""
			Creates a raw request to the server, wrapping the actual message.
			Also, makes sure user is currently authenticated.

			Returns the raw request protocol buffer object.
		"""

		# At first, if we authenticated longer than 30 minutes ago, it's time to re-login.
		if time.time() - self.last_authenticated > Constants.HALF_AN_HOUR:
			self.url, self.session_token = self.login(self.email, self.oauth_token, self.login_type, False)

		request_envelop = RequestEnvelop_pb2.RequestEnvelop()
		request_envelop.status_code = 2
		request_envelop.rpc_id = Utils.randomize_rpc_id()

		request_envelop.latitude = self.location.latitude
		request_envelop.longitude = self.location.longitude
		request_envelop.altitude = self.location.altitude # TODO: Check if neccessary

		request_envelop.auth_ticket.token = self.session_token.token
		request_envelop.auth_ticket.expire_timestamp_ms = self.session_token.expire_timestamp_ms
		request_envelop.auth_ticket.sig = self.session_token.sig
		request_envelop.unknown12 = 3122

		return request_envelop


	def change_location(self, location):
		"""
			Changes current client location


			location: A Location instance describing the new position
		"""
		self.location = location


	def login(self, email, oauth_token, login_type="Google", use_cache=True):
		"""
			Receives a session token and an endpoint url from the server,
			in effect, logging in the user.


			email: User email address
			oauth_token: User's google oauth2 token
			login_type: Indicating the type of the login, either `Google` or `PTC`
			use_cache: Whether to use saved login information

			Returns None.
		"""
		self.login_type = login_type
		self.email = email
		self.oauth_token = oauth_token
		if self.login_type == "Google":
			google_login = GoogleLogin.GoogleLogin(self.email, self.oauth_token, self.logger)
			self.url, self.session_token = google_login.login(use_cache)
		elif self.login_type == "PTC":
			raise Exception("PTC Login not implemented yet.")
		else:
			raise Exception("Error")
		self.last_authenticated = time.time()
		if self.logger:
			self.logger.info("Logged in successfully as %s!" % email)


	def get_map_objects(self, location):
		"""
			Gets map objects of a given location's nearby S3 cells.


			location: A Location instance describing the current search center location

			Returns a parsed server response.
		"""
		neighboring_cell_ids = Utils.get_neighbors(location.latitude, location.longitude)
		self.logger.debug("Received the following neighboring cell ids:\r\n%s" % neighboring_cell_ids)

		raw_request = self._create_raw_request()
		new_request = raw_request.requests.add()
		new_request.request_type = RequestEnums_pb2.GET_MAP_OBJECTS

		gmo = GetMapObjects.GetMapObjects(raw_request, self.url, self.logger)
		return gmo.get(location.latitude, location.longitude, neighboring_cell_ids)


	def get_player(self):
		"""
			Gets logged in player's information

			Returns a parsed server response.
		"""
		raw_request = self._create_raw_request()
		new_request = raw_request.requests.add()
		new_request.request_type = RequestEnums_pb2.GET_PLAYER

		return GetPlayer.GetPlayer(raw_request, self.url, self.logger).get()


	def get_inventory(self):
		"""
			Gets logged in player's inventory

			Returns a parsed server response.
		"""
		raw_request = self._create_raw_request()
		new_request = raw_request.requests.add()
		new_request.request_type = RequestEnums_pb2.GET_INVENTORY

		return GetInventory.GetInventory(raw_request, self.url, self.logger).get()


	def download_settings(self):
		"""
			Downloads logged in player's settings.

			Returns a parsed server response.
		"""
		raw_request = self._create_raw_request()
		new_request = raw_request.requests.add()
		new_request.request_type = RequestEnums_pb2.DOWNLOAD_SETTINGS

		return DownloadSettings.DownloadSettings(raw_request, self.url, self.logger).get()


	def fort_details(self, pokestop_details):
		"""
			Gets a Pokestop's details.


			pokestop_details: A dictionary containing three keys:
						  id -> Pokestop's id
						  latitude -> Pokestop's latitude
						  longitude -> Pokestop's longitude

			Returns a parsed server response.
		"""
		raw_request = self._create_raw_request()
		new_request = raw_request.requests.add()
		new_request.request_type = RequestEnums_pb2.FORT_DETAILS

		return FortDetails.FortDetails(raw_request, self.url, self.logger).get(pokestop_details)

	
	def fort_search(self, pokestop_details):
		"""
			Searches a Pokestop.


			pokestop_details: A dictionary containing three keys:
						  id -> Pokestop's id
						  latitude -> Pokestop's latitude
						  longitude -> Pokestop's longitude

			Returns a parsed server response.
		"""
		raw_request = self._create_raw_request()
		new_request = raw_request.requests.add()
		new_request.request_type = RequestEnums_pb2.FORT_SEARCH

		fs = FortSearch.FortSearch(raw_request, self.url, self.logger)
		return fs.get(pokestop_details, self.location.latitude, self.location.longitude)


	def encounter(self, encounter_id, spawn_point_id, location):
		"""
			Encounters a Pokemon.


			encounter_id: Pokemon encounter id
			spawn_point_id: Pokemon spawn point id
			location: A Location instance describing player current location

			Returns a parsed server response.
		"""
		raw_request = self._create_raw_request()
		new_request = raw_request.requests.add()
		new_request.request_type = RequestEnums_pb2.ENCOUNTER

		enc = Encounter.Encounter(raw_request, self.url, self.logger)
		return enc.get(encounter_id, spawn_point_id, location.latitude, location.longitude)


	def catch_pokemon(self, encounter_id, spawn_point_id, pokeball_type='Normal'):
		"""
			Catches a Pokemon.


			encounter_id: Pokemon encounter id
			spawn_point_id: Pokemon spawn point id

			Returns a parsed server response.
		"""
		raw_request = self._create_raw_request()
		new_request = raw_request.requests.add()
		new_request.request_type = RequestEnums_pb2.CATCH_POKEMON

		cp = CatchPokemon.CatchPokemon(raw_request, self.url, self.logger)
		return cp.get(encounter_id, spawn_point_id, pokeball_type)


	def release_pokemon(self, pokemon_id):
		"""
			Releases a Pokemon.


			pokemon_id: Pokemon id

			Returns a parsed server response.
		"""
		raw_request = self._create_raw_request()
		new_request = raw_request.requests.add()
		new_request.request_type = RequestEnums_pb2.RELEASE_POKEMON

		return ReleasePokemon.ReleasePokemon(raw_request, self.url, self.logger).get(pokemon_id)