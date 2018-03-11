from StringIO import StringIO
from zipfile import ZipFile

from flask import Flask, Response, request, jsonify, make_response

from filters.basic_files_filter import BasicFilesFilter
from filters.helper_filter import HelperFilter
from filters.license_filter import LicenseFilter
from filters.web_filter import WebFilter

# Initialize the Flask application
app = Flask(__name__)


# REST Service methods

# handle undefined routes
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': str(error)}), 404)


# `builder` method takes get arguments and packs the files accordingly
@app.route('/builder', methods=['GET'])
def builder():
    # initializing a StringIO object
    in_memory_output_file = StringIO()

    # initializing a ZipFile object with StringIO object as a file
    zip_file = ZipFile(in_memory_output_file, 'w')

    # create a filter chain
    license_handler = LicenseFilter()
    helper_handler = HelperFilter(license_handler)
    basic_files_handler = BasicFilesFilter(helper_handler)
    web_filter_handler = WebFilter(basic_files_handler)

    # start the process
    web_filter_handler.handle_request(zip_file, request.args)

    # return the warning if there is nothing to zip into
    if in_memory_output_file.len == 0:
        # no file to pack
        zip_file.close()
        return not_found("No file to pack")

    # close the open ZipFile object
    zip_file.close()
    in_memory_output_file.seek(0)

    # return response which is StringIO object packed as a ZipFile
    return Response(in_memory_output_file,
                    mimetype='application/zip',
                    headers={
                        'Content-Disposition': 'attachment;filename=pythonizr.zip'
                    })


if __name__ == '__main__':
    app.run(
        host="localhost"
    )
