from app.core.validation import Validation
from app.core.utils.helper import str2arr
from app.core.utils.helper import isarr, getArrRoot, getArrChild

from .layout import Layout

class Form(Layout):

    template = '/partials/layouts/form.html'

    def __init__(self, fomrData = None, dataKey = None):
        super().__init__()
        self.validationError = []
        self.formData = fomrData
        self.dataKey = dataKey

    def build(self, **kwargs):
        return self.render(fields = self.fieldRefactor(), **kwargs)

    def fieldRefactor(self):
        if self.getQuery() is None:
            return self.fields()
        fields = []
        for field in self.fields():
            field.setValue(self.getQuery())
            fields.append(field)
        return fields

    def fields(self):
        return []

    def validation(self):
        return {}

    def isValidated(self):
        for name, regex in self.validation().items():
            value = self.formData[str2arr(name)]
            validation = Validation(regex, value, name)
            if validation.isValid() == False:
                self.validationError.append(validation.getErrors())
        return len(self.validationError) == 0

    def FormData(self, formData):
        self.formData = formData
        return self

    def getValidationError(self):
        return self.validationError

    def getFormData(self):
        arr = {}
        for key, value in self.formData.items():
            if '[]' in key:
                value = self.formData.getlist(key)
                key = key.replace('[]','')

            if isarr(key) == True:
                root = getArrRoot(key)
                if root not in arr:
                    arr[root] = {}
                child = getArrChild(key)
                arr[root][child] = value
            else:
                arr[key] = value
        if self.dataKey is not None and self.dataKey in arr:
            return arr[self.dataKey]
        return arr
