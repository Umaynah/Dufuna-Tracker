from flask import render_template
from app import app

@app.route('/')
def home():
	return render_template('home.html',title='Dufuna Scholar Tracker')

@app.route('/sign_up.html')
def sign_up():
	return render_template('sign_up.html')

@app.route('/sign_in.html')
def sign_in():
	return render_template('sign_in.html')