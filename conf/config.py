# Pretty sure we don't actually need this, since it can be calculated from max player kos
#DEFAULT_MAX_KOS = 3
FOR_GLORY_MAX_PLAYER_KOS = 2
# TODO: Write method to turn a code into pretty names using these two dicts
ATK_CODES_TO_NAMES = {"J": "Jab", "D": "Dash", "T": "Tilt", "S": "Smash",
                      "A": "Aerial", "B": "Special", "H": "Throw"}
DIRECTION_CODES_TO_NAMES = {"U": "Up", "D": "Down", "N": "Neutral",
                            "F": "Forward", "B": "Back", "FI": "Final"}
# TODO: Write utility method to .lower() and split and join all move name strings
# This way of storing the map of acceptable move names is uglier than
# MOVE_CODES_TO_ALLOWED_NAMES (below), but it's more efficient and fits the
# design better, since the keys should be the input from the user.
ALLOWED_NAMES_TO_MOVE_CODES = {"utilt": "UT", "uptilt": "UT", "dtilt": "DT",
    "downtilt": "DT", "ftilt": "FT", "forwardtilt": "FT", "usmash": "US",
    "upsmash": "US", "dsmash": "DS", "downsmash": "DS", "fsmash": "FS",
    "forwardsmash": "FS", "uair": "UA", "upair": "UA", "dair": "DA",
    "downair": "DA", "fair": "FA", "forwardair": "FA", "bair": "BA",
    "backair": "BA", "nair": "NA", "neutralair": "NA", "upb": "UB",
    "uspecial": "UB", "upspecial": "UB", "downb": "DB", "dspcial": "DB",
    "downspecial": "DB", "sideb": "FB", "forwardb": "FB", "sspecial": "FB",
    "sidespecial": "FB", "fspecial": "FB", "forwardspecial": "FB", "b": "NB",
    "special": "NB", "neutralb": "NB", "nspecial": "NB", "neutralspecial": "NB",
    "uthrow": "UH", "upthrow": "UH", "dthrow": "DH", "downthrow": "DH",
    "fthrow": "FH", "forwardthrow": "FH", "bthrow": "BH", "backthrow": "BH"}
#MOVE_CODES_TO_ALLOWED_NAMES = {"J": [], "D": [], "UT": ["utilt", "uptilt"],
#    "DT": ["dtilt", "downtilt"], "FT": ["ftilt", "forwardtilt"],
#    "US": ["usmash", "upsmash"], "DS": ["dsmash", "downsmash"],
#    "FS": ["fsmash", "forwardsmash"], "UA": ["uair", "upair"],
#    "DA": ["dair", "downair"], "FA": ["fair", "forwardair"],
#    "BA": ["bair", "backair"], "NA": ["nair", "neutralair"],
#    "UB": ["upb", "uspecial", "upspecial"],
#    "DB": ["downb", "dspecial", "downspecial"],
#    "FB": ["sideb", "forwardb", "sspecial",
#           "sidespecial", "fspecial", "forwardspecial"],
#    "NB": ["b", "special", "neutralb", "nspecial", "neutralspecial"],
#    "UH": ["uthrow", "upthrow"], "DH": ["dthrow", "downthrow"],
#    "FH": ["fthrow", "forwardthrow"], "BH": ["bthrow", "backthrow"]}
