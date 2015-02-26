#!/usr/bin/env

from common_mongo import smash_conn
from Smash.res import constants

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
        # TODO: If mii_name is passed in WITH existing tag or id, we should
        #       update the smasher's mii name in the coll
        store = False
        # TODO: This is too long, make it a separate method
        # Instantiation checks
        if mii_name == "" and tag == "" and smasher_id == -1:
            raise ValueError("Smasher must be instantiated with Mii name, " +
                             "tag, or id")
        elif tag != "" or smasher_id != -1:
            # A tag or id was passed in, so this Smasher is important enough to
            # store
            if tag == '':
                smasher_ids = self.get_all_smasher_ids()
                if smasher_id not in smasher_ids:
                    raise ValueError("Can't instantiate Smasher with only id" +
                                     " and no tag")
                else:
                    # Smasher with this id exists, use it
                    # TODO: Make this a separate method
                    smasher = smash_conn.get_smasher({'smasher_id':smasher_id})
                    mii_name = smasher['mii_name']
                    tag = smasher['tag']
                    smasher_id = smasher['smasher_id']
            elif smasher_id == -1:
                smasher_tags = self.get_all_smasher_tags()
                if tag in smasher_tags:
                    # Smasher with this tag exists, use it
                    smasher = smash_conn.get_smasher({'tag':tag})
                    mii_name = smasher['mii_name']
                    tag = smasher['tag']
                    smasher_id = smasher['smasher_id']
                else:
                    smasher_id = max(self.get_all_smasher_ids()) + 1
                    store = True
            else:
                smasher = smash_conn.get_smasher({'smasher_id':smasher_id})
                if smasher != None:
                    if smasher['tag'] != tag:
                        raise ValueError("Found existing Smasher with id " +
                                     "{0} but different ".format(smasher_id) +
                                     "tags: {0} v {1}".format(tag,
                                                              smasher['tag']))
                    else:
                        # Smasher with this tag and id exists, use it
                        mii_name = smasher['mii_name']
                        tag = smasher['tag']
                        smasher_id = smasher['smasher_id']
                else:
                    # No matching IDs, so this Smasher probably doesn't exist,
                    # but check for duplicate tags
                    if tag not in self.get_all_smasher_tags():
                        store = True
                    else:
                        raise ValueError("Smasher with tag {0} ".format(tag) +
                                         "already exists in the collection")

        # Set attributes
        self.mii_name = mii_name
        self.tag = tag
        self.smasher_id = smasher_id

        # Store the Smasher, if we've already determined it doesn't exist
        # in the collection
        if store:
            smash_conn.store_smasher(self)

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

    ### Do the methods that interact with mongo belong elsewhere? ###

    # Get the specified attribute for all Smashers
    def get_all_smasher_attr(self, attr):
        attrs = []
        smashers = smash_conn.get_all_smashers()
        for smasher in smashers:
            smasher_attr = smasher[attr]
            if smasher_attr in attrs:
                raise Exception("Uh oh! Two Smashers have the same " +
                                "{0}".format(attr))
            attrs.append(smasher_attr)
        return attrs

    # Get all Smasher tags
    def get_all_smasher_tags(self):
        return self.get_all_smasher_attr('tag')

    # Get all Smasher Mii Names
    def get_all_smasher_mii_names(self):
        return self.get_all_smasher_attr('mii_name')

    # Get all Smasher ids
    def get_all_smasher_ids(self):
        return self.get_all_smasher_attr('smasher_id')
