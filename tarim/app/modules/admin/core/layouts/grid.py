from .layout import Layout

class Grid(Layout):

    template = '/partials/layouts/grid.html'

    def __init__(self):
        super().__init__() 

    def build(self, data = None, **kwargs):
        return self.render()
