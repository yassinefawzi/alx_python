from flask import Flask

'''assigning flask to app'''
app = Flask(__name__)

'''assigning the app route to the root with ignoring slashes'''
@app.route('/', strict_slashes = False)
def hello_hbnb():
    '''creating a function that return text if opened by root'''
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes = False)
def hbnb():
    '''creating a function that return text if called by hbnb'''
    return("HBNB")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)