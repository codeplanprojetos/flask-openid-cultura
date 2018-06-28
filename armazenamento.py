# -*- coding: utf-8 -*-
from os import environ, sep, path, getcwd
from configparser import ConfigParser

class Storage:

    def __init__(self):
        if path.exists('./config/env.cfg'):
            self.config = ConfigParser()
            self.config.read('./config/session.cfg')
        else:
            self.config = ConfigParser()

    def __setitem__(self, key, value):
        self.config[key] = value
        self.config.write('./config/session.cfg')

    def __getitem__(self, key):
        return self.config[key]

