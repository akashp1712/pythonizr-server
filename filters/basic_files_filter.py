from boilerplate_templates.basic_templates import readme_rst_template, \
    main_py_template, setup_py_template, test_basic_template
from filters.base_filter import BaseFilter


# `main_py` adds a main.py file with basic boilerplate
def add_main_py(zip_file):
    zip_file.writestr('main.py', main_py_template)


# `setup_py` adds a setup.py file with a sample project
def add_setup_py(zip_file):
    zip_file.writestr('setup.py', setup_py_template)

    # sample project and test directories
    zip_file.writestr('sample/__init__.py', '')
    zip_file.writestr('sample/main.py', main_py_template)
    zip_file.writestr('tests/test_basic.py', test_basic_template)


# `readme_str` adds a sample README.str file
def add_readme_rst(zip_file):
    zip_file.writestr('README.rst', readme_rst_template)


# `requirements_txt` adds an empty requirements.txt file
def add_requirements_txt(zip_file):
    # empty file
    zip_file.writestr('requirements.txt', '')


# `manifest_in` adds a MANIFEST.in file for the sample project
def add_manifest_in(zip_file, content):
    zip_file.writestr('MANIFEST.in', content)


class BasicFilesFilter(BaseFilter):

    def handle_request(self, zip_file, args):

        if 'main_py' in args:
            add_main_py(zip_file)

        if 'setup_py' in args:
            add_setup_py(zip_file)

        if 'readme_rst' in args:
            add_readme_rst(zip_file)

        if 'requirements_txt' in args:
            add_requirements_txt(zip_file)

        if 'manifest_in' in args:
            manifest_content = ''
            # build the content for the manifest file according to the arguments

            if 'no_license' not in args: # Check if license.txt file is requested
                manifest_content += 'include LICENSE.txt'

            add_manifest_in(zip_file, manifest_content)

        # handle successor if provided
        if self._successor is not None:
            self._successor.handle_request(zip_file, args)
