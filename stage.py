#!/usr/bin/env

from res import constants

stages = constants.STAGE_NAME_TO_ID

class Stage(object):
    def __init__(self, name="", stage_id=-1, omega=False):
        if name == "" and stage_id == -1:
            raise ValueError("Stage must be instantiated with either name or id")
        if name not in stages.keys():
            if name != "":
                raise ValueError("No stage with name: {0}".format(name))
            name = self.get_stage_name_for_id(stage_id)
        if stage_id not in stages.values():
            if stage_id != -1:
                raise ValueError("No stage with id: {0}".format(stage_id))            
            stage_id = self.get_stage_id_for_name(name)
        # TODO: Omega should be part of the display name, but not the actual
        #       attribute. Come back to this when it's needed (different method?)
        #if omega == True:
        #    name += " (Omega)"
        self.name = name
        self.id = stage_id
        self.omega = omega

    # Return name associated with stage id
    def get_stage_name_for_id(self, stage_id):
        for name in stages.keys():
            if stage_id == stages[name]:
                return name

    # Return id associated with stage name
    def get_stage_id_for_name(self, name):
        return stages[name]
