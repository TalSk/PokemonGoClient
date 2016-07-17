import time
import RequestEnvelop_pb2
from Enums import RequestEnums_pb2
from Util import Constants, Logger, NetUtil, TypeUtil, Utils
from Auth import GoogleLogin
from Actions import GetMapObjects


class PokeonGoClient(object):
	
	def __init__(self, log=False):
		self.logger=None
		if log:
			self.logger = Logger.initialize_logger()


	def _create_raw_request(self):
		request_envelop = RequestEnvelop_pb2.RequestEnvelop()
		request_envelop.status_code = 2
		request_envelop.rpc_id = Utils.randomize_rpc_id()

		request_envelop.auth_ticket.token = self.session_token.token
		request_envelop.auth_ticket.expire_timestamp_ms = self.session_token.expire_timestamp_ms
		request_envelop.auth_ticket.sig = self.session_token.sig
		request_envelop.unknown12 = 3122 # TODO

		return request_envelop


	def login(self, email, oauth_token):
		google_login = GoogleLogin.GoogleLogin(email, oauth_token, self.logger)
		self.url, self.session_token = google_login.login()
		if self.logger:
			self.logger.info("Logged in successfully as %s!" % email)


	def _parse_map_objects_response(self, data):
		# TODO: Make pokemon found a set
		# TODO: Calculate distance to walk to wild and catchable pokemon.
		# TODO: Put nearby pokemon in a differnet area
		for map_cell in data.map_tiles:
			if len(map_cell.three_steps_pokemon) > 0:
				for pokemon in map_cell.three_steps_pokemon:
					print "[I] There is a %s just %s meters away" % (Constants.POKEDEX[str(pokemon.pokemon_id)], pokemon.distance_in_meters)
			if len(map_cell.two_steps_pokemon) > 0:
				for pokemon in map_cell.two_steps_pokemon:
					pokemon_name = Constants.POKEDEX[str(pokemon.pokemon_details.pokemon_id)]
					print "[!] There is a %s in these co-ords: %s, %s!" % (pokemon_name, pokemon.latitude, pokemon.longitude)
			if len(map_cell.one_step_pokemon) > 0:
				for pokemon in map_cell.one_step_pokemon:
					pokemon_name = Constants.POKEDEX[str(pokemon.pokemon_id)]
					disappear_time = "Unknown time"
					if pokemon.expiration_timestamp_ms != -1:
						disappear_time = time.ctime(pokemon.expiration_timestamp_ms / 1000.)
					print "[!] There is a %s in these co-ords: %s, %s! Disappears in: %s" % (pokemon_name, pokemon.latitude, pokemon.longitude, disappear_time)


	def get_map_objects(self, latitude, longitude, altitude):
		neighboring_cell_ids = Utils.get_neighbors(latitude, longitude)
		self.logger.debug("Received the following neighboring cell ids:\r\n%s" % neighboring_cell_ids)
		latitude = TypeUtil.double_to_hex(latitude)
		longitude = TypeUtil.double_to_hex(longitude)

		raw_request = self._create_raw_request()
		get_map_objects_request = raw_request.requests.add()
		get_map_objects_request.request_type = RequestEnums_pb2.GET_MAP_OBJECTS
		raw_request.latitude = latitude
		raw_request.longitude = longitude
		raw_request.altitude = altitude # TODO

		map_objects_response = GetMapObjects.GetMapObjects(raw_request, self.url, self.logger).get(latitude, longitude, neighboring_cell_ids)
		return self._parse_map_objects_response(map_objects_response)


	def get_player(self):
		# TODO
		pass

if __name__ == '__main__':
	a = PokeonGoClient(log=True)
	a.login("taltaltal1994@gmail.com", "oauth2rt_1/#")
	a.get_map_objects(31.804105, 34.784143, 0x4042c00000000000)
	#a.get_map_objects(31.809826, 34.784631)

