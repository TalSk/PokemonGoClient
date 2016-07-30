from Enums import PlayerEnums_pb2

class Inventory(object):
	"""
		Inventory class, which lets user perform actions involving player's inventory.
	"""
	def __init__(self, client):
		self.client = client
		self.update()


	def update(self):
		"""
			Updates current inventory information, specifically total item count and pokeball information.
		"""
		self.inventory = self.client.get_inventory()

		self.count = self.get_inventory_total_count()

		pokeballs = self.get_inventory_item_count(PlayerEnums_pb2.ITEM_POKE_BALL)
		great_pokeballs = self.get_inventory_item_count(PlayerEnums_pb2.ITEM_GREAT_BALL)
		ultra_pokeballs = self.get_inventory_item_count(PlayerEnums_pb2.ITEM_ULTRA_BALL)
		master_pokeballs = self.get_inventory_item_count(PlayerEnums_pb2.ITEM_MASTER_BALL)
		self.pokeballs = {
			'Normal': pokeballs,
			'Great': great_pokeballs,
			'Ultra': ultra_pokeballs,
			'Master': master_pokeballs
		}

	def has_pokeballs(self):
		"""
			Returns true whether player has some pokeballs (besides master).
		"""
		if self.pokeballs['Normal'] or self.pokeballs['Great'] or self.pokeballs['Ultra']:
			return True
		return False


	def choose_pokeball(self):
		"""
			Chooses first available pokeball (besides master). Going from worst to best.
		"""
		if self.pokeballs['Normal']:
			self.pokeballs['Normal'] -= 1
			return 'Normal'
		if self.pokeballs['Great']:
			self.pokeballs['Great'] -= 1
			return 'Great'
		if self.pokeballs['Ultra']:
			self.pokeballs['Ultra'] -= 1
			return 'Ultra'
		return None


	def get_inventory_total_count(self):
		""" 
			Gets total inventory item count.
		"""
		count = 0
		for item in self.inventory.inventory_delta.inventory_items:
			if item.inventory_item_data.item:
				if item.inventory_item_data.item.count:
					count += item.inventory_item_data.item.count
		return count


	def get_inventory_item_count(self, item_id):
		"""
			Gets a specific inventory item count.


			item_id: The request item id to count.
		"""
		for item in self.inventory.inventory_delta.inventory_items:
			if item.inventory_item_data.item:
				if item.inventory_item_data.item.item == item_id:
					if item.inventory_item_data.item.count:
						return item.inventory_item_data.item.count
		return 0