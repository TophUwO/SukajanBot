######################################################################
# Project:    Sukajan Bot v0.1                                       #
# File Name:  init.py                                                #
# Author:     Sukajan One-Trick <tophuwo01@gmail.com>                #
# Description:                                                       #
#   a bot for the KirikoMains subreddit for advanced custom          #
#   features required by the moderation team                         #
#                                                                    #
# (C) 2023 Sukajan One-Trick. All rights reserved.                   #
######################################################################

# This file implements the init module, managing configuration resources
# and constants.

# imports
import dotenv
import logging


# This class holds all configuration options the bot supports alongside
# bot-wide constants.
class SukajanConfig(object):
    def __init__(self):
        self._object = {}

        # Load config file.
        if not self.readconfig():
            raise Exception(f'Failed to read config file ".env".')


    # Retrieves a value from the internal settings object. If the key
    # does not exist, return '*fallback*.
    #
    # Returns value associated with *key*, otherwise *fallback*.
    def getvalue(self, key: str, fallback: any) -> any:
        return self._object.get(key, fallback)

    
    # Updates the configuration of the given *key* with *value*.
    # If the key does not exist, create a new one. If the key did
    # not exist previously, the function returns None.
    #
    # Returns old value.
    def setvalue(self, key: str, value: any) -> any:
        # Get old value.
        oldval = self._object.get(key, None)

        # Update value.
        self._object[key] = value
        return oldval


    # Reads the config file specified by *fname*.
    # The internal settings object is updated.
    # 
    # Returns True on success, False on failure.
    def readconfig(self, fname: str = '.env') -> bool:
        try:
            self._object = dotenv.dotenv_values(fname)
        except Exception as tmp_e:
            logging.critical(f'Failed to read "{fname}" configuration file. Desc: {tmp_e}')

            return False

        # Everything went well.
        return True


    # Writes the current configuration to the ".env" file.
    #
    # Returns True on success, False on failure.
    def writeconfig(self, fname: str = '.env') -> bool:
        try:
            with open(fname, 'w') as tmp_file:
                for key, value in self._object.items():
                    tmp_file.write(f'{key} = {value}\n')
        except Exception as tmp_e:
            logging.error(f'Failed to write to configuration file "{fname}". Desc: {tmp_e}')

            return False

        # Everything went well.
        return True


