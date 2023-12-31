from flask import render_template, request
from application import app
from application.forms import RecordForm
from application.storage import Symptom_log
from application.api_connections import ApiConnect
from datetime import datetime

@app.route('/')
def index():
	return render_template('index.html', title='Home')

@app.route('/add_symptom', methods=['GET', 'POST'])
def add_symptom():
	form = RecordForm()
	if request.method == 'POST':
		pain_score = form.pain.data
		if pain_score == None:
			pain_score = 0
		symptom = form.symptom.data

		now = datetime.now()
		date = now.strftime("%Y-%m-%d")
		time = now.strftime("%H:%M")

		result = Symptom_log.add_a_symptom(date, time, pain_score, symptom)

		if result == True:
			return render_template('success.html', title="Success", pain=pain_score, symptom=symptom, date=date, time=time)
		
		else:
			return render_template('error.html', title="Error", pain=pain_score, symptom=symptom, date=date, time=time)
	
	return render_template('add_symptom.html', title='Add Symptom', form=form)

@app.route('/summary')
def summary():

	# Retrieve data from database
	print("requesting data")
	result = Symptom_log.get_all_symptoms()

	# Parcel it into the json for the api
	print("creating parcel")
	parcel = Symptom_log.create_symptom_list(result)

	# make the api request - visualize
	print("requesting visuals")
	visualize_response = ApiConnect.request_visuals(parcel)
	print("visuals received")
		
	scatterplot_url = visualize_response['scatterplot']
	bubbleplot_url = visualize_response['bubbleplot']


	# make the api request - summarize
	print("requesting summary")
	summary = ApiConnect.request_summary(parcel)
	print("summary received")
	
	return render_template('summary.html', title='Summary', scatterplot_url=scatterplot_url, bubbleplot_url=bubbleplot_url, summary=summary)
