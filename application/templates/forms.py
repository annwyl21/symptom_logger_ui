from wtforms import SubmitField, StringField, IntegerField
from flask_wtf import FlaskForm

class RecordForm(FlaskForm):
	symptoms = StringField('Symptoms')
	pain = IntegerField('Pain')
	submit = SubmitField('Submit')