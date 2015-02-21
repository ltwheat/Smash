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
        self.stats = {}
        # TODO: This segment should be a lot simpler, and the required stats
        #       should be in some config or something instead of hard-coded
        #       here
        try:
            self.stats['KOs'] = stats['KOs']
            self.stats['falls'] = stats['falls']
            self.stats['SDs'] = stats['SDs']
            self.stats['time_alive'] = stats['time_alive']
            self.stats['damage_given'] = stats['damage_given']
            self.stats['damage_taken'] = stats['damage_taken']
            self.stats['damage_recovered'] = stats['damage_recovered']
            self.stats['peak_damage'] = stats['peak_damage']
            self.stats['launch_distance'] = stats['launch_distance']
            self.stats['ground_time'] = stats['ground_time']
            self.stats['air_time'] = stats['air_time']
            self.stats['hit_percentage'] = stats['hit_percentage']
            self.stats['ground_attacks'] = stats['ground_attacks']
            self.stats['air_attacks'] = stats['air_attacks']
            self.stats['smash_attacks'] = stats['smash_attacks']
            self.stats['grabs'] = stats['grabs']
            self.stats['throws'] = stats['throws']
            self.stats['edge_grabs'] = stats['edge_grabs']
            self.stats['projectiles'] = stats['projectiles']
            self.stats['items_grabbed'] = stats['items_grabbed']
            self.stats['max_launch_speed'] = stats['max_launch_speed']
            self.stats['max_launcher_speed'] = stats['max_launcher_speed']
            self.stats['longest_drought'] = stats['longest_drought']
            self.stats['transformation_time'] = stats['transformation_time']
            self.stats['final_smashes'] = stats['final_smashes']
        except KeyError:
            print("Expected an item not contained in stats:")
            print(traceback.print_exc())

    # Nicer than Player.__dict__
    def convert_to_dict():
        player = {"smasher":self.smasher.convert_to_dict(),
                  "fighter":self.fighter.convert_to_dict(),
                  "winner":self.winner, "stats":self.stats}
