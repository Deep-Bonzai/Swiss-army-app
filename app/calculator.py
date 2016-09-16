
class Calculator():
	def __init__(self):
		self.add_magic = 0

	def addition(self, number1, number2):
		self.add_magic = number1 + number2
		return self.add_magic