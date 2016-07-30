import ResponseEnvelop_pb2
from Util import NetUtil
from Requests import ReleasePokemonRequest_pb2
from Responses import ReleasePokemonResponse_pb2

class ReleasePokemon(object):
	
	def __init__(self, raw_request, url, logger=None):
		self.request = raw_request
		self.url = url
		self.logger = logger
	

	def _handle_response(self, response):
		response_envelop = ResponseEnvelop_pb2.ResponseEnvelop()
		response_envelop.ParseFromString(response.content)
		release_pokemon_response = ReleasePokemonResponse_pb2.ReleasePokemonResponse()
		release_pokemon_response.ParseFromString(response_envelop.responses[0])
		assert release_pokemon_response

		if self.logger:
			self.logger.info("Received RELEASE_POKEMON response:\r\n")
			self.logger.debug("%s" % release_pokemon_response)
		return release_pokemon_response

	
	def get(self, pokemon_id):
		release_pokemon_request = ReleasePokemonRequest_pb2.ReleasePokemonRequest()
		release_pokemon_request.pokemon_id = pokemon_id
		self.request.requests[0].message = release_pokemon_request.SerializeToString()
		data = self.request.SerializeToString()

		if self.logger:
			self.logger.info("Sending RELEASE_POKEMON request:\r\n")
			self.logger.debug("%s" % self.request)
		return self._handle_response(NetUtil.request("POST", self.url, data))