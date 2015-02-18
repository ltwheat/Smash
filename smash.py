#!/usr/bin/env

import datetime
from stage import Stage

# TODO: Write a script that makes it easier to enter all this info.
# 1) A couple of the keys should always be 0 for FG--have the script error
#    out if they aren't
# 2) IDs? object_id (match_id, in this case) is stored in mongo automatically
#    but do we need an external one? Should have one for players, at least.
#    a) No way to differentiate other players aside from name, though...is this
#       different in WiiU version?
# 3) Should we keep stage around? FG will always be Omega, so doesn't matter,
#    but still could be interesting nonetheless and will port easily to
#    competitive format
# 4) MAKE PLAYERS, MATCHES AND STAGES INTO OBJECTS
# 5) Extra info not in match that's useful:
#    a) % at when killed for each stock
#    b) SDs should be recorded less leniently than in game. If I've been hit
#       recently but botch the recovery, that should be an SD
#    c) Direction of each KO?
# 6) Stage -> stage_id?

##### NOTES #####
# time_alive == 'out at'. Figured 'time_alive was more clear
# launch_distance: TODO: Is that me or him?
# max_launch(er)_speed: which one is me, which one is him?
# longest_drought: longest amount of time without throwing out an attack
# transformation_time: total time spent in alternate state. Should always
#                      be zero in FG

player1={"name": "Mr. Wheat", "character": "Duck Hunt", "winner": True,
         "KOs": 2, "Falls": 1, "SDs": 0, "time_alive": -1, "damage_given": 286,
         "damage_taken": 190, "damage_recoverd": 0, "peak_damage": 105,
         "launch_distance": 302, "ground_time": 115, "air_time": 71,
         "hit_percentage": 44, "ground_attacks": 59, "air_attacks": 20,
         "smash_attacks": 8, "grabs": 13, "throws": 4, "edge_grabs": 5,
         "projectiles": 25, "items_grabbed": 0, "max_launch_speed": 130,
         "max_launcher_speed": 145, "longest_drought": 9,
         "transformation_time": 0, "final_smashes": 0}

player2={"TODO": "Fill this in later"}

match={"date": datetime.datetime(2014, 11, 21), "duration": 186,
       "stage": "Gaur Plains", "player1": player1, "player2": player2}

def enter_match(defaults=True, omega=True):
    # TODO: Need type checking for all of this
    print("Enter match information:")
    date = input("Date: ")
    duration = input("Duration (s): ")
    stage = input("Stage: ")
    if not defaults == True:
        omega = input(" (Omega?) ")
    print("First, how did you do?")

    # TODO: Make this a separate function
    print("PLAYER 1 (You):")
    smasher1_name = "Lt Wheat"
    if not defaults == True:
        smasher1_name = input("Name: ")
    fighter1_name = input("Character: ")
    winner1 = input("Did they win?")
    #stats1 = input("stats: ")

    print("PLAYER 2 (Opponent):")
    smasher2_name = input("Name: ")
    fighter2_name = input("Character: ")
    winner2 = input("Did they win?")
    #stats2 = input("stats: ")
    #info = prompt(all_match_info_player1)
    #stage_name = prompt("Stage?   ")

    #stage = Stage(name=stage_name, omega=omega)
    #construct match
    #mongodao.store(match)

if __name__ == "__main__":
    enter_match()
