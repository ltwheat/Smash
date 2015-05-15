#!/usr/bin/env

from res import constants

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

        self.smasher = smasher
        self.fighter = fighter
        self.winner = winner
        self.kos = kos
        self.falls = falls
        self.sds = sds

        # Most fighters have 8 palette swaps--the ones who don't are listed
        # in res.constants
        max_palette_id = 7
        fighter_to_num_palettes_dict = constants.FIGHTER_NAME_TO_NUM_PALETTES
        if self.fighter.name in fighter_to_num_palettes_dict:
            max_palette_id = fighter_to_num_palettes_dict[self.fighter.name] - 1
        if 0 > palette > max_palette_id:
            raise ValueError("Invalid palette id {0}: ".format(palette) +
                             "palette id must be between 0 and " +
                             "{0} (inclusive)".format(max_palette_id))
        self.palette = palette

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
