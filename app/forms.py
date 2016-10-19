from wtforms import Form, DecimalField, StringField, IntegerField, validators, ValidationError, RadioField

class WordCount(Form):
	count = StringField("Enter Words to Count", validators=[validators.DataRequired()])

class CalculatorForm(Form):
	number1 = DecimalField("Enter first number", default=0.0, validators=[validators.DataRequired()])
	number2 = DecimalField("Enter second number", default=0.0, validators=[validators.DataRequired()])
	operator = RadioField("Operators",
		default = "+ Add",
		choices = [
			("+ Add", "+ Add"),
			("- Subtract", "- Subtract"),
			("* Multiply", "* Multiply"),
			("/ Divide", "/ Divide")
		])

class RepoForm(Form):
	username = StringField("Enter the Username of Interest", validators=[validators.DataRequired()])