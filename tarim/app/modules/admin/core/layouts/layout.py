from flask import render_template

class Layout:

    data = ''
    name = ''

    template = None

    width = ''

    classList = []

    def __init__(self):
        self.classList = [self.width] + self.classList

    def render(self, **kwargs):
        return render_template(self.template,
                               width = self.width,
                               _class = self.getClassList(),
                               data = self.getQuery(),
                               **kwargs)

    def build(self, **kwargs):
        return self.render(**kwargs)

    def getClassList(self):
        return ' '.join(self.classList)

    def setRepository(self, repository):
        self.repository = repository
        return self

    def getRepository(self):
        return self.repository

    def getQuery(self, key = None):
        if key:
            return self.repository.get(key)
        return self.repository.get(self.data)

    def getChild(self, key):
        if key in self.getQuery():
            return self.getQuery()[key]
        return None
