#!/usr/bin/env

from res import constants

class Match(object):
    def __init__(self, date, duration, stage, player1, player2, match_id=-1):
        # TODO: 3DS only records date not time--is WiiU different? If not,
        #       should we come up with a way of recording time or is date
        #       sufficient?
        self.date = date
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

        synopsis = "{0}\n".format(self.date)
        synopsis += "WINNER:\n------\n{0} as {1}\n".format(winner_name,
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

    # Nicer than match.__dict__
    def convert_to_dict():
        match = {"date":self.date, "duration":self.duration,
                 "stage":self.stage.convert_to_dict,
                 "player1":self.player1.convert_to_dict(),
                 "player2":self.player2.convert_to_dict(),
                 "match_id":self.match_id}
        return match
