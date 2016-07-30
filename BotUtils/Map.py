from Util import Utils, Constants
from Enums import FortEnums_pb2
import time

class Map(object):

	def __init__(self, client):
		self.client = client
		self.update()


	def update(self):
		"""
			Updates map object, effectively sending a GET_MAP_OBJECTS request.
		"""
		self.gmo = self.client.get_map_objects(self.client.location)


	def walk_until_near(self, destination, min_near_distance):
		"""
			"Walks" to a target destination location until close enough.


			destination: A Location class of the target location.
			min_near_distance: The minimum distance required to arrive from destination.
		"""
		while self.client.location.distance(destination) > min_near_distance:
			diff_lat = self.client.location.latitude - destination.latitude
			diff_lon = self.client.location.longitude - destination.longitude
			new_location = Utils.Location(self.client.location.latitude - diff_lat, self.client.location.longitude - diff_lon)
			while self.client.location.distance(new_location) > 20:
				diff_lat /= 2
				diff_lon /= 2
				new_location = Utils.Location(self.client.location.latitude - diff_lat, self.client.location.longitude - diff_lon)
			print "[I] Moved from %s, %s to %s, %s" % (self.client.location.latitude, self.client.location.longitude, new_location.latitude, new_location.longitude)
			self.client.location = new_location
			self.update()
			time.sleep(9)


	def get_nearby_pokestops(self):
		"""
			Parses latest GET_MAP_OBJECTS resposne to receive every detail about nearby pokestops.
		"""
		self.update()
		found_pokestops = []
		for map_cell in self.gmo.map_cells:
			for fort in map_cell.forts:
				if fort.fort_type == FortEnums_pb2.CHECKPOINT and fort.enabled:
					# It's a pokestop
					found_pokestops.append({
						"id" : fort.id,
						"latitude" : fort.latitude,
						"longitude" : fort.longitude,
						"cooldown_left" : fort.cooldown_complete_timestamp_ms
						})
		return found_pokestops


	def get_nearby_pokemon(self):
		"""
			Parses latest GET_MAP_OBJECTS response to receive every detail about nearby pokemon.
		"""
		self.update()
		found_pokemon = {}
		for map_cell in self.gmo.map_cells:
			if len(map_cell.three_steps_pokemon) > 0:
				for pokemon in map_cell.three_steps_pokemon:
					found_pokemon[pokemon.encounter_id] = {
						"encounter_id": pokemon.encounter_id,
						"id" : pokemon.pokemon_id,
						"name" : Constants.POKEDEX[str(pokemon.pokemon_id)],
						"distance" : pokemon.distance_in_meters
					}
					found_pokemon[pokemon.encounter_id]["catchable"] = False

			if len(map_cell.one_step_pokemon) > 0:
				for pokemon in map_cell.one_step_pokemon:
					found_pokemon[pokemon.encounter_id]["encounter_id"] = pokemon.encounter_id
					found_pokemon[pokemon.encounter_id]["latitude"] = pokemon.latitude
					found_pokemon[pokemon.encounter_id]["longitude"] = pokemon.longitude
					found_pokemon[pokemon.encounter_id]["spawnpoint_id"] = pokemon.spawnpoint_id
					if pokemon.expiration_timestamp_ms != -1:
						found_pokemon[pokemon.encounter_id]["disappear"] = time.ctime(pokemon.expiration_timestamp_ms / 1000.)
					found_pokemon[pokemon.encounter_id]["catchable"] = True

			if len(map_cell.two_steps_pokemon) > 0:
				for pokemon in map_cell.two_steps_pokemon:
					found_pokemon[pokemon.encounter_id]["encounter_id"] = pokemon.encounter_id
					found_pokemon[pokemon.encounter_id]["latitude"] = pokemon.latitude
					found_pokemon[pokemon.encounter_id]["longitude"] = pokemon.longitude
					found_pokemon[pokemon.encounter_id]["time_till_hidden"] = pokemon.time_till_hidden_ms / 1000.
					found_pokemon[pokemon.encounter_id]["spawnpoint_id"] = pokemon.spawn_point_id	
					found_pokemon[pokemon.encounter_id]["catchable"] = True	
		return found_pokemon