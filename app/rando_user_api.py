import requests

class Randomly():
	def __init__(self, 
		title="",
		first="", 
		last="", 
		picture=None,
		email="",
		cell="",
		gender="",

		):
		
		self.title = title
		self.first = first
		self.last = last
		self.picture = picture
		self.email = email
		self.cell = cell
		self.gender = gender

class RandoUserAPI():
	def __init__(self):
		self.base_url = "https://randomuser.me/api/"


	def generate_rando(self):


		url = "{}{}".format(self.base_url, "?results=10")
		r = requests.get(url)
		result = r.json()

		rando_list = []

		x = 9
		# while x > 0:
		bootilicious = Randomly(
			title = result["results"][0]["name"]["title"],
			first = result["results"][0]["name"]["first"],
			last = result["results"][0]["name"]["last"],
			picture = result["results"][0]["picture"]["thumbnail"],
			email = result["results"][0]["email"],
			cell = result["results"][0]["cell"],
			gender = result["results"][0]["gender"]
		)

		rando_list.append(bootilicious)
		for i in rando_list:
			print(i)
			# x -= 1

		return rando_list