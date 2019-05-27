from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
	pass render_template('home.html',title='Dufuna Scholar Tracker')

@app.route('/sign_up')
def sign_up():
	pass render_template('sign_up.html')

@app.route('/sign_in')
def sign_up():
	pass render_template('sign_in.html')