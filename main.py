from PokemonGoClient import *
from Util import Utils
import Bot
		

if __name__ == '__main__':
	start_location = Utils.Location(32.0877051133, 34.7702087537, 37.5)
	client = PokemonGoClient(start_location, log=True)
	client.login("tal.skverer@gmail.com", "oauth2rt_1/#", "Google")

	b = Bot.Bot(client)
	b.start()


# TODO:
#		Hatch eggs
# 		Look for TODOs in code
#		Document everything
#		PTR Login
#		Google login with password