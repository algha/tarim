from app.modules.admin.core.fields import *
from .fields.category import CategoryField
from .fields.tag import TagField
from orator.orm import Collection
from app import algha

class FieldsList():

    def __init__(self):
        fields = []

        for field in algha.getFields():
            input = FieldType(field.title, field.type, field)
            fields.append(input)
            
        self.fields = fields

    def as_dict(self):
        data = {}
        for field in self.fields:
            data[field.type] = field.name
        return data

    def getFieldObject(self, key):
        collection = Collection(self.fields)
        item = collection.first(lambda item: item.type == key)
        return item.obj



class FieldType():

    def __init__(self, name, type, obj):
        self.name = name
        self.type = type
        self.obj  = obj
