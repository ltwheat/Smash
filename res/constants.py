# TODO: Should these be ID to name instead?
SMASHER_NAME_TO_ID = {"Lt Wheat": 1}

FIGHTER_NAME_TO_ID = {"Mario": 1, "Luigi": 2, "Dr. Mario": 3, "Peach": 4,
                        "Bowser": 5, "Yoshi": 6, "Wario": 7, "Donkey Kong": 8,
                        "Diddy Kong": 9, "Link": 10, "Toon Link": 11,
                        "Zelda": 12, "Sheik": 13, "Ganondorf": 14, "Samus": 15,
                        "Zero Suit Samus": 16, "Kirby": 17, "Meta Knight": 18,
                        "King Dedede": 19, "Fox": 20, "Falco": 21,
                        "Pikachu": 22, "Jigglypuff": 23, "Charizard": 24,
                        "Lucario": 25, "Captain Falcon": 26, "Ness": 27,
                        "Marth": 28, "Ike": 29, "Mr. Game & Watch": 30,
                        "Pit": 31, "Olimar": 32, "R.O.B.": 33, "Sonic": 34,
                        "Rosalina & Luma": 35, "Bowser Jr.": 36, "Greninja": 37,
                        "Lucina": 38, "Robin": 39, "Palutena": 40,
                        "Dark Pit": 41, "Little Mac": 42, "Villager": 43,
                        "Wii Fit Trainer": 44, "Shulk": 45, "Duck Hunt": 46,
                        "Mega Man": 47, "Pac-Man": 48, "Mii Gunner": 49,
                        "Mii Brawler": 50, "Mii Swordfighter": 51, "Mewtwo": 52}

STAGE_NAME_TO_ID = {"Final Destination": 0, "Battlefield": 1, "3D Land": 2,
                    "Golden Plains": 3, "Rainbow Road": 4, "Paper Mario": 5,
                    "Mushroomy Kingdom": 6, "Jungle Japes": 7,
                    "Gerudo Valley": 8, "Spirit Train": 9, "Brinstar": 10,
                    "Yoshi's Island (Brawl)": 11, "Dream Land": 12,
                    "Corneria": 13, "Unova Pokemon League": 14,
                    "Prism Tower": 15, "Mute City": 16, "Magicant": 17,
                    "Arena Ferox": 18, "Flat Zone 2": 19,
                    "Reset Bomb Forest": 20, "Warioware, Inc.": 21,
                    "Distant Planet": 22, "Tortimer Island": 23,
                    "Boxing Ring": 24, "Gaur Plain": 25, "Balloon Fight": 26,
                    "Living Room": 27, "Find Mii": 28, "Tomodachi Life": 29,
                    "Pictochat 2": 30, "Green Hill Zone": 31, "Wily Castle": 32,
                    "PAC-MAZE": 33, "Big Battlefield": 34, "Mario Galaxy": 35,
                    "Mushroom Kingdom U": 36, "Mario Circuit": 37,
                    "Delfino Plaza": 38, "Luigi's Mansion": 39,
                    "Mario Circuit (Brawl)": 40, "Wooly World": 41,
                    "Yoshi's Island (Melee)": 42, "Gamer": 43,
                    "Jungle Hijinxs": 44, "Kongo Jungle 64": 45, "75m": 46,
                    "Skyloft": 47, "Temple": 48, "Bridge of Eldin": 49,
                    "Pyrosphere": 50, "Norfair": 51,
                    "The Great Cave Offensive": 52, "Halberd": 53,
                    "Orbital Gate Assault": 54, "Lylat Cruise": 55,
                    "Kalos Pokemon League": 56, "Pokemon Stadium 2": 57,
                    "Port Town Aero Dive": 58, "Onett": 59, "Coliseum": 60,
                    "Castle Siege": 61, "Flat Zone X": 62,
                    "Palutena's Temple": 63, "Skyworld": 64,
                    "Garden of Hope": 65, "Town and City": 67,
                    "Smashville": 68, "Wii Fit Studio": 69, "Duck Hunt": 70,
                    "Wrecking Crew": 71, "Pilotwings": 72, "Wuhu Island": 73,
                    "Windy Hill Zone": 74, "PAC-LAND": 75, "Miiverse": 76}

# Any characters with a non-standard number of palette swaps should be mapped
# here
FIGHTER_NAME_TO_NUM_PALETTES = {"Little Mac": 16}

# TODO: This is temporary until I get a better system in place and convert all
#       existing matches
MOVES = ["jab", "ftilt", "dash", "fsmash", "dtilt", "dsmash", "utilt",
         "usmash", "nspecial", "sspecial", "dspecial", "uspecial",
         "fthrow", "bthrow", "dthrow", "uthrow", "nair", "fair", "bair",
         "dair", "uair"]

# TODO: Add variants and a standardizer, so for instance, accept 'up' as well
#       as 'top', but still store 'top'
DIRECTIONS = ['right', 'left', 'top', 'bottom']
