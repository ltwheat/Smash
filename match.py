#!/usr/bin/env

import datetime

class Match(object):
    def __init__(self, date, duration, stage, player1, player2, time_limit=300):
        if type(date) != datetime.datetime:
            raise TypeError("date must be datetime.datetime object")
        if type(duration) != int:
            raise TypeError("duration must be int")
        if type(time_limit) != int:
            raise TypeError("time_limit must be int")

        self.date = date
        self.duration = duration
        self.stage = stage
        self.player1 = player1
        self.player2 = player2
        # TODO: Move match_id assignment over from smash_conn.store_match()
        self.match_id = -1
        self.time_limit = time_limit

    # Return brief synopsis of match
    def get_synopsis(self):
        # Get winner and their character
        winner = self.get_winner()
        winner_tag = winner.smasher.tag
        if winner_tag == "":
            winner_tag = winner.smasher.mii_name
        winner_fighter = winner.fighter.name

        # Get loser and their character
        loser = self.get_loser()
        loser_tag = loser.smasher.tag
        if loser_tag == "":
            loser_tag = loser.smasher.mii_name
        loser_fighter = loser.fighter.name

        # Generate (formatted)  synopsis
        synopsis = "\n{0}\n".format(self.date)
        synopsis += "WINNER:\n------\n{0} as {1}\n".format(winner_tag,
                                                          winner_fighter)
        synopsis += "\nLOSER:\n------\n{0} as {1}\n".format(loser_tag,
                                                            loser_fighter)
        synopsis += "\non {0}".format(self.stage.name)
        if self.stage.omega == True:
            synopsis += " (Omega)"
        synopsis += "\n"
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
