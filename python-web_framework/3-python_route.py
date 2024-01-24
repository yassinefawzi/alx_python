from flask import Flask

'''assigning flask to app'''
app = Flask(__name__)

#assigning the app route to the root with ignoring slashes
@app.route('/', strict_slashes = False)
def hello_hbnb():
    # creating a function that return text if called by root
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes = False)
def hbnb():
    # creating a function that return text if called by hbnb
    return "HBNB"

@app.route('/c/<text>', strict_slashes = False)
def c_text(text):
    # creating a function that return text with the string next to it
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/<text>', strict_slashes = False)
def python_text(text='is_cool'):
    # creating a function that return text
    text = text.replace('_', ' ')
    return f'Python {text}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)