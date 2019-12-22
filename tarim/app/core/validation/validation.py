class Validation:
    def __init__(self, regex, value, name):
        self.regex = regex
        self.value = value
        self.name = name
        self.error = ''

    def isValid(self):
        regexes = self.regex.split('|')
        for regex in regexes:
            if regex == 'required' and len(self.value) == 0:
                self.error = '{} is required.'.format(self.name)
                return False

    def getErrors(self):
        return self.error
