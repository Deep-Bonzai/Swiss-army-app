from wtforms import Form, StringField, IntegerField, validators, ValidationError, RadioField

class WordCount(Form):
	count = StringField("Enter a sentence.", validators=[validators.DataRequired()])

#class TimesTable(Form):
#	column = IntegerField("Enter number of columns.", validators=[validators.DataRequired()])
#	row = IntegerField("Enter number of rows.", validators=[validators.DataRequired()])

class CalculatorForm(Form):
	number1 = IntegerField("Enter first number", validators=[validators.DataRequired()])
	number2 = IntegerField("Enter second number", validators=[validators.DataRequired()])
	operator = RadioField("Operators",
		default = "+ Add",
		choices = [
			("+ Add", "+ Add"),
			("- Subtract", "- Subtract"),
			("* Multiply", "* Multiply"),
			("/ Divide", "/ Divide")
		])