'''
importing flask and starting the app
'''

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes = False)
def hello_hbnb():
    """
    this function return a string with Hello HBNB! if it's accessed
    with the root
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)