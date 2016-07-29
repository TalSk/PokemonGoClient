# PokémonGoClient
Pokémon Go client using Pokémon Go endpoints.

## What is this?
The code provides some Pokémon Go functionality; it serves as a client for the Pokémon Go servers.
This tool will let you:
- Scan for Pokémon around your location. (Plus exact location of Pokémon 2 or 1 paws away!)
- Retreive information about Pokéstops and gyms around your location
- Retreive information about your trainer

And in the future, using this tool, the following will be implemented:
- Auto-walker - for hatching eggs easily.
- Auto-PokéScanner
- Auto-PokéStopper
- Auto-PokéCatcher

## Alright, I'm interested!
Some teasers:

* Catching Pokémon

![Catching Pokemon](http://i.imgur.com/HhKG5N4.png)
* Scanning Pokémon

![Pokemon](http://i.imgur.com/AL6OAFg.png)
* Scanning Pokéstops

![Pokestops](http://i.imgur.com/oOkLBaQ.png)
* Getting player info

![Player](http://i.imgur.com/NVeRqQp.png)
* Getting player inventory

![Inventory](http://i.imgur.com/it5qNym.png)
* Getting Settings

![Settings](http://i.imgur.com/uVDFRv6.png)


* Botting!
![Bot](http://i.imgur.com/udNdwBC.png)


## Documentation
- Instantiate a starting location (Using the Location class from `Utils.py`)
- Instantiate a client, giving it the starting location
- Call the `login` function, with your Google Email, and a token extracted from your phone.
- The client supports the following actions (Those are well-documented in `PokemonGoClient.py`:
    * GET_MAP_OBJECT
    * DOWNLOAD_SETTINGS
    * GET_INVENTORY
    * GET_PLAYER
    * ENCOUNTER
    * CATCH_POKEMON
    * RELEASE_POKEMON
    * FORT_DETAILS
    * FORT_SEARCH

Alternatively, you can instantiate a Bot class (from `Bot.py`) using a Client instance.
The bot imitates a normal player playing the game. The bot will:
* Looks for Pokemon around the current location.
* Catches said Pokemon, using an almost-perfect throw, using the worst available pokeball.
* After catching every Pokemon, goes to the closest available Pokestop and spins it (If player inventory isn't full)
* Repeats for profit.
