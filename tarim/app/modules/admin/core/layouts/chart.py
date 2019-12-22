from .layout import Layout

class Chart(Layout):

    template = '/partials/layouts/chart.html'

    def __init__(self):
        super().__init__()

    def build(self, data = None, **kwargs):
        return self.render(fields = self.fields())
