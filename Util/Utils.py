import s2sphere
from random import randint


def get_neighbors(latitude, longitude):
	r = s2sphere.RegionCoverer()
	r.max_level = 15
	r.min_level = 15
	p1 = s2sphere.LatLng.from_degrees(latitude - 0.005, longitude - 0.005)
	p2 = s2sphere.LatLng.from_degrees(latitude + 0.005, longitude + 0.005)
	return r.get_covering(s2sphere.LatLngRect.from_point_pair(p1, p2))


def randomize_rpc_id():
	return randint(1000000000000000000, 9000000000000000000)