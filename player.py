#!/usr/bin/env

import traceback

# The Player object represents the actual performance of one Smasher
# in a given match. Thus, a player has ("is", at its core) a Smasher,
# represented in the Match by a Fighter, a boolean to determine whether
# it was victorious, and a dict of stats for that match.
class Player(object):
    def __init__(self, smasher, fighter, winner, stats):
        # winner being something other than a boolean can cause trouble down the road
        if type(winner) != bool:
            raise TypeError("winner must be a boolean!")
        self.smasher = smasher
        self.fighter = fighter
        self.winner = winner
        # Populate match statistics
        try:
            self.kos = stats['KOs']
            self.falls = stats['falls']
            self.sds = stats['SDs']
            self.time_alive = stats['time_alive']
            self.damage_given = stats['damage_given']
            self.damage_taken = stats['damage_taken']
            self.damage_recovered = stats['damage_recovered']
            self.peak_damage = stats['peak_damage']
            self.launch_distance = stats['launch_distance']
            self.ground_time = stats['ground_time']
            self.air_time = stats['air_time']
            self.hit_percentage = stats['hit_percentage']
            self.ground_attacks = stats['ground_attacks']
            self.air_attacks = stats['air_attacks']
            self.smash_attacks = stats['smash_attacks']
            self.grabs = stats['grabs']
            self.throws = stats['throws']
            self.edge_grabs = stats['edge_grabs']
            self.projectiles = stats['projectiles']
            self.items_grabbed = stats['items_grabbed']
            self.max_launch_speed = stats['max_launch_speed']
            self.max_launcher_speed = stats['max_launcher_speed']
            self.longest_drought = stats['longest_drought']
            self.transformation_time = stats['transformation_time']
            self.final_smashes = stats['final_smashes']
        except KeyError:
            print("Expected an item not contained in stats:")
            print(traceback.print_exc())
