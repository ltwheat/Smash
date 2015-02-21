#!/usr/bin/env

# TODO: Move to a config of some sort
# TODO: Add variants and a standardizer, so for instance, accept 'downb' as
#       well as 'dspecial', but still store as 'dspecial'. Same thing with
#       direction, e.g. 'top' -> 'up'
moves = ["jab", "ftilt", "dash", "fsmash", "dtilt", "dsmash", "utilt",
         "usmash", 'nspecial', 'sspecial', 'dspecial', 'uspecial', 'fthrow',
         'bthrow', 'dthrow', 'uthrow', 'nair', 'fair', 'bair', 'dair', 'uair']
directions = ['right', 'left', 'up', 'down']

# Represents a KO on one player. For now, only applies to 1v1
# move: the move, described by uair, bthrow, dspecial, jab, etc
# damage: the % damage the victim was add when they were knocked out
# direction: which side of the screen the victim was knocked out of
class KO(object):
    # TODO: What about a sweetspot boolean?
    def __init__(self, move, damage, direction):
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
        
        self.move = move
        self.damage = damage
        self.direction = direction

    # Nicer than KO.__dict__
    def convert_to_dict(self):
        ko = {"move":self.move, "damage":self.damage,
              "direction":self.direction}
        return ko
