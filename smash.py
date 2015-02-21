#!/usr/bin/env

import datetime
import pymongo

from fighter import Fighter
from ko import KO
from match import Match
from player import Player
from smasher import Smasher
from stage import Stage

# TODO: Write a script that makes it easier to enter all this info.
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

# TODO: convert b/w objects and docs
dt = datetime.datetime.now()
dur = 60
lylat = Stage(name="Lylat Cruise")
smasher_lt = Smasher(name="Lt Wheat")
luigi = Fighter(name="Luigi")
mario = Fighter(name="Mario")
kos1 = [KO("uspecial",101,"up"), KO("fsmash",120,"right")]
kos2 = [KO("dsmash",143,"left")]
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


match_test={"date": datetime.datetime(2014, 11, 21), "duration": 186,
       "stage": "Gaur Plains", "player1": player1, "player2": player2}

#smash_db_name = "smash_wii_u"
smash_db_name = "test_db"
fg_coll_name = "for_glory"
### Mongodb notes ###
#   1) Connection/Client -> Database -> Collection
#      b) client=pymongo.MongoClient()
#         db=pymongo.database.Database(client, "db_name")
#         db.coll_name.insert({"sample":"dict"})
#      b) client=pymongo.MongoClient()
#         db=client['db_name']
#         coll=db['coll_name']
#         coll.insert({"sample":"dict"})
#   2) Collection won't actually exist until data is inserted
#   3) Commonly used gets:
#      a) coll/conn.database_names()# returns all db names
#      b) db.collection_names()# returns all collection names in db
#      c) coll.find_one()# returns (random?) single item from coll
#      d) list(coll.find())# returns everything in coll. Must be cast
def store_match(match):
    try:
        client = pymongo.MongoClient()
        # Automatically connects or creates if nonexistent
        db = client[smash_db_name]
        coll = db[fg_coll_name]
        # TODO: This check loops through every match in the db but I feel like
        #       that probably won't scale? Should we keep a separate coll of
        #       just match ids?
        match_id = coll.find().count()
        for db_match in list(coll.find()):
            if match_id == db_match['match_id']:
                err_msg = "Match with id {0} already found in " \
                           "collection".format(match_id)
                raise pymongo.errors.DuplicateKeyError(err_msg)
        db_match_id = coll.insert(match)
        print("Stored match of id {0}:".format(match_id))
    except pymongo.errors.ConnectionFailure:
        print("Could not connect to database")
    except pymongo.errors.DuplicateKeyError as dke:
        print(dke)
        
def enter_match(defaults=True, omega=True):
    # TODO: Need type checking for all of this
    print("Enter match information:")
    # TODO: Parse all kinds of datetime strings, or come up with another way
    #       to enter them (optional arg?), eg Feb 2, February 2nd, 2/2
    date = input("Date: ")
    date_time = datetime.datetime(2015, 2, 19, 21, 30)
    duration = int(input("Duration (s): "))

    # TODO: Make this a separate function
    stage_name = input("Stage: ")
    if not defaults == True:
        omega = bool(input(" (Omega?) "))#TODO: bool casting doesn't work on strings lol
    stage = Stage(name=stage_name, omega=omega)
    print("First, how did you do?")

    # TODO: Make this a separate function
    print("PLAYER 1 (You):")
    smasher1_name = "Lt Wheat"
    if not defaults == True:
        smasher1_name = input("Name: ")
    smasher1 = Smasher(name=smasher1_name)
    
    fighter1_name = input("Character: ")
    fighter1 = Fighter(name=fighter1_name)
    
    winner1 = bool(input("Did they win (empty string for no)"))
    stats1 = {}

    kos1 = []
    num_kos1 = int(input("How many KOs did you get? "))
    print("Tell me about those.")
    for num in range(num_kos1):
        print("KO {0}:".format(num + 1))
        ko_move = input("Move? ")
        ko_dmg = int(input("% Damage? "))
        ko_side = input("Off of which side of the screen? ")
        ko = KO(ko_move, ko_dmg, ko_side)
        kos1.append(ko)

    print("Other stats:")
    stats1['falls'] = int(input("Falls: "))
    stats1['SDs'] = int(input("SDs (Remember this is special): "))
    stats1['time_alive'] = int(input("Time Alive: "))
    stats1['damage_given'] = int(input("Damage Given: "))
    stats1['damage_taken'] = int(input("Damage Taken: "))
    stats1['damage_recovered'] = int(input("Damage Recovered: "))
    stats1['peak_damage'] = int(input("Peak Damage: "))
    stats1['launch_distance'] = int(input("Launch Distance: "))
    stats1['ground_time'] = int(input("Ground Time: "))
    stats1['air_time'] = int(input("Air Time: "))
    stats1['hit_percentage'] = int(input("Hit Percentage: "))
    stats1['ground_attacks'] = int(input("Ground Attacks: "))
    stats1['air_attacks'] = int(input("Air Attacks: "))
    stats1['smash_attacks'] = int(input("Smash Attacks: "))
    stats1['grabs'] = int(input("Grabs: "))
    stats1['throws'] = int(input("Throws: "))
    stats1['edge_grabs'] = int(input("Edge Grabs: "))
    stats1['projectiles'] = int(input("Projectiles: "))
    stats1['items_grabbed'] = int(input("Items Grabbed: "))
    stats1['max_launch_speed'] = int(input("Max Launch Speed: "))
    stats1['max_launcher_speed'] = int(input("Max Launcher Speed: "))
    stats1['longest_drought'] = int(input("Longest Drought: "))
    stats1['transformation_time'] = int(input("Transformation Time: "))
    stats1['final_smashes'] = int(input("Final Smashes: "))
    
    player1_palette = 0
    if not defaults == True:
        player1_palette = int(input("Palette #: "))

    player1 = Player(smasher1, fighter1, winner1, kos1, stats1,
                     player1_palette)
    # TODO: Make this a separate function
    print("PLAYER 2 (Opponent):")
    smasher2_name = input("Name: ")
    smasher2 = Smasher(name=smasher1_name)
    
    fighter2_name = input("Character: ")
    fighter2 = Fighter(name=fighter2_name)
    
    winner2 = not winner1

    kos2 = []
    num_kos2 = int(input("How many KOs did they get? "))
    print("Tell me about those.")
    for num in range(num_kos2):
        print("KO {0}:".format(num + 1))
        ko_move = input("Move? ")
        ko_dmg = int(input("% Damage? "))
        ko_side = input("Off of which side of the screen? ")
        ko = KO(ko_move, ko_dmg, ko_side)
        kos2.append(ko)
    
    stats2 = {}
    stats2['falls'] = int(input("Falls: "))
    stats2['SDs'] = int(input("SDs (Remember this is special): "))
    stats2['time_alive'] = int(input("Time Alive: "))
    stats2['damage_given'] = int(input("Damage Given: "))
    stats2['damage_taken'] = int(input("Damage Taken: "))
    stats2['damage_recovered'] = int(input("Damage Recovered: "))
    stats2['peak_damage'] = int(input("Peak Damage: "))
    stats2['launch_distance'] = int(input("Launch Distance: "))
    stats2['ground_time'] = int(input("Ground Time: "))
    stats2['air_time'] = int(input("Air Time: "))
    stats2['hit_percentage'] = int(input("Hit Percentage: "))
    stats2['ground_attacks'] = int(input("Ground Attacks: "))
    stats2['air_attacks'] = int(input("Air Attacks: "))
    stats2['smash_attacks'] = int(input("Smash Attacks: "))
    stats2['grabs'] = int(input("Grabs: "))
    stats2['throws'] = int(input("Throws: "))
    stats2['edge_grabs'] = int(input("Edge Grabs: "))
    stats2['projectiles'] = int(input("Projectiles: "))
    stats2['items_grabbed'] = int(input("Items Grabbed: "))
    stats2['max_launch_speed'] = int(input("Max Launch Speed: "))
    stats2['max_launcher_speed'] = int(input("Max Launcher Speed: "))
    stats2['longest_drought'] = int(input("Longest Drought: "))
    stats2['transformation_time'] = int(input("Transformation Time: "))
    stats2['final_smashes'] = int(input("Final Smashes: "))
    
    player2_palette = 0
    if not defaults == True:
        player2_palette = int(input("Palette #: "))

    player2 = Player(smasher2, fighter2, winner2, kos2, stats2,
                     player2_palette)


    match = Match(date_time, duration, stage, player1, player2)
    store_match(match.convert_to_dict())
    print(match.get_synopsis())

def enter_test_match():
    match = Match(dt, dur, lylat, player1, player2)
    store_match(match.convert_to_dict())
    print(match.get_synopsis())

if __name__ == "__main__":
    enter_match()
