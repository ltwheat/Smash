#!/usr/bin/env

from res import constants

directions = constants.DIRECTIONS
moves = constants.MOVES

# Represents a KO on one player. For now, only applies to 1v1
# move: the move, described by uair, bthrow, dspecial, jab, etc
# damage: the % damage the victim was at when they were knocked out
# direction: which side of the screen the victim was knocked out of
# time: number of seconds into the match the victim was KO'd
class KO(object):
    ## TODO: Attributes to add in the future:
    ##      -sweetspot boolean?
    ##      -charge attribute, for smashes or certain specials?
    ##      -rage (over 100%)?
    ##      -Shield break deaths (Jiggs, shield break on edge of stage -> fall)?
    ##      -Stage spike boolean?
    def __init__(self, move, damage, direction, time):
        # Instantiation checks
        if move not in moves:
            print("move must be one of the following:")
            print(moves)
            raise ValueError
        if direction not in directions:
            print("direction must be one of the following:")
            print(directions)
            raise ValueError
        if type(damage) != int:
            raise TypeError("damage must be an integer")
        if type(time) != int:
            raise TypeError("time must be an integer (how many seconds into" +
                            "the match?)")
        
        self.move = move
        self.damage = damage
        self.direction = direction
        self.time = time

    # Nicer than KO.__dict__
    def convert_to_dict(self):
        ko = {"move":self.move, "damage":self.damage,
              "direction":self.direction, "time":self.time}
        return ko
