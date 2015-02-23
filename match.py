#!/usr/bin/env

from res import constants

class Match(object):
    def __init__(self, date, duration, stage, player1, player2, time_limit=300):
        # TODO: Type checks
        self.date = date
        self.duration = duration
        self.stage = stage
        self.player1 = player1
        self.player2 = player2
        self.match_id = -1
        self.time_limit = time_limit

    # Return brief synopsis of match
    # TODO: Make this prettier
    def get_synopsis(self):
        winner = self.get_winner()
        winner_name = winner.smasher.name
        winner_fighter = winner.fighter.name

        loser = self.get_loser()
        loser_name = loser.smasher.name
        loser_fighter = loser.fighter.name

        synopsis = "{0}\n".format(self.date)
        synopsis += "WINNER:\n------\n{0} as {1}\n".format(winner_name,
                                                          winner_fighter)
        synopsis += "\nLOSER:\n------\n{0} as {1}\n".format(loser_name,
                                                            loser_fighter)
        synopsis += "on {0}\n".format(self.stage.name)
        return synopsis

    # Return winner
    def get_winner(self):
        if self.player1.winner:
            return self.player1
        return self.player2

    # Return loser
    def get_loser(self):
        if self.player1.winner:
            return self.player2
        return self.player1

    # Nicer than match.__dict__
    def convert_to_dict(self):
        match = {"date":self.date, "duration":self.duration,
                 "stage":self.stage.convert_to_dict(),
                 "player1":self.player1.convert_to_dict(),
                 "player2":self.player2.convert_to_dict(),
                 "match_id":self.match_id, "time_limit":self.time_limit}
        return match
