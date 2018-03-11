from boilerplate_templates.web_templates import app_py_template
from filters.base_filter import BaseFilter


# `flask_single_module` adds flask simple project with single module
def add_flask_single_module(zip_file):
    zip_file.writestr('app.py', app_py_template)
    zip_file.writestr('config.py', '')


class WebFilter(BaseFilter):

    def handle_request(self, zip_file, args):

        if 'flask_single_module' in args:
            add_flask_single_module(zip_file)

        # handle successor if provided
        if self._successor is not None:
            self._successor.handle_request(zip_file, args)
