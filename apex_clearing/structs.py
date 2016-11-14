from __future__ import unicode_literals

from enum import Enum


class DictStructList(list):
    def to_dict(self):
        return [v.to_dict() if isinstance(v, DictStruct) else v
                for v in self]


class DictStruct:
    fields = {}  # or list for all simple optional fields

    def __init__(self, json: dict):
        if isinstance(self.fields, (list, tuple)):
            self.fields = {field: None for field in self.fields}
        assert isinstance(self.fields, dict)
        for field, params in self.fields.items():
            try:
                required = bool(params[1])
            except (TypeError, IndexError):
                required = False

            try:
                converter = params[0]
            except (TypeError, IndexError):
                converter = None

            # find field name in dict
            try:
                v = json[field]
            except KeyError as e:
                if not required:
                    continue
                raise KeyError("Cannot find '{field}'[required] in {class}."
                               .format(**{
                    'field': field,
                    'class': self.__class__.__name__,
                }))

            if v is not None:
                if callable(converter):
                    if isinstance(converter, list):
                        converter = converter[0]
                        v = DictStructList(converter(i) for i in v)
                    else:
                        v = converter(v)
                if isinstance(v, Enum):
                    v = v.value
            setattr(self, field, v)

    def to_dict(self):
        return {
            k: (v.to_dict()
                if isinstance(v, (DictStruct, DictStructList))
                else v)
            for k, v in self.__dict__.items()
            }
