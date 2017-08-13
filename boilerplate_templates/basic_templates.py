
# Templates for basic files

readme_rst_template='''
A sample Python project
=======================

This is the README file for the project.

The file should use UTF-8 encoding and be written using `reStructuredText
<http://docutils.sourceforge.net/rst.html>`_. It
will be used to generate the project webpage on PyPI and will be displayed as
the project homepage on common code-hosting services, and should be written for
that purpose.

Typical contents for this file would include an overview of the project, basic
usage examples, etc. Generally, including the project changelog in here is not
a good idea, although a simple "What's New" section for the most recent version
may be appropriate.
'''


setup_py_template = '''# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package description',
    long_description=readme,
    author='<author_name>',
    author_email='author@example.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests'))
)
'''

test_basic_template = '''
# added to demonstrate `find_packages` example in
# setup.py that excludes installing the "tests" package


def test_success():
    assert True
'''

main_py_template = '''
def main():
    print('main function')

if __name__ == "__main__":
    main()
'''
