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


@app.route('/hbnb', strict_slashes = False)
def hbnb():
    '''creating a function that return text if called by hbnb'''
    return("HBNB")

@app.route('/c/<text>', strict_slashes = False)
def c_text(text):
    '''creating a function that return text with the string next to it'''
    text = text.replace('_', ' ')
    return f"C {text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)