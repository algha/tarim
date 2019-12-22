from jinja2 import nodes
from jinja2.ext import Extension
from jinja2.nodes import ContextReference

class PullableExtension(Extension):
    tags = set(['push','pull'])

    def __init__(self, environment):
        super(PullableExtension, self).__init__(environment)
        self.push = {}

    def parse(self, parser):
        """Parse tokens """
        tag = parser.stream.__next__()
        ctx_ref = ContextReference()

        if tag.value == "push":
            args = [ctx_ref, parser.parse_expression(), nodes.Const(tag.lineno)]
            body = parser.parse_statements(['name:endpush'], drop_needle=True)
            callback = self.call_method('compiled', args)
        else:
            args = [ctx_ref, parser.parse_expression()]
            body = []
            callback = self.call_method('scope', args)

        return nodes.CallBlock(callback, [], [], body).set_lineno(tag.lineno)

    def scope(self, context, tagname, caller):
        if tagname in self.push:
            return self.push[tagname]
        return ''

    def compiled(self, context, tagname, linenum, caller):
        self.push[tagname] = caller()
        return ''
