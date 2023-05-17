# __init__.py
from flask import Flask,render_template, request,redirect
from flask_cors import CORS
app = Flask(__name__)
app.secret_key = "something secret"
CORS(app)

DATABASE = "tvshows_db"
