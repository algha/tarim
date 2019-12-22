
class Rule:
    """
    :type = ['native', 'secondary', 'option']
    """
    def __init__(self, name, rule = '',
                 methods = None,
                 endpoint = None,
                 type = ['native', 'option'],
                 method = None):
        self.name = name
        self.rule = rule
        self.endpoint = endpoint
        self.method = method
        self.type = type
        if self.method:
            self.type = ['secondary']

        if not isinstance(methods, list) and methods:
            self.methods = [methods]
        else:
            self.methods = methods

    def getMethodsOfSecondary(self):
        if self.hasNative():
            return None
        return self.methods

    def isRule(self, endpoint):
        return endpoint.endswith(self.name)

    def hasNative(self):
        return self.hasType('native')

    def hasSecondary(self):
        return self.hasType('secondary')

    def hasOption(self):
        return self.hasType('option')

    def hasType(self, type):
        if type in self.type:
            return True
        return False
