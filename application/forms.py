from wtforms import SubmitField, StringField, IntegerField
from flask_wtf import FlaskForm

class RecordForm(FlaskForm):
	symptom = StringField('Symptom')
	pain = IntegerField('Pain')
	submit = SubmitField('Submit')