from flask import Flask


app = Flask(__name__)

from routes.routes import *
from database.load_templates import *
