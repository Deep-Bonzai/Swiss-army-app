
class Calculator():
	def __init__(self):
		self.add_magic = 0.00

	def addition(self, number1, number2):
		self.add_magic = number1 + number2
		return self.add_magic

	def subtraction(self, number1, number2):
		self.subtract_magic = number1 - number2
		return self.subtract_magic

	def multiplication(self, number1, number2):
		self.multiply_magic = number1 * number2
		return self.multiply_magic

	def division(self, number1, number2):
		if number2 == 0:
			self.divide_magic = 0
		else:
			self.divide_magic = number1 / number2
		return self.divide_magic