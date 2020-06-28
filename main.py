import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug = os.environ.get('DEBUG') == 'True', host = '0.0.0.0', port = os.environ.get('PORT'))

# @app.route('/say-bye')
# def say_bye():
#     return 'Goodbye!'

