import ResponseEnvelop_pb2
import random
from Util import NetUtil
from Requests import CatchPokemonRequest_pb2
from Responses import CatchPokemonResponse_pb2

class CatchPokemon(object):
	POKEBALLS = {
		'Normal': 1,
		'Great': 2,
		'Ultra': 3,
		'Master': 4,
	}

	
	def __init__(self, raw_request, url, logger=None):
		self.request = raw_request
		self.url = url
		self.logger = logger
	

	def _handle_response(self, response):
		response_envelop = ResponseEnvelop_pb2.ResponseEnvelop()
		response_envelop.ParseFromString(response.content)
		catch_pokemon_response = CatchPokemonResponse_pb2.CatchPokemonResponse()
		catch_pokemon_response.ParseFromString(response_envelop.responses[0])
		assert catch_pokemon_response

		if self.logger:
			self.logger.info("Received CATCH_POKEMON response:\r\n")
			self.logger.debug("%s" % catch_pokemon_response)
		return catch_pokemon_response

	
	def get(self, encounter_id, spawn_point_id, pokeball_type):
		catch_pokemon_request = CatchPokemonRequest_pb2.CatchPokemonRequest()
		catch_pokemon_request.encounter_id = encounter_id
		catch_pokemon_request.spawn_point_guid = spawn_point_id

		catch_pokemon_request.pokeball = self.POKEBALLS[pokeball_type]
		catch_pokemon_request.hit_pokemon = True # Obviously
		catch_pokemon_request.normalized_reticle_size = 1.7 + random.random() / 4 # Anything between 1.7 to 1.95 is great.
		catch_pokemon_request.spin_modifier = 0.75 + random.random() / 4 # Anything between 0.75 to 1
		catch_pokemon_request.normalized_hit_position = 1.0
		self.request.requests[0].message = catch_pokemon_request.SerializeToString()
		data = self.request.SerializeToString()

		if self.logger:
			self.logger.info("Sending CATCH_POKEMON request:\r\n")
			self.logger.debug("%s" % catch_pokemon_request)
		return self._handle_response(NetUtil.request("POST", self.url, data))