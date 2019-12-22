from flask import render_template
from collections.abc import Iterable
from app.core.utils.helper import str2arr, array2str
import json


class FieldAttribute(object):
    def __init__(self, **kwargs):
        self.initAttributes()

    def initAttributes(self):
        self.attributes = {
            'name': None
        }

    def renderAttr(self):
        attrs = []
        for key, value in self.attributes.items():
            attr = ''
            if isinstance(value, str):
                classAttr = 'get{}'.format(key.capitalize())
                if hasattr(self, classAttr):
                    value = getattr(self, classAttr)()
                attr = '{}="{}"'.format(key, value)
            elif isinstance(value, bool) and value:
                attr = '{}="{}"'.format(key, key)
            attrs.append(attr)
        return ' '.join(attrs)

    def set(self, name, value = None):
        self.attributes[name] = value
        return self

    def get(self, name):
        if name in self.attributes:
            return self.attributes[name]
        return ''

    def inAttributes(self, key):
        return key in self.attributes

    def required(self, required = True):
        self.set('required', required)
        return self

class FieldDataAttribute(FieldAttribute):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initDataAttributes()

    def initDataAttributes(self):
        self.dataAttributes = {}

    def setData(self, key, value):
        self.dataAttributes[key] = value
        return self

    def renderDataAttr(self):
        attrs = []
        for key, value in self.dataAttributes.items():
            key = '{}-{}'.format(self.dataAttrPrefix() ,key)
            attr = '{}="{}"'.format(key, value)
            attrs.append(attr)
        return ' '.join(attrs)

    def parseDataAttr(self, data):
        try:
            data = json.loads(data)
            for key, value in data.items():
                if key in data:
                    self.setData(key, value)
        except:
            pass

    def dataAttrPrefix(self):
        return 'data'

class Field(FieldDataAttribute):

    template = None
    type = ''
    title = ''

    def __init__(self, name = None, label = None, **kwargs):
        super().__init__(**kwargs)
        if name:
            self.setName(name)
        if label:
            self.label = label


    def render(self, **kwargs):
        return render_template(self.template, field = self)

    def setLabel(self, label):
        self.label = label
        return self

    def setName(self, name):
        self.set('name', str2arr(name))
        return self

    def setValue(self, value):
        _value = self._setValue(value)
        if self.inAttributes('value'):
            self.set('value', _value)
        else:
            self.value = _value

    def _setValue(self, value):
        _value = ''
        name = self.getOldName()
        if name is None:
            return _value
        if '.' not in name:
            if hasattr(value, name):
                _value = getattr(value, name)
            elif isinstance(value, Iterable) and name in value:
                _value = value[name]
        else:
            _value = self.getValueOfData(value, name)

        return _value


    def getOldName(self):
        name = self.get('name')
        return array2str(name)

    def getValueOfData(self, value, name):
        names = name.replace('[]', '').split('.')
        _value = value
        for name in names:
            if isinstance(_value, Iterable):
                if name in _value:
                    _value = _value[name]
                else:
                    _value = None
            elif hasattr(_value, name):
                _value = getattr(_value, name)
            else:
                _value = None
        return _value
