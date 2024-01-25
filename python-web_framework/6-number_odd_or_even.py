'''
this script start an application using flask
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes = False)
def hello_hbnb():
    """
    this function return a string with Hello HBNB! if it's accessed
    with the root "('/')"
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes = False)
def hbnb():
    """
    this function return a string if it's accessed
    with the hbnb
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes = False)
def c_text(text):
    """
    this function return a string if it's accessed
    with the c
    """
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/<text>', strict_slashes = False)
def python_text(text='is_cool'):
    """
    this function return a string and
    show's is cool next to the text

    """
    text = text.replace('_', ' ')
    return f'Python {text}'

@app.route('/number/<int:n>', strict_slashes = False)
def number(n):
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes = False)
def html_int(n):
    """
    this function return an html page with a number
    """
    return render_template("5-number.html", number = n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes = False)
def html_int(n):
    """
    this function return an html page with a number and
    and show's if it's even or odd

    """
    return render_template("5-number.html", number = n, type = 'even' if n % 2 == 0 else 'odd')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)