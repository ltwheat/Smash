#!/usr/bin/env

import traceback

# The Player object represents the actual performance of one Smasher
# in a given match. Thus, a player has ("is", at its core) a Smasher,
# represented in the Match by a Fighter (using the palette swap determined
# by 'palette'), a boolean to determine whether it was victorious, a list of its
# KOs, and the number of falls and SDs it suffered.
class Player(object):
    def __init__(self, smasher, fighter, winner, kos, falls, sds, palette=0):
        # Type-checks
        if type(winner) != bool:
            raise TypeError("winner must be a boolean!")
        if type(kos) != list:
            raise TypeError("kos must be a list")
        if type(falls) != int:
            raise TypeError("falls must be an int")
        if type(sds) != int:
            raise TypeError("sds must be an int")

        # Logic checks
        if sds > falls:
            raise ValueError("Can't have more SDs than Falls")

        self.smasher = smasher
        self.fighter = fighter
        self.winner = winner
        self.kos = kos
        self.falls = falls
        self.sds = sds

        max_palette_id = 7
        # Little Mac has 16 palette swaps
        if self.fighter.name == "Little Mac":
            max_palette_id = 15
        if 0 > palette > max_palette_id:
            raise ValueError("Invalid palette id {0}: ".format(palette) +
                             "palette id must be between 0 and " +
                             "{0} (inclusive)".format(max_palette_id))
        self.palette = palette

        # Populate match statistics
        #self.stats = {}
        #try:
            #========= CAN'T PUT IN MATCH CUZ REPLAYS SUCK =======#
            ##self.stats['time_alive'] = stats['time_alive']
            ##self.stats['damage_given'] = stats['damage_given']
            ##self.stats['damage_taken'] = stats['damage_taken']
            ##self.stats['damage_recovered'] = stats['damage_recovered']
            ##self.stats['peak_damage'] = stats['peak_damage']
            ##self.stats['launch_distance'] = stats['launch_distance']
            ##self.stats['ground_time'] = stats['ground_time']
            ##self.stats['air_time'] = stats['air_time']
            ##self.stats['hit_percentage'] = stats['hit_percentage']
            ##self.stats['ground_attacks'] = stats['ground_attacks']
            ##self.stats['air_attacks'] = stats['air_attacks']
            ##self.stats['smash_attacks'] = stats['smash_attacks']
            ##self.stats['grabs'] = stats['grabs']
            ##self.stats['throws'] = stats['throws']
            ##self.stats['edge_grabs'] = stats['edge_grabs']
            ##self.stats['projectiles'] = stats['projectiles']
            ##self.stats['items_grabbed'] = stats['items_grabbed']
            ##self.stats['max_launch_speed'] = stats['max_launch_speed']
            ##self.stats['max_launcher_speed'] = stats['max_launcher_speed']
            ##self.stats['longest_drought'] = stats['longest_drought']
            ##self.stats['transformation_time'] = stats['transformation_time']
            ##self.stats['final_smashes'] = stats['final_smashes']
        #except KeyError:
        #    print("Expected an item not contained in stats:")
        #    print(traceback.print_exc())

    # Nicer than Player.__dict__
    def convert_to_dict(self):
        # Convert KOs first
        kos = []
        for ko in self.kos:
            kos.append(ko.convert_to_dict())

        player = {"smasher":self.smasher.convert_to_dict(),
                  "fighter":self.fighter.convert_to_dict(),
                  "palette":self.palette, "kos":kos, "falls": self.falls,
                  "sds": self.sds, "winner":self.winner}
        return player
