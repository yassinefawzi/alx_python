from flask import Flask, render_template

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

def python_text(text='is_cool'):
    # creating a function that return text
    text = text.replace('_', ' ')
    return f'Python {text}'

@app.route('/number/<int:n>', strict_slashes = False)
def number(n):
    # creating a function that return a string if n is a number
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes = False)
def html_int(n):
    # creating a function that display a web page if n is a number
    return render_template("5-number.html", number = n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes = False)
def html_int(n):
    # creating a function that display a web page if n is a number and showing if it's odd or even
    return render_template("5-number.html", number = n, type = 'even' if n % 2 == 0 else 'odd')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)