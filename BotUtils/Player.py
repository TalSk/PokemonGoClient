from BotUtils.Inventory import Inventory
from BotUtils.Map import Map
import time

class Player(object):
	"""
		A class representing a PokemonGo Player.
	"""
	MIN_CP = 300
	ITEMS_TO_THROW = {
		'POTION' : 101,
  		'SUPER_POTION' : 102,
  		'REVIVE' : 201,
  		'RAZZ_BERRY' : 701
	}

	def __init__(self, client):
		self.client = client
		self.update()


	def update(self):
		"""
			Updates player information.
		"""
		self.player = self.client.get_player()
		self.inventory = Inventory(self.client)
		self.map = Map(self.client)


	def maybe_release_pokemon(self, name, pokemon_cp, pokemon_id):
		"""
			Releases a pokemon if its CP is lower than the minimum CP.


			name: Pokemon's name.
			pokemon_cp: Pokemon's CP.
			pokemon_id: Pokemon's id.
		"""
		if self.MIN_CP > pokemon_cp:
			self.client.release_pokemon(pokemon_id)
			print "[I] Released %s. (%s CP)." % (name, pokemon_cp)


	def throw_items(self):
		"""
			Throws unneeded items from inventory.
		"""
		for item in self.ITEMS_TO_THROW:
			count = self.inventory.get_inventory_item_count(self.ITEMS_TO_THROW[item])
			self.client.recycle_inventory_item(self.ITEMS_TO_THROW[item], count)
			print "[I] Threw %s %s" % (count, item)
			time.sleep(5)


	def hatch_eggs(self):
		"""
			Hatches eggs which are ready.
		"""
		pass