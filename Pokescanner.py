import Utils
import request_pb2
import response_pb2
import time
from Constants import *
from JWTReceiver import *

class Pokescanner(object):
	CACHE_FILE = "login.cache"
	
	def __init__(self):
		self.logger = Utils.initialize_logger()


	def _has_cache_login(self):
		try:
			with open(self.CACHE_FILE, "rb") as f:
				timestamp = f.readline()
				if not timestamp:
					return False
				if time.time() > float(timestamp) + HOUR:
					return False
				return True
		except Exception:
			return False


	def _get_cache_login(self):
		with open(self.CACHE_FILE, "rb") as f:
			f.readline()
			url = f.readline()[:-2] # To remove \r\n
			token_data = response_pb2.ResponseEnvelop.TokenData()
			token = f.readline()[:-2]
			token_data.token = token
			timestamp = f.readline()[:-2]
			token_data.timestamp = long(timestamp)
			sig = f.readline()[:-2]
			token_data.sig = sig
			return url, token_data


	def _cache_login(self):
		with open(self.CACHE_FILE, "wb") as f:
			f.write(str(time.time()) + "\r\n")
			f.write(self.url + "\r\n")
			f.write(self.session_token.token + "\r\n")
			f.write(str(self.session_token.timestamp) + "\r\n")
			f.write(self.session_token.sig + "\r\n")


	def _parse_response(self, response_content):
		response_envelop = response_pb2.ResponseEnvelop()
		response_envelop.ParseFromString(response_content)
		return response_envelop


	def _session_token_request(self, jwt_token):
		# Creating a raw request
		req_env = request_pb2.RequestEnvelop()
		req_env.unknown1 = 2
		req_env.rpc_id = Utils.randomize_rpc_id()
		# It doesn't matter what kind of response you request here, you won't get any response. You must send at least one, though.
		session_token_request = req_env.requests.add()
		session_token_request.type = GET_MAP_OBJECTS_REQUEST
		# Adding the authentication details
		req_env.auth.provider = "google"
		req_env.auth.token.contents = jwt_token
		req_env.time_delta = 1036 # TODO

		raw_data = req_env.SerializeToString()
		self.logger.debug("Sending session token request:\r\n%s" % req_env)
		return Utils.request("POST", BASE_NIANTIC_URL, raw_data).content


	def _handle_session_token_response(self, response):
		res_pb = self._parse_response(response)
		assert res_pb.endpoint
		assert res_pb.token
		# The endpoint we recieve doesn't have a scheme prefix, or the rpc suffix.
		return "https://" + res_pb.endpoint + "/rpc", res_pb.token


	def _create_session(self, jwt_token):
		response = self._session_token_request(jwt_token)
		return self._handle_session_token_response(response)


	def google_login(self, user_email, user_oauth_token):
		if self._has_cache_login():
			self.url, self.session_token = self._get_cache_login()
		else:
			jwt_receiver = JWTReceiver(user_email, user_oauth_token)
			self.url, self.session_token = self._create_session(jwt_receiver.get_token())
			self._cache_login()
		self.logger.debug("Received endpoint url: %s" % self.url)
		self.logger.debug("Received session token:\r\n%s" % self.session_token)
		self.logger.info("Logged in successfully!")


	def _get_map_objects_request(self, latitude, longitude, cell_ids):
		# Creating a raw request
		req_env = request_pb2.RequestEnvelop()
		req_env.unknown1 = 2
		req_env.rpc_id = Utils.randomize_rpc_id()


		# Requesting a GET_MAP_OBJECTS response
		get_map_objects_request = req_env.requests.add()
		get_map_objects_request.type = GET_MAP_OBJECTS_REQUEST

		# Adding information about wanted response - requested cell ids
		get_map_objects_proto = request_pb2.RequestEnvelop.GetMapObjectsRequest()
		for cell_id in cell_ids:
		 	get_map_objects_proto.cell_id.append(cell_id.id())
		 	get_map_objects_proto.since_time_ms.append(0)
		get_map_objects_proto.player_lat = latitude
		get_map_objects_proto.player_lng = longitude

		get_map_objects_request.message = get_map_objects_proto.SerializeToString()
		# Adding other request details, including session token
		req_env.gps_x = latitude
		req_env.gps_y = longitude
		req_env.gps_z = GPS_Z_CONSTANT
		req_env.token.token = self.session_token.token
		req_env.token.timestamp = self.session_token.timestamp
		req_env.token.sig = self.session_token.sig
		req_env.time_delta = 3122 # TODO



		data = req_env.SerializeToString()
		self.logger.debug("Sending get map objects request:\r\n%s" % req_env)

		return Utils.request("POST", self.url, data).content


	def _handle_get_map_objects_response(self, response):
		res_pb = self._parse_response(response)
		get_map_objects_response = response_pb2.PossibleResponse1()
		get_map_objects_response.ParseFromString(res_pb.responses[0])
		assert get_map_objects_response
		self.logger.debug("Parsing get map objects response:\r\n%s" % get_map_objects_response)

		# TODO: Make pokemon found a set
		# TODO: Calculate distance to walk to wild and catchable pokemon.
		# TODO: Put nearby pokemon in a differnet area
		for map_tile in get_map_objects_response.map_tiles:
			if len(map_tile.nearby_pokemon) > 0:
				for nearby_pokemon in map_tile.nearby_pokemon:
					print "[I] There is a %s just %s meters away" % (POKEDEX[str(nearby_pokemon.pokedex_number)], Utils.hex_to_float(nearby_pokemon.distance_meters))
			if len(map_tile.wild_pokemon) > 0:
				for wild_pokemon in map_tile.wild_pokemon:
					print "[!] There is a %s in these co-ords: %s, %s!" % (POKEDEX[str(wild_pokemon.info.number)], Utils.hex_to_double(wild_pokemon.lat), Utils.hex_to_double(wild_pokemon.lng))
			if len(map_tile.catchable_pokemon) > 0:
				for catchable_pokemon in map_tile.catchable_pokemon:
					print "[!] There is a %s in these co-ords: %s, %s!" % (POKEDEX[str(catchable_pokemon.pkmn_no)], Utils.hex_to_double(catchable_pokemon.lat), Utils.hex_to_double(catchable_pokemon.lng))


	def scan(self, latitude, longitude):
		neighboring_cell_ids = Utils.get_neighbors(latitude, longitude)
		self.logger.debug("Received the following neighboring cell ids:\r\n%s" % neighboring_cell_ids)
		latitude = Utils.double_to_hex(latitude)
		longitude = Utils.double_to_hex(longitude)

		response =	self._get_map_objects_request(latitude, longitude, neighboring_cell_ids)
		return self._handle_get_map_objects_response(response)


if __name__ == '__main__':
	a = Pokescanner()
	a.google_login("taltaltal1994@gmail.com", "#")
	a.scan(31.809736251831055, 34.7845344543457)

