from wtforms import Form, StringField, IntegerField, validators, ValidationError

class WordCount(Form):
	count = StringField("Enter a sentence.", validators=[validators.DataRequired()])

#class TimesTable(Form):
#	column = IntegerField("Enter number of columns.", validators=[validators.DataRequired()])
#	row = IntegerField("Enter number of rows.", validators=[validators.DataRequired()])