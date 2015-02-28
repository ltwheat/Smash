#!/usr/bin/env

import datetime
import pymongo
import traceback

from common_mongo import smash_conn
from fighter import Fighter
from ko import KO
from match import Match
from player import Player
from smasher import Smasher
from stage import Stage
##### TODOS #####
# 1) A couple of the keys should always be 0 for FG--have the script error
#    out if they aren't
# 2) IDs? object_id (match_id, in this case) is stored in mongo automatically
#    but do we need an external one? Should have one for players, at least.
#    a) No way to differentiate other players aside from name, though...is this
#       different in WiiU version?


##### NOTES #####
# time_alive == 'out at'. Figured 'time_alive' was more clear
# launch_distance: TODO: Is that me or him?
# max_launch(er)_speed: which one is me, which one is him?
# longest_drought: longest amount of time without throwing out an attack
# transformation_time: total time spent in alternate state. Should always
#                      be zero in FG
dt = datetime.datetime.now()
dur = 60
lylat = Stage(name="Lylat Cruise")
smasher_lt = Smasher(tag="Lt Wheat")
luigi = Fighter(name="Luigi")
mario = Fighter(name="Mario")
kos1 = [KO("uspecial",101,"top",54), KO("fsmash",120,"right",146)]
kos2 = [KO("dsmash",143,"left",123)]
stats_lt={"falls": 1, "SDs": 0, "time_alive": -1, "damage_given": 286,
         "damage_taken": 190, "damage_recovered": 0, "peak_damage": 105,
         "launch_distance": 302, "ground_time": 115, "air_time": 71,
         "hit_percentage": 44, "ground_attacks": 59, "air_attacks": 20,
         "smash_attacks": 8, "grabs": 13, "throws": 4, "edge_grabs": 5,
         "projectiles": 25, "items_grabbed": 0, "max_launch_speed": 130,
         "max_launcher_speed": 145, "longest_drought": 9,
         "transformation_time": 0, "final_smashes": 0}

player1 = Player(smasher_lt, luigi, True, kos1, stats_lt)
player2 = Player(smasher_lt, mario, False, kos2, stats_lt)


# Construct a Fighter from a dict
def dict_to_fighter(fighter_dict):
    try:
        name = fighter_dict['name']
        fighter_id = fighter_dict['fighter_id']
        fighter = Fighter(name, fighter_id)
    except Exception:
        print("Unknown error lol")
    return fighter

# Construct a KO from a dict
def dict_to_ko(ko_dict):
    try:
        move = ko_dict['move']
        damage = ko_dict['damage']
        direction = ko_dict['direction']
        time = ko_dict['time']        
        ko = KO(move, damage, direction, time)
    except Exception:
        print("Unknown error lol")
        traceback.print_exc()
    return ko

# Construct a Match from a dict
def dict_to_match(match_dict):
    try:
        date = match_dict['date']
        duration = match_dict['duration']
        stage = dict_to_stage(match_dict['stage'])
        player1 = dict_to_player(match_dict['player1'])
        player2 = dict_to_player(match_dict['player2'])
        time_limit = match_dict['time_limit']
        match = Match(date, duration, stage, player1, player2, time_limit)
    except Exception:
        print("Unknown error lol")
        traceback.print_exc()
    return match

# Construct a Player from a dict
def dict_to_player(player_dict):
    try:
        # Convert list of KOs
        kos = []
        for ko in player_dict['kos']:
            kos.append(dict_to_ko(ko))

        smasher = dict_to_smasher(player_dict['smasher'])
        fighter = dict_to_fighter(player_dict['fighter'])
        palette = player_dict['palette']
        winner = player_dict['winner']
        stats = player_dict['stats']
        player = Player(smasher, fighter, winner, kos, stats, palette)
    except Exception:
        print("Unknown error lol")
        traceback.print_exc()
    return player

# Construct a Smasher from a dict
def dict_to_smasher(smasher_dict):
    try:
        mii_name = smasher_dict['mii_name']
        tag = smasher_dict['tag']
        smasher_id = smasher_dict['smasher_id']
        smasher = Smasher(mii_name, tag, smasher_id)
    except Exception:
        print("Unknown error lol")
    return smasher

# Construct a Stage from a dict
def dict_to_stage(stage_dict):
    try:
        name = stage_dict['name']
        stage_id = stage_dict['stage_id']
        omega = stage_dict['omega']
        stage = Stage(name, stage_id, omega)
    except Exception:
        print("Unknown error lol")
    return stage

# Wrapper method for entering match info. Type check and ignore blank answers
def input_match_attr(prompt_string, attr_type=str):
    val = ""
    while(val==""):
    # Prompt for input (assume empty string is an accident)
        val = input(prompt_string)

    if attr_type == bool:
        if val.lower() == "false":
            val = False

    # TODO: try/except this part once you figure out how to switch control b/w
    #       this func and enter_match(). For now, this throwing an error will
    #       suffice.
    val = attr_type(val)
    return val

# TODO: This needs some work after all the refactoring stuff.
def enter_match(date_time=None, defaults=True, omega=True):
    print("Enter match information:")

    # TODO: Putting KO entry at the beginning doesn't really help unless we
    #       record them as a come, rather than one player at a time.
    kos1 = []
    print("Assuming you're watching the replay, tell me about the KOs first")
    # TODO: For Glory, limit b/w 0 and 2
    num_kos1 = int(input("How many KOs did you get? "))
    if num_kos1 != 0:
        print("Tell me about those.")
    for num in range(num_kos1):
        print("KO {0}:".format(num + 1))
        ko_move = input_match_attr("Move? ")
        ko_dmg = input_match_attr("% Damage? ", int)
        ko_side = input_match_attr("Off of which side of the screen? ")
        ko_time = input_match_attr("How long into the match (s)? ", int)
        ko = KO(ko_move, ko_dmg, ko_side, ko_time)
        kos1.append(ko)

    kos2 = []
    num_kos2 = int(input("How many KOs did they get? "))
    if num_kos2 != 0:
        print("Tell me about those.")
    for num in range(num_kos2):
        print("KO {0}:".format(num + 1))
        ko_move = input_match_attr("Move? ")
        ko_dmg = input_match_attr("% Damage? ", int)
        ko_side = input_match_attr("Off of which side of the screen? ")
        ko_time = input_match_attr("How long into the match (s)? ", int)
        ko = KO(ko_move, ko_dmg, ko_side, ko_time)
        kos2.append(ko)
                      
    # TODO: Parse all kinds of datetime strings, or come up with another way
    #       to enter them (optional arg?), eg Feb 2, February 2nd, 2/2
    date = input("Date: (NOTE: This doesn't actually matter)")
    if date_time == None:
        # TODO: There's probably a cleaner way to do this...
        date_time = datetime.datetime.today()
        day = date_time.day
        month = date_time.month
        year = date_time.year
        date_time = datetime.datetime(year, month, day)
    duration = input_match_attr("Duration (s): ", int)

    # TODO: Make this a separate function
    stage_name = input_match_attr("Stage: ")
    if not defaults == True:
        omega = input(" (Omega?) ", bool)
    stage = Stage(name=stage_name, omega=omega)
    print("First, how did you do?")

    # TODO: Make this a separate function
    print("PLAYER 1 (You):")
    smasher1_tag = "Lt Wheat"
    smasher1_mii_name = "Mr. Wheat"
    if not defaults == True:
        smasher1_tag = input_match_attr("Tag: ")
        smasher1_mii_name = input_match_attr("Mii Name: ")
    smasher1 = Smasher(mii_name=smasher1_mii_name, tag=smasher1_tag)
    
    fighter1_name = input_match_attr("Character: ")
    fighter1 = Fighter(name=fighter1_name)
    
    winner1 = input_match_attr("Did you win ('false' for 'no')", bool)
    stats1 = {}

    print("Other stats:")
    stats1['falls'] = input_match_attr("Falls: ", int)
    stats1['SDs'] = input_match_attr("SDs (Remember this is special): ", int)
    # TODO: FOR GLORY: time_alive doesn't need to be entered--if it's for the
    #       winner, it's n/a or -1, and for the loser, it's the same as
    #       duration
    stats1['time_alive'] = -1
    if not winner1:
        stats1['time_alive'] = input_match_attr("Time Alive: ", int)
    # TODO: FOR GLORY: damage_given and damage_taken are inverses for opponents
    stats1['damage_given'] = input_match_attr("Damage Given: ", int)
    stats1['damage_taken'] = input_match_attr("Damage Taken: ", int)
    stats1['damage_recovered'] = input_match_attr("Damage Recovered: ", int)
    # TODO: peak_damage can be calculated from all KOs
    stats1['peak_damage'] = input_match_attr("Peak Damage: ", int)
    stats1['launch_distance'] = input_match_attr("Launch Distance: ", int)
    stats1['ground_time'] = input_match_attr("Ground Time: ", int)
    stats1['air_time'] = input_match_attr("Air Time: ", int)
    stats1['hit_percentage'] = input_match_attr("Hit Percentage: ", int)
    stats1['ground_attacks'] = input_match_attr("Ground Attacks: ", int)
    stats1['air_attacks'] = input_match_attr("Air Attacks: ", int)
    stats1['smash_attacks'] = input_match_attr("Smash Attacks: ", int)
    stats1['grabs'] = input_match_attr("Grabs: ", int)
    # TODO: throws must be 0 if grabs is 0
    stats1['throws'] = input_match_attr("Throws: ", int)
    stats1['edge_grabs'] = input_match_attr("Edge Grabs: ", int)
    stats1['projectiles'] = input_match_attr("Projectiles: ", int)
    stats1['items_grabbed'] = input_match_attr("Items Grabbed: ", int)
    # TODO: FOR GLORY: max_launch(er)_speed are inverses for opponents
    stats1['max_launch_speed'] = input_match_attr("Max Launch Speed: ", int)
    stats1['max_launcher_speed'] = input_match_attr("Max Launcher Speed: ", int)
    stats1['longest_drought'] = input_match_attr("Longest Drought: ", int)
    stats1['transformation_time'] = input_match_attr("Transformation Time: ",
                                                     int)
    stats1['final_smashes'] = input_match_attr("Final Smashes: ", int)

    player1_palette = input_match_attr("Palette #: ", int)

    player1 = Player(smasher1, fighter1, winner1, kos1, stats1,
                     player1_palette)
    # TODO: Make this a separate function
    print("PLAYER 2 (Opponent):")
    # TODO: This needs to allow for other names, figure out a solution for
    #       that first
    smasher2_tag = ""
    if not defaults == True:
        smasher2_tag = input_match_attr("Tag: ")
    smasher2_mii_name = input_match_attr("Mii name: ")
    smasher2 = Smasher(mii_name=smasher2_mii_name, tag=smasher2_tag)
    
    fighter2_name = input_match_attr("Character: ")
    fighter2 = Fighter(name=fighter2_name)
    
    winner2 = not winner1
    
    stats2 = {}
    stats2['falls'] = input_match_attr("Falls: ", int)
    stats2['SDs'] = input_match_attr("SDs (Remember this is special): ", int)
    stats2['time_alive'] = -1
    if not winner2:
        stats2['time_alive'] = input_match_attr("Time Alive: ", int)
    stats2['damage_given'] = input_match_attr("Damage Given: ", int)
    stats2['damage_taken'] = input_match_attr("Damage Taken: ", int)
    stats2['damage_recovered'] = input_match_attr("Damage Recovered: ", int)
    stats2['peak_damage'] = input_match_attr("Peak Damage: ", int)
    stats2['launch_distance'] = input_match_attr("Launch Distance: ", int)
    stats2['ground_time'] = input_match_attr("Ground Time: ", int)
    stats2['air_time'] = input_match_attr("Air Time: ", int)
    stats2['hit_percentage'] = input_match_attr("Hit Percentage: ", int)
    stats2['ground_attacks'] = input_match_attr("Ground Attacks: ", int)
    stats2['air_attacks'] = input_match_attr("Air Attacks: ", int)
    stats2['smash_attacks'] = input_match_attr("Smash Attacks: ", int)
    stats2['grabs'] = input_match_attr("Grabs: ", int)
    stats2['throws'] = input_match_attr("Throws: ", int)
    stats2['edge_grabs'] = input_match_attr("Edge Grabs: ", int)
    stats2['projectiles'] = input_match_attr("Projectiles: ", int)
    stats2['items_grabbed'] = input_match_attr("Items Grabbed: ", int)
    stats2['max_launch_speed'] = input_match_attr("Max Launch Speed: ", int)
    stats2['max_launcher_speed'] = input_match_attr("Max Launcher Speed: ", int)
    stats2['longest_drought'] = input_match_attr("Longest Drought: ", int)
    stats2['transformation_time'] = input_match_attr("Transformation Time: ",
                                                     int)
    stats2['final_smashes'] = input_match_attr("Final Smashes: ", int)

    player2_palette = input_match_attr("Palette #: ", int)

    player2 = Player(smasher2, fighter2, winner2, kos2, stats2,
                     player2_palette)


    match = Match(date_time, duration, stage, player1, player2)
    smash_conn.store_match(match.convert_to_dict())
    print(match.get_synopsis())

def enter_test_match():
    match = Match(dt, dur, lylat, player1, player2)
    store_match(match.convert_to_dict())
    print(match.get_synopsis())

if __name__ == "__main__":
    #enter_match()
    pass
