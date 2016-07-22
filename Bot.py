import threading
from Util import Utils


class Bot(object):
	def __init__(self, client):
		self.client = client
		self.current_location = self.client.location

		self.heartbeat_thread = threading.Thread(target=heartbeat)
		self.heartbeat_thread.start()


	def heartbeat(self):
	"""
		Sends a heartbeat to the server; effectively sending a get map objects request
	"""
		self.gmo_latest = self.client.get_map_objects(self.current_location)
		time.sleep(10)