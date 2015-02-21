#!/usr/bin/env

from res import constants

fighters = constants.FIGHTER_NAME_TO_ID

class Fighter(object):
    def __init__(self, name="", fighter_id=-1):
        # Instantiation conditions
        if name == "" and fighter_id == -1:
            raise ValueError("Fighter must be instantiated with either name " +
                             "or id")
        if name not in fighters.keys():
            if name != "":
                raise ValueError("No fighter with name: {0}".format(name))
            name = self.get_fighter_name_for_id(fighter_id)
        if fighter_id not in fighters.values():
            if fighter_id != -1:
                raise ValueError("No fighter with id: {0}".format(fighter_id))            
            fighter_id = self.get_fighter_id_for_name(name)

        # Set attributes
        self.name = name
        self.id = fighter_id

    # Return name associated with fighter id
    def get_fighter_name_for_id(self, fighter_id):
        for name in fighters.keys():
            if fighter_id == fighters[name]:
                return name

    # Return id associated with fighter name
    def get_fighter_id_for_name(self, name):
        return fighters[name]

    # Nicer than Figher.__dict__
    def convert_to_dict():
        fighter = {"name":self.name, "fighter_id":self.fighter_id}
        return fighter
