from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# config

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')
db = SQLAlchemy(app)

from . import views
from . import models
