from flask import Flask
from database.load_templates import init_db


app = Flask(__name__)

init_db()

from routes.routes import *
