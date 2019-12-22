from flask import (send_from_directory, render_template)

class BaseTemplate(object):

    template = None

    @classmethod
    def render(cls, template = None, **kwargs):
        if template:
            return render_template(template, **kwargs)
        return render_template(cls.template, **kwargs)
