import threading
import random
import time
from Util import Utils, Constants, NetUtil
from geopy.distance import vincenty
from Enums import FortEnums_pb2, PlayerEnums_pb2

class Bot(object):
	STOP_EVENT = threading.Event()
	MIN_CP = 300

	def __init__(self, client):
		self.client = client
		self.player = self.client.get_player()
		self.altitude = 37
		self.heartbeat_thread = threading.Thread(target=self._heartbeat)
		self.heartbeat_thread.start()


	def _get_pokeballs_count(self):
		pokeballs = 0
		great_pokeballs = 0
		ultra_pokeballs = 0
		master_pokeballs = 0
		for item in self.inventory.inventory_delta.inventory_items:
			if item.inventory_item_data.item:
				if item.inventory_item_data.item.item == PlayerEnums_pb2.ITEM_POKE_BALL:
					if item.inventory_item_data.item.count:
						pokeballs = item.inventory_item_data.item.count
				elif item.inventory_item_data.item.item == PlayerEnums_pb2.ITEM_GREAT_BALL:
					if item.inventory_item_data.item.count:
						great_pokeballs = item.inventory_item_data.item.count
				elif item.inventory_item_data.item.item == PlayerEnums_pb2.ITEM_ULTRA_BALL:
					if item.inventory_item_data.item.count:
						ultra_pokeballs = item.inventory_item_data.item.count
				elif item.inventory_item_data.item.item == PlayerEnums_pb2.ITEM_MASTER_BALL:
					if item.inventory_item_data.item.count:
						master_pokeballs = item.inventory_item_data.item.count
		return {
			'Normal': pokeballs,
			'Great': great_pokeballs,
			'Ultra': ultra_pokeballs,
			'Master': master_pokeballs
		}



	def _count_items(self):
		self.inventory = self.client.get_inventory()
		count = 0
		for item in self.inventory.inventory_delta.inventory_items:
			if item.inventory_item_data.item:
				if item.inventory_item_data.item.count:
					count += item.inventory_item_data.item.count
		return count


	def _heartbeat(self):
		"""
			Sends a heartbeat to the server; effectively sending a get map objects request
		"""
		while 1:
			if self.STOP_EVENT.isSet():
				return
			self.altitude += random.random() - random.random()
			self.client.location.change_altitude(self.altitude)
			try:
				self.gmo_latest = self.client.get_map_objects(self.client.location)
				print "[I] Sent heartbeat"
			except NetUtil.ServerDownException:
				print "[I] Server exception in heartbeat"
				pass
			except Exception:
				print "[I] General exception in heartbeat"
				pass
			time.sleep(10)


	def stop(self):
		self.STOP_EVENT.set()


	def _catch_nearby_pokemon(self):
		pokemons = self._parse_pokemon(self.gmo_latest)
		for encounter_id in pokemons:
			pokemon = pokemons[encounter_id]
			if pokemon["catchable"]:
				pokeball_type = self._choose_pokeball()
				if pokeball_type:
					pokemon_location = Utils.Location(pokemon["latitude"], pokemon["longitude"])
					print "[I] Moving to a %s from %s, %s to %s, %s" % (pokemon["name"], self.client.location.latitude, self.client.location.longitude, pokemon["latitude"], pokemon["longitude"])
					self._walk_to_until_near(pokemon_location, Constants.ENCOUNTER_RANGE_METERS - (random.random() * 5))
					print "[I] Close enough. Trying to catch pokemon"
					self.has_moved = True
					fight_over = False
					while fight_over == False:
						pokeball_type = self._choose_pokeball()
						if pokeball_type == None:
							print "[I] No Pokeballs left."
							return
						enc_res = self.client.encounter(pokemon["encounter_id"], pokemon["spawnpoint_id"], pokemon_location)
						time.sleep(2 + random.random() * 5) # Gotta wait between encounter and throwing the ball.
						cp_res = self.client.catch_pokemon(pokemon["encounter_id"], pokemon["spawnpoint_id"], pokeball_type)
						if cp_res.status == 1: # Success
							print "[I] Caught a %s, with %s CP." % (pokemon["name"], enc_res.pokemon.pokemon.cp)
							self._maybe_release_pokemon(pokemon["name"], enc_res.pokemon.pokemon.cp, cp_res.captured_pokemon_id)						
							fight_over = True
						elif cp_res.status == 2: # Escape
							print "[I] %s escaped from Pokeball. Trying again" % pokemon["name"]
						elif cp_res.status == 3: # Flee
							print "[I] %s fled :(" % pokemon["name"]
							fight_over = True
					time.sleep(5)
				else:
					print "[I] No Pokeballs left."
					return


	def _maybe_release_pokemon(self, name, pokemon_cp, pokemon_id):
		if self.MIN_CP > pokemon_cp:
			self.client.release_pokemon(pokemon_id)
			print "[I] Released caught %s. (%s CP)." % (name, pokemon_cp)


	def _choose_pokeball(self):
		self.inventory = self.client.get_inventory()
		self.pokeballs = self._get_pokeballs_count()
		if self.pokeballs['Normal']:
			return 'Normal'
		if self.pokeballs['Great']:
			return 'Great'
		if self.pokeballs['Ultra']:
			return 'Ultra'
		return None


	def _spin_closest_pokestop(self):
		pokestops = self._parse_pokestops(self.gmo_latest)
		pokestop = self._pick_closest_pokestop(pokestops)
		if pokestop:
			pokestop_location = Utils.Location(pokestop["latitude"], pokestop["longitude"])
			print "[I] Moving to a pokestop from %s, %s to %s, %s" % (self.client.location.latitude, self.client.location.longitude, pokestop["latitude"], pokestop["longitude"])
			self._walk_to_until_near(pokestop_location, Constants.INTERACTION_RANGE_METERS - (random.random() * 5))
			print "[I] Moved close enough, spinning..."
			self.has_moved = True
			self.client.fort_details(pokestop)
			time.sleep(2 + random.random() * 2) # Gotta wait.
			self.client.fort_search(pokestop)
			print "[I] Span a Pokestop at %s, %s" % (pokestop["latitude"], pokestop["longitude"])


	def start(self):
		try:
			while 1:
				try:
					self.has_moved = False
					self.gmo_latest = self.client.get_map_objects(self.client.location)
					self._catch_nearby_pokemon()
					items_count = self._count_items()
					if items_count < 350:
						self.gmo_latest = self.client.get_map_objects(self.client.location)
						self._spin_closest_pokestop()
					if self.has_moved == False:
						print "[I] Could not catch any pokemon or spin any pokestop, quitting..."
						return

					"[I] Done a round, sleeping..."
				except NetUtil.ServerDownException:
					print "[I] Servers are down, retrying..."
					pass
				except Exception:
					print "[I] General exception, retrying..."
					pass
				time.sleep(10)

		finally:
			self.stop()


	def _walk_to_until_near(self, destination, near_distance):
		while self.client.location.distance(destination) > near_distance:
			diff_lat = self.client.location.latitude - destination.latitude
			diff_lon = self.client.location.longitude - destination.longitude
			new_location = Utils.Location(self.client.location.latitude - diff_lat, self.client.location.longitude - diff_lon)
			while self.client.location.distance(new_location) > 20:
				diff_lat /= 2
				diff_lon /= 2
				new_location = Utils.Location(self.client.location.latitude - diff_lat, self.client.location.longitude - diff_lon)
			print "[I] Moved from %s, %s to %s, %s" % (self.client.location.latitude, self.client.location.longitude, new_location.latitude, new_location.longitude)
			self.client.location = new_location
			time.sleep(9)


	def _pick_closest_pokestop(self, pokestop_list):
		spinnable_pokestops = []
		for pokestop in pokestop_list:
			if pokestop["cooldown_left"] == 0:
				spinnable_pokestops.append(pokestop)
		if spinnable_pokestops:
			closest_pokestop = spinnable_pokestops[0]
			for pokestop in spinnable_pokestops:
				closest_pokestop_loc = Utils.Location(closest_pokestop["latitude"], closest_pokestop["longitude"])
				pokestop_loc = Utils.Location(pokestop["latitude"], pokestop["longitude"])
				if self.client.location.distance(pokestop_loc) < self.client.location.distance(closest_pokestop_loc):
					closest_pokestop = pokestop
			return closest_pokestop
		return []


	def _parse_pokestops(self, gmo_data):
		found_pokestops = []
		for map_cell in gmo_data.map_cells:
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


	def _parse_pokemon(self, gmo_data):
		found_pokemon = {}
		for map_cell in gmo_data.map_cells:
			# Order matters. We 'prefer' specific message since it has way more details.
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
		return found_pokemon