import Utils
import request_pb2
import response_pb2
from Constants import *
from JWTReceiver import *

class Pokescanner(object):
	
	def __init__(self):
		self.logger = Utils.initialize_logger()


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
		jwt_receiver = JWTReceiver(user_email, user_oauth_token)
		self.url, self.session_token = self._create_session(jwt_receiver.get_token())
		self.logger.debug("Received endpoint url: %s" % self.url)
		self.logger.debug("Received session token:\r\n%s" % self.session_token)


	def _get_map_objects_request(self, longitude, latitude, cell_ids):
		# Creating a raw request
		req_env = request_pb2.RequestEnvelop()
		req_env.unknown1 = 2
		req_env.rpc_id = Utils.randomize_rpc_id()

		# Requesting a GET_MAP_OBJECTS response
		get_map_objects_request = req_env.requests.add()
		get_map_objects_request.type = GET_MAP_OBJECTS_REQUEST

		# Adding information about wanted response - requested cell ids
		get_map_objects_proto = request_pb2.RequestEnvelop.GetMapObjectsRequest()
		#for cell_id in cell_ids:
		#	get_map_objects_proto.cell_id.append(cell_id.id())
		get_map_objects_proto.cell_id.append(1513976118942629888)
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
		req_env.time_delta = 151 # TODO

		data = req_env.SerializeToString()

		return Utils.request("POST", self.url, data).content


	def _handle_get_map_objects_response(self, response):
		res_pb = self._parse_response(response)
		get_map_objects_response = response_pb2.PossibleResponse1()
		get_map_objects_response.ParseFromString(res_pb.responses[0])
		assert get_map_objects_response

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
		latitude = Utils.double_to_hex(latitude)
		longitude = Utils.double_to_hex(longitude)

		response =	self._get_map_objects_request(latitude, longitude, neighboring_cell_ids)
		return self._handle_get_map_objects_response(response)


if __name__ == '__main__':
	a = Pokescanner()
	a.google_login("taltaltal1994@gmail.com", "#")
	a.scan(31.8070215,34.7796028)

