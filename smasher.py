#!/usr/bin/env

from res import constants

smashers = constants.SMASHER_NAME_TO_ID

class Smasher(object):
    def __init__(self, name="", smasher_id=-1):
        if name == "" and smasher_id == -1:
            raise ValueError("Smasher must be instantiated with either name or id")
        if name not in smashers.keys():
            if name != "":
                raise ValueError("No smasher with name: {0}".format(name))
            name = self.get_smasher_name_for_id(smasher_id)
        if smasher_id not in smashers.values():
            if smasher_id != -1:
                raise ValueError("No smasher with id: {0}".format(smasher_id))            
            smasher_id = self.get_smasher_id_for_name(name)
        self.name = name
        self.smasher_id = smasher_id

    # Return name associated with smasher id
    def get_smasher_name_for_id(self, smasher_id):
        for name in smashers.keys():
            if smasher_id == smashers[name]:
                return name

    # Return id associated with smasher name
    def get_smasher_id_for_name(self, name):
        return smashers[name]

    # Nicer than Smasher.__dict__
    def convert_to_dict(self):
        smasher = {"name":self.name, "smasher_id":self.smasher_id}
        return smasher
