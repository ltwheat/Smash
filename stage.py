#!/usr/bin/env

import string

from res import constants

stages = constants.STAGE_NAME_TO_ID

class Stage(object):
    def __init__(self, name="", stage_id=-1, omega=False):
        # Correctly format the stage name
        cap_name = self.stage_title(name)

        # Type/value checks
        if name == "" and stage_id == -1:
            raise ValueError("Stage must be instantiated with either name or id")
        if cap_name not in stages.keys():
            if name != "":
                raise ValueError("No stage with name: {0}".format(cap_name))
            name = self.get_stage_name_for_id(stage_id)
        if stage_id not in stages.values():
            if stage_id != -1:
                raise ValueError("No stage with id: {0}".format(stage_id))            
            stage_id = self.get_stage_id_for_name(cap_name)
        if type(omega) != bool:
            raise TypeError("omega must be a boolean")

        # Set attributes
        self.name = cap_name
        self.stage_id = stage_id
        self.omega = omega

    # Convert the input name to the correctly formatted stage name. There is
    # no universal Python string manipulation method to account for all the
    # variants of Smash 4's punctuation in stage names. .title() works for all
    # stages except ones with apostrophes and either of the PAC stages.
    def stage_title(self, name):
        title = name.title()
        # .title() will always capitalize the letter after an apostrophe, so
        # undo that change
        if "'" in title:
            title = self.apostrophize_title(title)
        # The PAC stages are in all caps
        if "pac" in title.lower():
            title = title.upper()
        return title

    # TODO: This needs to be in a utility file/method
    # Correctly capitalize stage names with apostrophes
    def apostrophize_title(self, title):
        split_title = title.split("'")
        new_title = split_title[0]
        for segment in split_title[1:]:
            # Stick the apostrophe back in, along with the lowercased
            # subsequent letter and then the rest of the string
            new_title += "'{0}{1}".format(segment[0].lower(), segment[1:])
        return new_title

    # Adds the Omega to the name, if appropriate
    def get_name(self):
        if self.omega:
            return "{0} (Omega)".format(self.name)
        return self.name

    # Return name associated with stage id
    def get_stage_name_for_id(self, stage_id):
        for name in stages.keys():
            if stage_id == stages[name]:
                return name

    # Return id associated with stage name
    def get_stage_id_for_name(self, name):
        return stages[name]

    # Nicer than Stage.__dict__
    def convert_to_dict(self):
        stage = {"name":self.name, "stage_id":self.stage_id,
                 "omega":self.omega}
        return stage
