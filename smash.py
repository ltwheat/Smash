#!/usr/bin/env

import datetime
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
# 3) Long-term: Handle team matches


##### NOTES #####
# time_alive == 'out at'. Figured 'time_alive' was more clear
# launch_distance: TODO: Is that me or him?
# max_launch(er)_speed: which one is me, which one is him?
# longest_drought: longest amount of time without throwing out an attack
# transformation_time: total time spent in alternate state. Should always
#                      be zero in FG

### SAMPLE OBJECTS ###
#dt = datetime.datetime.now()
#dur = 60
#lylat = Stage(name="Lylat Cruise")
#smasher_lt = Smasher(tag="Lt Wheat")
#luigi = Fighter(name="Luigi")
#mario = Fighter(name="Mario")
#kos1 = [KO("uspecial",101,"top",54), KO("fsmash",120,"right",146)]
#kos2 = [KO("dsmash",143,"left",123)]
#stats_lt={"falls": 1, "SDs": 0, "time_alive": -1, "damage_given": 286,
#         "damage_taken": 190, "damage_recovered": 0, "peak_damage": 105,
#         "launch_distance": 302, "ground_time": 115, "air_time": 71,
#         "hit_percentage": 44, "ground_attacks": 59, "air_attacks": 20,
#         "smash_attacks": 8, "grabs": 13, "throws": 4, "edge_grabs": 5,
#         "projectiles": 25, "items_grabbed": 0, "max_launch_speed": 130,
#         "max_launcher_speed": 145, "longest_drought": 9,
#         "transformation_time": 0, "final_smashes": 0}
#player1 = Player(smasher_lt, luigi, True, kos1, stats_lt)
#player2 = Player(smasher_lt, mario, False, kos2, stats_lt)


# Construct a Fighter from a dict
def dict_to_fighter(fighter_dict):
    try:
        name = fighter_dict['name']
        fighter_id = fighter_dict['fighter_id']
        fighter = Fighter(name, fighter_id)
    except Exception:
        print("Unknown error lol")
        traceback.print_exc()
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
        traceback.print_exc()
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
        traceback.print_exc()
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

def enter_ko():
    # TODO: Since the move instantiation doesn't happen til the end of this
    #       method, the user can input a bad move and have to enter the rest of
    #       the info til an error is thrown, which is annoying. Maybe check the
    #       acceptable moves right after the move is entered?
    ko_move = input_match_attr("Move? ")
    ko_dmg = input_match_attr("% Damage? ", int)
    ko_side = input_match_attr("Off of which side of the screen? ")
    # TODO: Ask for timer instead of length of time, more reliable
    ko_time = input_match_attr("How long into the match (s)? ", int)
    ko = KO(ko_move, ko_dmg, ko_side, ko_time)
    return ko
    #print("KO: {0}".format(ko.convert_to_dict()))

# Enter all kos for the match
def enter_kos(for_glory=True):
    # TODO: These should be config items, since we also use them in enter_stats
    max_player_kos = 2
    if for_glory == False:
        max_player_kos = input_match_attr("How many stock? ", int)
    max_match_kos = max_player_kos * 2 - 1

    # Player attributes
    kos1 = []
    kos2 = []
    sds1 = 0
    sds2 = 0
    last_fall_time = -1
    all_kos_entered = False
    while not all_kos_entered:
        if len(kos1) + len(kos2) + sds1 + sds2 == 0:
            print("First death:")
        else:
            print("Next death:")

        # SD
        sd = input_match_attr("Was it an SD? ")
        if sd.lower() in ['y', 'yes', 'true']:
            # TODO: Think about adding a time for SDs, or, *gasp*, making a
            #       separate class for them
            player_sd = input_match_attr("Which player SD'd? ", int)
            if player_sd == 1:
                sds1 += 1
            else:
                sds2 += 1
            # The last known fall was a SD, so we don't know when the last fall
            # was
            last_fall_time = -1

        # KO
        else:
            player_ko = input_match_attr("Which player scored the KO? ", int)
            ko = enter_ko()
            if player_ko == 1:
                kos1.append(ko)
            # Assume the other player can have any port, not just 2.
            else:
                kos2.append(ko)
            last_fall_time = ko.time
            
        p1_falls = len(kos2) + sds1
        p2_falls = len(kos1) + sds2
        all_kos_entered = (p1_falls == max_player_kos) or \
                          (p2_falls == max_player_kos)
    return kos1, kos2, sds1, sds2, last_fall_time

# Enter Stage
def enter_stage(for_glory=True):
    stage_name = input_match_attr("Stage: ")
    omega = True
    if not for_glory == True:
        omega = input(" (Omega?) ", bool)
    stage = Stage(name=stage_name, omega=omega)
    return stage

# Enter Smasher
# TODO: Should this allow for entering a smasher with an id, too?
def enter_smasher(defaults=True):
    smasher_tag = "Lt Wheat"
    smasher_mii_name = "Mr. Wheat"
    if not defaults == True:
        smasher_tag = ""
        smasher_mii_name = input_match_attr("Mii Name: ")
    smasher = Smasher(mii_name=smasher_mii_name, tag=smasher_tag)
    return smasher

# Enter Player stats
def enter_player_stats(winner, kos, sds, for_glory=True):
    # TODO: Think about passing in both players' information--if we do, we can
    #       fairly easily calculate the following:
    #       falls
    #       peak_damage
    #       max_launch(er)_speed
    stats = {}
    max_player_kos = 2
    if for_glory == False:
        max_player_kos = input_match_attr("How many stock? ")
    stats['falls'] = max_player_kos - sds
    if winner == True:
        stats['falls'] = input_match_attr("Falls: ", int)
    stats['SDs'] = sds
    #========= CAN'T PUT IN MATCH CUZ REPLAYS SUCK =======#
    ## TODO: FOR GLORY: time_alive doesn't need to be entered--if it's for the
    ##       winner, it's n/a or -1, and for the loser, it's the same as
    ##       duration...so pass in duration
    ##time_alive = -1
    ##if not winner:
    ##    if for_glory == True:
    ##        #time_alive = duration
    ##        pass
    ##    #else:v1
    ##    time_alive = input_match_attr("Time Alive: ", int)
    ## TODO: Put in additional checks here, such as ground_time + air_time can't
    ##       be more than time_alive, etc
    ##stats['time_alive'] = time_alive
    ##stats['damage_given'] = input_match_attr("Damage Given: ", int)
    ##stats['damage_taken'] = input_match_attr("Damage Taken: ", int)
    ##stats['damage_recovered'] = input_match_attr("Damage Recovered: ", int)
    ##stats['peak_damage'] = input_match_attr("Peak Damage: ", int)
    ##stats['launch_distance'] = input_match_attr("Launch Distance: ", int)
    ##stats['ground_time'] = input_match_attr("Ground Time: ", int)
    ##stats['air_time'] = input_match_attr("Air Time: ", int)
    ##stats['hit_percentage'] = input_match_attr("Hit Percentage: ", int)
    ##stats['ground_attacks'] = input_match_attr("Ground Attacks: ", int)
    ##stats['air_attacks'] = input_match_attr("Air Attacks: ", int)
    ##stats['smash_attacks'] = input_match_attr("Smash Attacks: ", int)
    ##stats['grabs'] = input_match_attr("Grabs: ", int)
    ##stats['throws'] = 0
    ##if stats['grabs'] != 0:
    ##    stats['throws'] = input_match_attr("Throws: ", int)
    ##stats['edge_grabs'] = input_match_attr("Edge Grabs: ", int)
    ##stats['projectiles'] = input_match_attr("Projectiles: ", int)
    ##stats['items_grabbed'] = input_match_attr("Items Grabbed: ", int)
    ##stats['max_launch_speed'] = input_match_attr("Max Launch Speed: ", int)
    ##stats['max_launcher_speed'] = input_match_attr("Max Launcher Speed: ", int)
    ##stats['longest_drought'] = input_match_attr("Longest Drought: ", int)
    ##stats['transformation_time'] = input_match_attr("Transformation Time: ",int)
    ## Matches with final smashes aren't worth recording

    return stats

# Enter Player
def enter_player(kos=[],sds=0,defaults=True, for_glory=True):
    # Enter Smasher
    smasher = enter_smasher(defaults)

    # Enter Fighter--only needs name, so no separate func
    fighter_name = input_match_attr("Character: ")
    fighter = Fighter(name=fighter_name)

    # Did they win?
    winner = input_match_attr("Did they win ('false' for 'no')? ", bool)

    print("Other stats:")
    stats = enter_player_stats(winner, kos, sds, for_glory)

    player_palette = input_match_attr("Palette # (0 for default): ", int)

    player = Player(smasher, fighter, winner, kos, stats, player_palette)
    return player

# Manually enter all match info via prompt
def enter_match(date_time=None, for_glory=True, defaults=True, omega=True):
    print("Enter match information:")

    # Enter KOs
    print("Assuming you're watching the replay, tell me about the KOs first")
    kos1, kos2, sds1, sds2, last_fall_time = enter_kos(for_glory)
                      
    # TODO: Parse all kinds of datetime strings, or come up with another way
    #       to enter them (optional arg?), eg Feb 2, February 2nd, 2/2
    #date = input("Date: (NOTE: This doesn't actually matter)")
    if date_time == None:
        # TODO: There's probably a cleaner way to do this...
        date_time = datetime.datetime.today()
        day = date_time.day
        month = date_time.month
        year = date_time.year
        date_time = datetime.datetime(year, month, day)

    # If we know the time of the last fall, we know how long the match lasted
    if last_fall_time != None:
        duration = last_fall_time
    else:
        duration = input_match_attr("Duration (s): ", int)

    # Enter Stage
    stage = enter_stage(for_glory)

    # Enter Players
    print("First, how did you do?")
    print("PLAYER 1 (You):")
    player1 = enter_player(kos1, sds1, defaults, for_glory)
    print("Next, how did your opponent do?")
    print("PLAYER 2 (Opponent):")
    player2 = enter_player(kos2, sds2, False, for_glory)

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
