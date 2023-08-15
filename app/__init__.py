from flask import Flask

#Create an instance of the Flask class
app = Flask(__name__)


# import all of the routes from the routes file into the current package
# This must be imported at the bottom of the file
from app import routes
