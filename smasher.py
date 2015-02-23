#!/usr/bin/env

from res import constants

# TODO: There needs to be a distinction b/w tag and Nintendo Network name,
#       e.g. "Lt Wheat" v "Mr. Wheat", since the latter is what shows up on
#       the FG match results screen and is the only thing I know--no way to
#       tell the other. Maybe Smasher can be instantiated with either?
# TODO: Need to think about relationship b/w mii name, tag and id, which are
#       necessary when, which need to be recorded with which in constants, etc
# TODO: For now, mii_name is just an additional (unnecessary) argument. Its
#       inclusion doesn't matter, as long as name is changed to tag now.
smashers = constants.SMASHER_NAME_TO_ID

class Smasher(object):
    def __init__(self, mii_name="", tag="", smasher_id=-1):
        # Instantiation checks
        if mii_name == "" and tag == "" and smasher_id == -1:
            raise ValueError("Smasher must be instantiated with Mii name, " +
                             "tag, or id")
        if tag not in smashers.keys():
            if tag != "":
                raise ValueError("No smasher with tag: {0}".format(tag))
            tag = self.get_smasher_tag_for_id(smasher_id)
        if smasher_id not in smashers.values():
            if smasher_id != -1:
                raise ValueError("No smasher with id: {0}".format(smasher_id))            
            smasher_id = self.get_smasher_id_for_tag(tag)

        # Set attributes
        self.mii_name = mii_name
        self.tag = tag
        self.smasher_id = smasher_id

    # Return name associated with smasher id
    def get_smasher_tag_for_id(self, smasher_id):
        for tag in smashers.keys():
            if smasher_id == smashers[tag]:
                return tag

    # Return id associated with smasher tag
    def get_smasher_id_for_tag(self, tag):
        return smashers[tag]

    # Nicer than Smasher.__dict__
    def convert_to_dict(self):
        smasher = {"mii_name":self.mii_name, "tag":self.tag,
                   "smasher_id":self.smasher_id}
        return smasher
