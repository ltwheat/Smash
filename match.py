#!/usr/bin/env

from res import constants

class Match(object):
    def __init__(self, time, duration, stage, player1, player2, match_id=-1):
        self.time = time
        self.duration = duration
        self.stage = stage
        self.player1 = player1
        self.player2 = player2
        self.match_id = match_id

    # Return brief synopsis of match
    def get_synopsis():
        winner = self.get_winner()
        winner_name = winner.smasher.name
        winner_fighter = winner.fighter.name

        loser = self.get_loser()
        loser_name = loser.smasher.name
        loser_fighter = loser.fighter.name

        synopsis = "WINNER:\n------\n{0} as {1}\n".format(winner_name,
                                                          winner_fighter)
        synopsis += "\nLOSER:\n------\n{0} as {1}\n".format(loser_name,
                                                            loser_fighter)
        synopsis += "on {0}\n".format(self.stage.name)
        return synopsis

    # Return winner
    def get_winner():
        if self.player1.winner:
            return self.player1
        return self.player2

    # Return loser
    def get_loser():
        if self.player1.winner:
            return self.player2
        return self.player1
