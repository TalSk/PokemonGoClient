import s2sphere
from random import randint
from geopy.distance import vincenty


def get_neighbors(latitude, longitude):
	r = s2sphere.RegionCoverer()
	r.max_level = 15
	r.min_level = 15
	p1 = s2sphere.LatLng.from_degrees(latitude - 0.005, longitude - 0.005)
	p2 = s2sphere.LatLng.from_degrees(latitude + 0.005, longitude + 0.005)
	return r.get_covering(s2sphere.LatLngRect.from_point_pair(p1, p2))


def randomize_rpc_id():
	return randint(1000000000000000000, 9000000000000000000)

class Location(object):
	def __init__(self, latitude, longitude, altitude=0):
		self.latitude = latitude
		self.longitude = longitude
		self.altitude = altitude

	def change_altitude(self, altitude):
		self.altitude = altitude

	def change_latitude(self, latitude):
		self.latitude = latitude

	def change_longitude(self, longitude):
		self.longitude = longitude

	def distance(self, other):
		src = (self.latitude, self.longitude)
		dst = (other.latitude, other.longitude)
		return vincenty(src, dst) * 1000 # In meters