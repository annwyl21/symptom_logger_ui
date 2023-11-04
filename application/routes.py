from flask import render_template, request
from application import app
from application.forms import RecordForm
from application.storage import Symptom_log
from datetime import datetime

@app.route('/')
def index():
	return render_template('index.html', title='Home')

@app.route('/add_symptom', methods=['GET', 'POST'])
def add_symptom():
	form = RecordForm()
	if request.method == 'POST':
		pain_score = form.pain.data
		symptom = form.symptom.data

		now = datetime.now()
		date = now.strftime("%Y-%m-%d")
		time = now.strftime("%Y-%m-%d")

		result = Symptom_log.add_a_symptom(date, time, pain_score, symptom)

		if result:
			return render_template('success.html', title="Success", pain=pain_score, symptom=symptom, date=date, time=time)
		
		else:
			return render_template('error.html', title="Error", pain=pain_score, symptom=symptom, date=date, time=time)
	
	return render_template('add_symptom.html', title='Add Symptom', form=form)

@app.route('/summary')
def summary():

	# Retrieve data from database
	# Parcel it into the json for the api
	# make the api request - visualize
	# make the api request - summarize
	# add ai button and boolean
	# display the results
	
	return render_template('summary.html', title='Summary')
