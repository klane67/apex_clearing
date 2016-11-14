from __future__ import unicode_literals

from ..structs import DictStruct


class User(DictStruct):
    fields = ['userName', 'userEntity', 'userClass']
