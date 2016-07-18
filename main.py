from PokemonGoClient import *
import time, pprint


def parse_map_objects_response(data):
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

			if len(map_cell.one_step_pokemon) > 0:
				for pokemon in map_cell.one_step_pokemon:
					found_pokemon[pokemon.encounter_id]["latitude"] = pokemon.latitude
					found_pokemon[pokemon.encounter_id]["longitude"] = pokemon.longitude
					if pokemon.expiration_timestamp_ms != -1:
						found_pokemon[pokemon.encounter_id]["disappear"] = time.ctime(pokemon.expiration_timestamp_ms / 1000.)

			if len(map_cell.two_steps_pokemon) > 0:
				for pokemon in map_cell.two_steps_pokemon:
					found_pokemon[pokemon.encounter_id]["latitude"] = pokemon.latitude
					found_pokemon[pokemon.encounter_id]["longitude"] = pokemon.longitude
					found_pokemon[pokemon.encounter_id]["time_till_hidden"] = pokemon.time_till_hidden_ms / 1000.
		
		return found_pokemon


if __name__ == '__main__':
	client = PokemonGoClient((32.0918229,34.7743952, 37.5), log=True)
	client.login("tal.skverer@gmail.com", "oauth2rt_1/#")
	#response = client.get_map_objects(32.0918229,34.7743952, 37.5)
	#print client.get_player()
	#pprint.pprint(parse_map_objects_response(response))
	#print client.get_inventory()

	#print "[I] There is a %s just %s meters away" % (Constants.POKEDEX[str(pokemon.pokemon_id)], pokemon.distance_in_meters)
	#print "[!] There is a %s in these co-ords: %s, %s!" % (pokemon_name, pokemon.latitude, pokemon.longitude)
	#print "[!] There is a %s in these co-ords: %s, %s! Disappears in: %s" % (pokemon_name, pokemon.latitude, pokemon.longitude, disappear_time)