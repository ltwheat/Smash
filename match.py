#!/usr/bin/env

from res import constants

# TODO: Need some globally intelligent way of assigning id
class Match(object):
    def __init__(self, time, duration, stage, player1, player2):
        self.time = time
        self.duration = duration
        self.stage = stage
        self.player1 = player1
        self.player2 = player2
