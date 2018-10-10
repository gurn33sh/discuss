from flask import render_template, url_for, Blueprint
from forum.forms import LoginForm, RegistrationForm
#from forum import app

views = Blueprint('views', __name__)
@views.route('/')
def index():
  return render_template('index.html')

@views.route('/login')
def login():
  form = LoginForm()
  return render_template('login.html', form=form)

@views.route('/register')
def register():
  form = RegistrationForm()
  return render_template('register.html', form=form)