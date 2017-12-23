from datetime import datetime

from base_filter import BaseFilter
from boilerplate_templates.license_templates import mit_license_template, \
    gnu_license_template, apache_license_template


def write_license_file(zip_file, content):
    zip_file.writestr('LICENSE.txt', content)


class LicenseFilter(BaseFilter):

    def handle_request(self, zip_file, args):

        if 'mit_license' in args:
            write_license_file(zip_file,
                               mit_license_template.format(datetime.now().year))

        elif 'apache_license' in args:
            write_license_file(zip_file,
                               apache_license_template.format(datetime.now().year))

        elif 'gnu_license' in args:
            write_license_file(zip_file,
                               gnu_license_template.format(datetime.now().year))

        elif 'empty_license' in args:
            write_license_file(zip_file, '')


        # handle successor if provided
        if self._successor is not None:
            self._successor.handle_request(zip_file, args)
