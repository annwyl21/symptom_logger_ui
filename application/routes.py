from flask import render_template
from application import app
from application.forms import RecordForm

@app.route('/')
def index():
	return render_template('index.html', title='Home')

@app.route('/add_symptom', methods=['GET', 'POST'])
def add_symptom():
	form = RecordForm()
	return render_template('add_symptom.html', title='Add Symptom', form=form)
