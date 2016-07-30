import random
import time
import datetime
from Util import Utils, Constants, NetUtil
from BotUtils.Player import Player

class Bot(object):
	"""
		A Bot class, which can play PokemonGo while imitating a human-like behaviour.

		Can be instantanced using a PokemonGoClient.
	"""

	def __init__(self, client):
		self.client = client
		self.player = Player(client)
		self.altitude = self.client.location.altitude


	def _get_random_num(self, minN, maxN):
		return minN + (random.random() * (maxN - minN))


	def _fight_pokemon(self, pokemon, pokemon_location):
		"""
			Fights a pokemon - effectively encounters and catching it.


			pokemon: A dictionary containing three keys:
						  encounter_id -> Pokemon's encounter id
						  spawnpoint_id -> Pokemon's spawnpoint id
						  name -> Pokemon's name
			pokemon_location: A Location class indicating the Pokemon's location.

		"""
		# Encounter pokemon
		enc_res = self.client.encounter(pokemon["encounter_id"], pokemon["spawnpoint_id"], pokemon_location)
		fight_over = False
		while fight_over == False:
			# Gotta wait some random time.
			time.sleep(self._get_random_num(2, 7)) 

			# Choose pokeball
			pokeball_type = self.player.inventory.choose_pokeball()
			if pokeball_type == None:
				print "[I] No pokeballs left."
				return
			print "[I] Using %s pokeball" % pokeball_type

			# Trying to catch pokemon, simulating an excellent max curve ball.
			cp_res = self.client.catch_pokemon(pokemon["encounter_id"], pokemon["spawnpoint_id"], pokeball_type)

			if cp_res.status == 1: # Success
				print "[I] Caught a %s, with %s CP." % (pokemon["name"], enc_res.pokemon.pokemon.cp)
				time.sleep(5)
				# Release pokemon if below CP threshold.
				self.player.maybe_release_pokemon(pokemon["name"], enc_res.pokemon.pokemon.cp, cp_res.captured_pokemon_id)						
				fight_over = True

			elif cp_res.status == 2: # Escape
				print "[I] %s escaped from Pokeball. Trying again" % pokemon["name"]

			elif cp_res.status == 3: # Flee
				print "[I] %s fled :(" % pokemon["name"]
				fight_over = True


	def _catch_nearby_pokemon(self):
		"""
			Catches all nearby pokemon, by getting an list of pokemon in the nearby map.
		"""
		pokemons = self.player.map.get_nearby_pokemon()
		for encounter_id in pokemons:
			pokemon = pokemons[encounter_id]
			# A pokemon is catchable if we have an exact location of it.
			if pokemon["catchable"]:
				# Test if we have at least one pokeball.
				if self.player.inventory.has_pokeballs():
					pokemon_location = Utils.Location(pokemon["latitude"], pokemon["longitude"])
					print "[I] Moving to a %s from %s, %s to %s, %s" % (pokemon["name"], self.client.location.latitude, self.client.location.longitude, pokemon["latitude"], pokemon["longitude"])
					self.player.map.walk_until_near(pokemon_location, Constants.ENCOUNTER_RANGE_METERS - (random.random() * 5))
					self.has_moved = True
					print "[I] Close enough. Trying to catch pokemon"
					self._fight_pokemon(pokemon, pokemon_location)
					time.sleep(5)
				else:
					print "[I] No pokeballs left."
					return


	def _spin_closest_pokestop(self):
		"""
			Spins closest pokestop according to the current player's location.
		"""
		pokestop = self._get_closest_available_pokestop()
		if pokestop:
			pokestop_location = Utils.Location(pokestop["latitude"], pokestop["longitude"])
			print "[I] Moving to a pokestop from %s, %s to %s, %s" % (self.client.location.latitude, self.client.location.longitude, pokestop["latitude"], pokestop["longitude"])
			self.player.map.walk_until_near(pokestop_location, Constants.INTERACTION_RANGE_METERS - (random.random() * 5))
			self.has_moved = True
			print "[I] Moved close enough, spinning..."

			self.client.fort_details(pokestop)
			# Gotta wait between geting details and spinning
			time.sleep(self._get_random_num(2, 4))
			self.client.fort_search(pokestop)
			print "[I] Span a Pokestop at %s, %s" % (pokestop["latitude"], pokestop["longitude"])


	def _get_closest_available_pokestop(self):
		"""
			Gets closest pokestop which wasn't spun in the last 5 minutes.
		"""
		pokestops = self.player.map.get_nearby_pokestops()
		spinnable_pokestops = []
		for pokestop in pokestops:
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


	def _is_playtime(self):
		"""
			Check if current time is between 00:00 AM to 08:00 AM
		"""
		curr_time = time.localtime()
		if curr_time.tm_hour < 8:
			return False
		return True


	def _sleep_till_playtime(self):
		"""
			Sleeps until 08:00 AM.
		"""
		t = time.localtime()
		start = datetime.datetime(year=t.tm_year, month=t.tm_mon, day=t.tm_mday, 
								  hour=t.tm_hour, minute=t.tm_min, second=t.tm_sec)
		end = datetime.datetime(year=t.tm_year, month=t.tm_mon, day=t.tm_mday, 
								  hour=8)
		diff = end-start
		if (diff.total_seconds() > 0):
			print "[I] Sleeping until 08:00 AM. Good night!"
			time.sleep(diff.total_seconds())


	def start(self):
		"""
			Main bot loop.

			- Plays only between 08:00 AM to 00:00 AM.
			- Looks for catchable pokemon (has exact location), and tries to catch them.
			- Throws unneeded items if inventory is full. (Defined as a constant in Player.py)
			- Moves to the closest Pokestop which hasn't been spun the last 5 minutes, and spins it.
		"""
		while 1:
			try:
				if not self._is_playtime():
					self._sleep_till_playtime()
				#self.player.hatch_eggs()
				#self.player.incubate_eggs()
				self.has_moved = False

				self._catch_nearby_pokemon()
				
				self._spin_closest_pokestop()

				self.player.inventory.update()
				if self.player.inventory.count >= 350:
					self.player.throw_items()

				if self.has_moved == False:
					print "[I] Could not catch any pokemon or spin any pokestops, quitting..."
					return

			except NetUtil.ServerDownException:
				print "[I] Servers are down, retrying..."
				pass
			except NetUtil.AuthExpiredException:
				try:
					self.client.login(client.email, client.oauth_token, client.login_type, False)
				except Exception:
					print "[I] Could not authenticate, quitting..."
					return
			# except Exception:
			# 	print "[I] General exception, retrying..."
			# 	pass
			time.sleep(10)