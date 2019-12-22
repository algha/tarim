from .layout import Layout

class Metric(Layout):

    template = '/partials/layouts/metric.html'

    def __init__(self):
        super().__init__() 

    def build(self, data = None, **kwargs):
        return self.render()
