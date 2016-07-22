from PokemonGoClient import *
from Enums import FortEnums_pb2
import time, pprint
import Util

def parse_pokemon_map_objects_response(data):
	# TODO: Calculate distance to walk to exact locations
	found_pokemon = {}
	for map_cell in data.map_tiles:
		# Order matters. We 'prefer' specific message since it has way more details.
		if len(map_cell.three_steps_pokemon) > 0:
			for pokemon in map_cell.three_steps_pokemon:
				found_pokemon[pokemon.encounter_id] = {
					"id" : pokemon.pokemon_id,
					"name" : Constants.POKEDEX[str(pokemon.pokemon_id)],
					"distance" : pokemon.distance_in_meters
				}
				found_pokemon[pokemon.encounter_id]["catchable"] = False

		if len(map_cell.one_step_pokemon) > 0:
			for pokemon in map_cell.one_step_pokemon:
				found_pokemon[pokemon.encounter_id]["latitude"] = pokemon.latitude
				found_pokemon[pokemon.encounter_id]["longitude"] = pokemon.longitude
				found_pokemon[pokemon.encounter_id]["spawnpoint_id"] = pokemon.spawnpoint_id
				if pokemon.expiration_timestamp_ms != -1:
					found_pokemon[pokemon.encounter_id]["disappear"] = time.ctime(pokemon.expiration_timestamp_ms / 1000.)
				found_pokemon[pokemon.encounter_id]["catchable"] = True

		if len(map_cell.two_steps_pokemon) > 0:
			for pokemon in map_cell.two_steps_pokemon:
				found_pokemon[pokemon.encounter_id]["latitude"] = pokemon.latitude
				found_pokemon[pokemon.encounter_id]["longitude"] = pokemon.longitude
				found_pokemon[pokemon.encounter_id]["time_till_hidden"] = pokemon.time_till_hidden_ms / 1000.
				found_pokemon[pokemon.encounter_id]["spawnpoint_id"] = pokemon.spawn_point_id
				
	return found_pokemon

def parse_pokestops_map_objects_response(data):
	found_pokestops = []
	for map_cell in data.map_tiles:
		for fort in map_cell.forts:
			if fort.fort_type == FortEnums_pb2.CHECKPOINT and fort.enabled:
				# It's a pokestop
				found_pokestops.append({
					"id" : fort.id,
					"latitude" : fort.latitude,
					"longitude" : fort.longitude
					})
	return found_pokestops


def search_pokestops(pokestops):
	for pokestop in pokestops:
		print client.fort_search(pokestop, pokestop["latitude"], pokestop["longitude"], 37.5)
		time.sleep(10)


def pokestops_bot(pokestops):
	# pokestops =  [{'id': u'9feec60670b74df9871391b4b9e3ca24.16',
	# 			   'latitude': 31.810439,
	# 			   'longitude': 34.784115},
	# 			  {'id': u'deb98d507a2c4665ad038851e93f033c.16',
	# 			   'latitude': 31.810791,
	# 			   'longitude': 34.784167}]

  	while 1:
  		success = False
  		while not success:
  			try:
  				get_map_objects_response = client.get_map_objects(31.810666, 34.784146, 37.5)
  				search_pokestops(pokestops)
 				success = True
			except Util.NetUtil.ServerDownException, Util.NetUtil.BadStatusException:
		 		time.sleep(20)
		 		continue
		current = time.time()
		while time.time() - current < 60. * 5:
			get_map_objects_response = client.get_map_objects(31.810666, 34.784146, 37.5)
		 	time.sleep(20)


def test_functionality():
	print client.download_settings()
	print client.get_player()
	print client.get_inventory()
	get_map_objects_response = client.get_map_objects(start_location)
	pprint.pprint(parse_pokemon_map_objects_response(get_map_objects_response))
	pprint.pprint(parse_pokestops_map_objects_response(get_map_objects_response))

		

if __name__ == '__main__':
	start_location = Util.Utils.Location(31.804589561409422, 34.783529859201494, 37.5)
	client = PokemonGoClient(start_location, log=True)
	client.login("tal.skverer@gmail.com", "oauth2rt_1/#", "Google")
	

	#get_map_objects_response = client.get_map_objects(start_location)
	#pprint.pprint(parse_pokemon_map_objects_response(get_map_objects_response))
	#print client.catch_pokemon(12827716286160938365L, u'1502b95b6b3', start_location)	
