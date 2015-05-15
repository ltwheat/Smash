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

from conf import config
from res import constants

##### TODOS #####
# 1) Long-term: Handle team matches



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

    try:
        val = attr_type(val)
    except ValueError:
        print("Could not cast {0} as type {1}".format(val, attr_type))
    return val

# Convert match clock time to elapsed time
def convert_match_time_to_elapsed_time(match_clock, for_glory=True):
    time_limit = config.FOR_GLORY_TIME_LIMIT
    if for_glory != True:
        time_limit = input_match_attr("What was the match time limit (s)? ",
                                      int)
    clock_units = match_clock.split(":")
    minutes = int(clock_units[0])
    seconds = int(clock_units[1])
    time_elapsed = time_limit - (minutes*60) - seconds
    return time_elapsed

# Enter a single KO
def enter_ko(for_glory=True):
    # The checks on moves and directions performed here are also performed in
    # the instantiation of the KO itself, however I've copied them here so
    # that the script will throw an error at the first sign of bad data
    # rather than making the user input all three KO attrs and then throwing
    # an error. This won't be necessary with a UI.
    ko_move = input_match_attr("Move? ")
    if ko_move not in constants.MOVES:
        print("move must be one of the following:")
        print(constants.MOVES)
        raise ValueError
    ko_dmg = input_match_attr("% Damage? ", int)
    ko_side = input_match_attr("Off of which side of the screen? ")
    if ko_side not in constants.DIRECTIONS:
        print("direction must be one of the following:")
        print(constants.DIRECTIONS)
        raise ValueError
    ko_clock_time = input_match_attr("What was the clock time " +
                                     "(to the nearest second)? ")

    ko_time = convert_match_time_to_elapsed_time(ko_clock_time, for_glory)
    ko = KO(ko_move, ko_dmg, ko_side, ko_time)
    return ko
    #print("KO: {0}".format(ko.convert_to_dict()))

# Enter all kos for the match
def enter_kos(for_glory=True):
    max_player_kos = config.FOR_GLORY_MAX_PLAYER_KOS
    if for_glory == False:
        max_player_kos = input_match_attr("How many stock? ", int)

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
            ko = enter_ko(for_glory)
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
    stats = {}
    max_player_kos = config.FOR_GLORY_MAX_KOS
    if for_glory == False:
        max_player_kos = input_match_attr("How many stock? ")
    stats['falls'] = max_player_kos - sds
    if winner == True:
        stats['falls'] = input_match_attr("Falls: ", int)
    stats['SDs'] = sds

    return stats

# Enter Player
def enter_player(kos=[], falls=0, sds=0, winner = False, defaults=True):
    # Enter Smasher
    smasher = enter_smasher(defaults)

    # Enter Fighter--only needs name, so no separate func
    fighter_name = input_match_attr("Character: ")
    fighter = Fighter(name=fighter_name)

    # Which palette swap did they use?
    player_palette = input_match_attr("Palette # (0 for default): ", int)

    player = Player(smasher, fighter, winner, kos, falls, sds, player_palette)
    return player

# Manually enter all match info via prompt
def enter_match(date=None, for_glory=True, defaults=True):
    print("Enter match information:")

    # Enter KOs
    print("Assuming you're watching the replay, tell me about the KOs first")
    kos1, kos2, sds1, sds2, last_fall_time = enter_kos(for_glory)
    falls1 = len(kos2)
    falls2 = len(kos1)

    # We know who the winner is based on who died fewer times
    winner1 = False
    winner2 = False
    if (falls1 + sds1) > (falls2 + sds2):
        winner2 = True
    else:
        winner1 = True
                      
    if date == None:
        # TODO: Convert all datetime objects into dates, since Smash replays
        #       only record with day granularity
        date = datetime.date.today()
        # ^^^ Then you can delete the following 4 lines
        day = date.day
        month = date.month
        year = date.year
        date = datetime.datetime(year, month, day)

    # If we know the time of the last fall, we know how long the match lasted
    if last_fall_time != -1:
        duration = last_fall_time
    else:
        duration = input_match_attr("Duration (s): ", int)

    # Enter Stage
    stage = enter_stage(for_glory)

    # Enter Players
    print("PLAYER 1 (You):")
    player1 = enter_player(kos1, falls1, sds1, winner1, defaults)
    print("PLAYER 2 (Opponent):")
    #print("Who did they play as?")
    player2 = enter_player(kos2, falls2, sds2, winner2, False)

    match = Match(date, duration, stage, player1, player2)
    smash_conn.store_match(match.convert_to_dict())
    print(match.get_synopsis())


if __name__ == "__main__":
    #enter_match()
    pass
