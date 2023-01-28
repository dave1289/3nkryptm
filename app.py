from flask import Flask, redirect, render_template, session, request, flash
from models import connect_db, db

app = Flask(__name__)

# standardized sqlalchemy init setting and variable structure
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hashing'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODICATIONS'] = False
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.app_context().push()

connect_db(app)

@app.route('/')
def show_home():
    return render_template('home.html')