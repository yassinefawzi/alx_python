'''
this is a script that use flask framework
in this script i start an application hosted in 0.0.0.0 and use the port 5000
in this script i coded the following functions
hello_hbnb, hbnb, c_text, python_text, html_int, html_intt

'''

from flask import Flask, render_template

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
    return "HBNB"

@app.route('/c/<text>', strict_slashes = False)
def c_text(text):
    '''creating a function that return text with the string next to it'''
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/<text>', strict_slashes = False)
def python_text(text='is_cool'):
    '''creating a function that return text'''
    text = text.replace('_', ' ')
    return f'Python {text}'

@app.route('/number_template/<int:n>', strict_slashes = False)
def html_int(n):
    '''creating a function that display a web page if n is a number'''
    return render_template("5-number.html", number = n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes = False)
def html_intt(n):
    '''creating a function that display
       a web page if n is a number.

    '''
    return render_template('6-number_odd_or_even.html', number = n, type = 'even' if n % 2 == 0 else 'odd')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)