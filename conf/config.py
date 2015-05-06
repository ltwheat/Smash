# Pretty sure we don't actually need this, since it can be calculated from max player kos
#DEFAULT_MAX_KOS = 3
FOR_GLORY_MAX_PLAYER_KOS = 2
# TODO: Write method to turn a code into pretty names using these two dicts
ATK_CODES_TO_NAMES = {"J": "Jab", "D": "Dash", "T": "Tilt", "S": "Smash",
                      "A": "Aerial", "B": "Special", "H": "Throw"}
DIRECTION_CODES_TO_NAMES = {"U": "Up", "D": "Down", "N": "Neutral",
                            "F": "Forward", "B": "Back", "FI": "Final"}
# TODO: This is the most efficient way to list these in terms of actual file
#       space, but the actual searching would be more efficient with a dict
#       like {"dthrow": "DT", "downthrow": "DT"} I think.
# TODO: Write utility method to .lower() and split and join all move name strings
MOVE_CODES_TO_ALLOWED_NAMES = {"J": [], "D": [], "UT": ["utilt", "uptilt"],
    "DT": ["dtilt", "downtilt"], "FT": ["ftilt", "forwardtilt"],
    "US": ["usmash", "upsmash"], "DS": ["dsmash", "downsmash"],
    "FS": ["fsmash", "forwardsmash"], "UA": ["uair", "upair"],
    "DA": ["dair", "downair"], "FA": ["fair", "forwardair"],
    "BA": ["bair", "backair"], "NA": ["nair", "neutralair"],
    "UB": ["upb", "uspecial", "upspecial"],
    "DB": ["downb", "dspecial", "downspecial"],
    "FB": ["sideb", "forwardb", "sspecial",
           "sidespecial", "fspecial", "forwardspecial"],
    "NB": ["b", "special", "neutralb", "nspecial", "neutralspecial"],
    "UH": ["uthrow", "upthrow"], "DH": ["dthrow", "downthrow"],
    "FH": ["fthrow", "forwardthrow"], "BH": ["bthrow", "backthrow"]}
