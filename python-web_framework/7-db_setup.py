from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import re
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)

#connecting to the database 
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_username}:{db_password}@{db_host}/{db_name}'


db = SQLAlchemy(app)

#User model with primary key id name and unique email
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(65))
    email = db.Column(db.String(75), unique=True, nullable=False)

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()  # This calls the function to create tables


@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)