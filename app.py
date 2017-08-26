from StringIO import StringIO
from datetime import datetime
from zipfile import ZipFile

from flask import Flask, Response, request, jsonify, make_response

from boilerplate_templates.basic_templates import readme_rst_template, \
    main_py_template, test_basic_template, setup_py_template
from boilerplate_templates.helpers_templates import gitignore_template, \
    cfg_handler_template, arg_parse_template
from boilerplate_templates.license_templates import mit_license_template, \
    apache_license_template, gnu_license_template

# Initialize the Flask application
app = Flask(__name__)



# `setup_py` adds a setup.py file with a sample project
def setup_py(zip_file):
    zip_file.writestr('setup.py', setup_py_template)

    # sample project and test directories
    zip_file.writestr('sample/__init__.py', '')
    zip_file.writestr('sample/main.py', main_py_template)
    zip_file.writestr('tests/test_basic.py', test_basic_template)


# `readme_str` adds a sample README.str file
def readme_rst(zip_file):
    zip_file.writestr('README.rst', readme_rst_template)


# `requirements_txt` adds an empty requirements.txt file
def requirements_txt(zip_file):
    # empty file
    zip_file.writestr('requirements.txt', '')


# `manifest_in` adds a MANIFEST.in file for the sample project
def manifest_in(zip_file):
    manifest_content = ''

    global is_license
    if is_license:
        manifest_content += 'include LICENSE.txt'

    zip_file.writestr('MANIFEST.in', manifest_content)


# `main_py` adds a main.py file with basic boilerplate
def main_py(zip_file):
    zip_file.writestr('main.py', main_py_template)



# `gitignore` adds a .gitignore file for git based python repo
def gitignore(zip_file):
    zip_file.writestr('.gitignore', gitignore_template)


def config_handler(zip_file):
    zip_file.writestr('config/__init__.py', '')
    zip_file.writestr('config/cfg.ini', '')
    zip_file.writestr('config/cfg_handler.py', cfg_handler_template)


def arg_parse(zip_file):
    zip_file.writestr('argparse_helper.py', arg_parse_template)



def mit_license(zip_file):
    zip_file.writestr('LICENSE.txt',
                      mit_license_template.format(datetime.now().year))


def apache_license(zip_file):
    zip_file.writestr('LICENSE.txt',
                      apache_license_template.format(datetime.now().year))


# `gnu_license` adds GNU GPLv3 License in LICENSE.txt file
def gnu_license(zip_file):
    zip_file.writestr('LICENSE.txt',
                      gnu_license_template.format(datetime.now().year))


def empty_license(zip_file):
    zip_file.writestr('LICENSE.txt', '')


# REST Service methods

# handle undefined routes
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': str(error)}), 404)


@app.route('/builder', methods=['GET'])
def builder():
    global func
    global is_license

    # Initializing StringIO object
    in_memory_output_file = StringIO()

    zip_file = ZipFile(in_memory_output_file, 'w')

    # Check if license.txt file is requested
    if 'no_license' not in request.args:
        is_license = True

    for req in request.args:
        if req in func:
            func[req](zip_file)

    if in_memory_output_file.len == 0:
        # no file to pack
        zip_file.close()
        return not_found("No file to pack")

    zip_file.close()
    in_memory_output_file.seek(0)

    return Response(in_memory_output_file,
                    mimetype='application/zip',
                    headers={
                        'Content-Disposition': 'attachment;filename=sample.zip'
                    })

'''
A Dictionary to hold function wrt GET arguments, 
each function takes ZipFile object as arguments and adds files/dir in it.
'''
func = {'main_py': main_py, 'setup_py': setup_py, 'readme_rst': readme_rst,
        'requirements_txt': requirements_txt, 'manifest_in': manifest_in,
        'gitignore': gitignore, 'config_handler': config_handler,
        'argparse': arg_parse,
        'mit_license': mit_license, 'apache_license': apache_license,
        'gnu_license': gnu_license, 'empty_license': empty_license}

is_license = False

if __name__ == '__main__':
    app.run(
        host="localhost"
    )
