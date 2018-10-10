from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/smooth/Desktop/g/test.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  Bootstrap(app)
  db.init_app(app)
  app.register_blueprint(views)
  with app.app_context():
    db.create_all()
  return app

from forum import models
from forum.views import *