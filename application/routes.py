from flask import render_template, request
from application import app

@app.route('/')
def index():
	return render_template('index.html', title='Home')