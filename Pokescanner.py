from random import randint
from JWTReceiver import *
import Utils
import request_pb2
import response_pb2
from Constants import *

class UnexpectedError(BaseException):
	pass

class Pokescanner(object):
	

	def __init__(self, user_email, user_token):
		jwt_receiver = JWTReceiver(user_email, user_token)
		self.url, self.session_token = self._init_session(jwt_receiver.get_token())


	def _make_init_request(self, jwt_token):
		init_request = request_pb2.RequestEnvelop()
		init_request.unknown1 = 2
		init_request.rpc_id = randint(1000000000000000000, 9000000000000000000)
		request = init_request.requests.add()
		request.type = GET_MAP_OBJECTS_REQUEST # It doesn't matter what response you request here, as you won't get a response.
		init_request.auth.provider = "google"
		init_request.auth.token.contents = jwt_token
		init_request.time_delta = 1036
		data = init_request.SerializeToString()

		return Utils.make_request("POST", BASE_NIANTIC_URL, data).content

	def _generate_response(self, response_content):
		response_envelop = response_pb2.ResponseEnvelop()
		response_envelop.ParseFromString(response_content)
		return response_envelop

	def _init_session(self, jwt_token):
		response = self._make_init_request(jwt_token)
		res_pb = self._generate_response(response)
		assert res_pb.endpoint
		assert res_pb.token
		# The endpoint we recieve doesn't have a scheme prefix, or the rpc suffix.
		return "https://" + res_pb.endpoint + "/rpc", res_pb.token

	def _parse_scan_response(self, response):
		res_pb = self._generate_response(response)
		get_map_objects_response = response_pb2.PossibleResponse1()
		get_map_objects_response.ParseFromString(res_pb.responses[0])

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
		#print get_map_objects_response

	def scan(self, latitude, longitude):
		latitude = Utils.double_to_hex(latitude)
		longitude = Utils.double_to_hex(longitude)

		get_map_request = request_pb2.RequestEnvelop()
		get_map_request.unknown1 = 2
		get_map_request.rpc_id = randint(1000000000000000000, 9000000000000000000)
		request = get_map_request.requests.add()
		request.type = GET_MAP_OBJECTS_REQUEST
		get_map_objects = request_pb2.RequestEnvelop.GetMapObjectsRequest()
		get_map_objects.cell_id = CELL_ID_CONSTANT
		get_map_objects.player_lat = latitude
		get_map_objects.player_lng = longitude
		request.message = get_map_objects.SerializeToString()
		get_map_request.gps_x = latitude
		get_map_request.gps_y = longitude
		get_map_request.gps_z = GPS_Z_CONSTANT
		get_map_request.token.token = self.session_token.token
		get_map_request.token.timestamp = self.session_token.timestamp
		get_map_request.token.sig = self.session_token.sig
		get_map_request.time_delta = 151
		data = get_map_request.SerializeToString()

		return self._parse_scan_response(Utils.make_request("POST", self.url, data).content)


if __name__ == '__main__':
	a = Pokescanner("taltaltal1994@gmail.com", "#")
	a.scan(31.8070215,34.7796028)

