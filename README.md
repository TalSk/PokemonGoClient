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

## Documentation
- Instantiate a starting location (Using the Location class from `Utils.py`)
- Instantiate a client, giving it the starting location
- Call the `login` function, with your Google Email, and a token extracted from your phone.
- The client support the following actions:
    * GET_MAP_OBJECT
    * DOWNLOAD_SETTINGS
    * GET_INVENTORY
    * GET_PLAYER
    * ENCOUNTER
    * CATCH_POKEMON
    * RELEASE_POKEMON
    * FORT_DETAILS
    * FORT_SEARCH
