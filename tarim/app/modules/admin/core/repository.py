class Repository():
    def __init__(self, query):
        self.query = query

    def get(self, key):
        if key in self.query:
            return self.query[key]
        return None

    def getRawQuery(self):
        return self.query
