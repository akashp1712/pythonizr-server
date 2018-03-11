app_py_template = '''
from flask import Flask, make_response, jsonify

app = Flask(__name__)


# REST Service methods

# handle undefined routes
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': str(error)}), 404)


# default route
@app.route('/', methods=['GET'])
def builder():

    return make_response(jsonify({'data': "This is sample response"}))


if __name__ == '__main__':
    app.run(
        host="localhost"
    )

'''