import request_pb2, response_pb2
import time
from Requests.GetMapObjectsRequest import *
from Util import Constants, Logger, NetUtil, TypeUtil, Utils
from Auth import GoogleLogin


class PokeonGoClient(object):
	
	def __init__(self, log=False):
		self.logger=None
		if log:
			self.logger = Logger.initialize_logger()


	def _create_raw_request(self):
		request_envelop = request_pb2.RequestEnvelop()
		request_envelop.unknown1 = 2
		request_envelop.rpc_id = Utils.randomize_rpc_id()

		request_envelop.token.token = self.session_token.token
		request_envelop.token.timestamp = self.session_token.timestamp
		request_envelop.token.sig = self.session_token.sig
		request_envelop.time_delta = 3122 # TODO

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
		for map_tile in data.map_tiles:
			if len(map_tile.nearby_pokemon) > 0:
				for nearby_pokemon in map_tile.nearby_pokemon:
					print "[I] There is a %s just %s meters away" % (Constants.POKEDEX[str(nearby_pokemon.pokedex_number)], TypeUtil.hex_to_float(nearby_pokemon.distance_meters))
			if len(map_tile.wild_pokemon) > 0:
				for wild_pokemon in map_tile.wild_pokemon:
					pokemon_name = Constants.POKEDEX[str(wild_pokemon.info.number)]
					pokemon_lat = TypeUtil.hex_to_double(wild_pokemon.lat)
					pokemon_lng = TypeUtil.hex_to_double(wild_pokemon.lng)
					disappear_time = time.ctime(time.time() + wild_pokemon.time_till_hidden)
					print "[!] There is a %s in these co-ords: %s, %s! Disappears in: %s" % (pokemon_name, pokemon_lat, pokemon_lng, disappear_time)
			if len(map_tile.catchable_pokemon) > 0:
				for catchable_pokemon in map_tile.catchable_pokemon:
					pokemon_name = Constants.POKEDEX[str(catchable_pokemon.pkmn_no)]
					pokemon_lat = TypeUtil.hex_to_double(catchable_pokemon.lat)
					pokemon_lng = TypeUtil.hex_to_double(catchable_pokemon.lng)
					print "[!] There is a %s in these co-ords: %s, %s!" % (pokemon_name, pokemon_lat, pokemon_lng)


	def get_map_objects(self, latitude, longitude, z_index):
		neighboring_cell_ids = Utils.get_neighbors(latitude, longitude)
		self.logger.debug("Received the following neighboring cell ids:\r\n%s" % neighboring_cell_ids)
		latitude = TypeUtil.double_to_hex(latitude)
		longitude = TypeUtil.double_to_hex(longitude)

		raw_request = self._create_raw_request()
		get_map_objects_request = raw_request.requests.add()
		get_map_objects_request.type = Constants.GET_MAP_OBJECTS_REQUEST
		raw_request.gps_x = latitude
		raw_request.gps_y = longitude
		raw_request.gps_z = z_index # TODO

		map_objects_response = GetMapObjectsRequest(raw_request, self.url, self.logger).get(latitude, longitude, neighboring_cell_ids)
		return self._parse_map_objects_response(map_objects_response)


	def get_player(self):
		# TODO
		pass

if __name__ == '__main__':
	a = PokeonGoClient(log=True)
	a.login("taltaltal1994@gmail.com", "oauth2rt_1/51760r0ineUINW0sUDr75RAPFq7pUuXoDb0RZzKgHT8")
	a.get_map_objects(31.804105, 34.784143, 0x4042c00000000000)
	#a.get_map_objects(31.809826, 34.784631)

