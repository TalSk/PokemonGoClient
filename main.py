from PokemonGoClient import *
from Enums import FortEnums_pb2
import time, pprint
import Util
import Bot


def test_functionality():
	print client.download_settings()
	print client.get_player()
	print client.get_inventory()
	get_map_objects_response = client.get_map_objects(start_location)
	pprint.pprint(parse_pokemon_map_objects_response(get_map_objects_response))
	pprint.pprint(parse_pokestops_map_objects_response(get_map_objects_response))

		

if __name__ == '__main__':
	start_location = Util.Utils.Location(31.815228, 34.773972, 37.5)
	client = PokemonGoClient(start_location, log=True)
	client.login("tal.skverer@gmail.com", "oauth2rt_1/#", "Google")
	
	b = Bot.Bot(client)
	try:
		b.start()
	finally:
		b.stop()


# TODO:
#		Hatch eggs
# 		Look for TODOs in code
#		Document everything
# 		Document in README
#		PTR Login
#		Google login with password