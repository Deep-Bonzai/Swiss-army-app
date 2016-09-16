from flask import render_template, request
from collections import Counter

from app import app
from app.forms import WordCount, CalculatorForm
from app.good_file import GoodFile
from app.calculator import Calculator


@app.route("/", methods=["GET", "POST"])
def index():
	return render_template("index.html")

@app.route("/word_counter", methods=["GET", "POST"])
def word_counter():
	word_count = WordCount(request.form)
	good_stuff = GoodFile()

#sets initial value for variables

#'if' protects for shitty empty form
	if request.method == "POST" and word_count.validate():
		phrase_length = good_stuff.number_words(word_count)
		char_length = good_stuff.number_char(word_count)
		max_key = good_stuff.common_word(word_count)
		frequent_letter = good_stuff.common_char(word_count)

	return render_template("word_counter.html", good_stuff=good_stuff, word_count=word_count)

@app.route("/times_table", methods=["GET", "POST"])
def times_table():
	#times_table_form = TimesTable(request.form)


	return render_template("times_table.html")

@app.route("/calculator", methods=["GET", "POST"])
def calculator():
	calculator_form = CalculatorForm(request.form)
	math_magic = Calculator()

	number1 = calculator_form.number1.data
	number2 = calculator_form.number2.data
	add_magic = math_magic.addition(number1, number2)


	return render_template("calculator.html",calculator_form=calculator_form,math_magic=math_magic,add_magic=add_magic,number1=number1,number2=number2)
